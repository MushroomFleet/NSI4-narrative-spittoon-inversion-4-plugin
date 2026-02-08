#!/usr/bin/env python3
"""
NSL 1.1 Converter — Converts between bucket folder structure and NSL XML format.

Usage:
    python nsl-converter.py export --bucket ./bucket --story ./STORY --output story.nsl
    python nsl-converter.py import --input story.nsl --bucket ./bucket --story ./STORY
"""

import argparse
import os
import sys
import json
import re
from datetime import datetime
from xml.etree.ElementTree import (
    Element, SubElement, tostring, parse, indent, ElementTree
)
from xml.dom import minidom
from pathlib import Path


def read_file(path):
    """Read a file and return its content."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path, content):
    """Write content to a file, creating directories as needed."""
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def detect_format(filename):
    """Detect file format from extension."""
    ext = Path(filename).suffix.lower()
    format_map = {
        '.md': 'markdown',
        '.txt': 'text',
        '.json': 'json',
        '.mermaid': 'mermaid',
        '.yaml': 'yaml',
        '.yml': 'yaml',
    }
    return format_map.get(ext, 'text')


def extract_title_from_lorebook(bucket_path):
    """Extract story title from LoreBook.md."""
    lorebook = os.path.join(bucket_path, 'LoreBook.md')
    if os.path.exists(lorebook):
        content = read_file(lorebook)
        match = re.search(r'#\s*LoreBook:\s*(.+)', content)
        if match:
            return match.group(1).strip()
    return 'Untitled Story Project'


def extract_tag_content(content, tag):
    """Extract content between XML-style tags in markdown files."""
    pattern = rf'<{tag}>(.*?)</{tag}>'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else content


def export_bucket(bucket_path, story_path, output_path):
    """Export bucket folder + story pages to NSL 1.1 XML file."""

    title = extract_title_from_lorebook(bucket_path)
    now = datetime.now(tz=__import__('datetime').timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Root element
    root = Element('NarrativeBucket', version='1.1',
                   xmlns='http://narrative-spittoon.org/nsl/1.1')

    # --- Metadata ---
    metadata = SubElement(root, 'Metadata')
    SubElement(metadata, 'Title').text = title
    SubElement(metadata, 'Created').text = now
    SubElement(metadata, 'Modified').text = now
    SubElement(metadata, 'StoryStructure').text = '6-page-inversion'

    # --- ProjectManifest ---
    manifest = SubElement(root, 'ProjectManifest')
    manifest_file = os.path.join(bucket_path, 'project-instructions.md')
    if os.path.exists(manifest_file):
        overview = SubElement(manifest, 'Overview')
        overview.text = read_file(manifest_file)
    else:
        overview = SubElement(manifest, 'Overview')
        overview.text = f'Narrative Spittoon Inversion project: {title}'

    # --- CognitiveFrameworks ---
    frameworks = SubElement(root, 'CognitiveFrameworks')

    framework_files = {
        'NarrativeSpittoon': 'NarrativeSpittoon.md',
        'GhostWritingStyle': 'GhostWritingStyle.md',
        'HolographicTutor': 'HolographicTutor.md',
    }

    for tag, filename in framework_files.items():
        filepath = os.path.join(bucket_path, filename)
        if os.path.exists(filepath):
            elem = SubElement(frameworks, tag, format='markdown')
            content_elem = SubElement(elem, 'Content')
            content = read_file(filepath)
            # Strip the outer XML-style tags if present
            content = extract_tag_content(content, tag)
            content_elem.text = content

    # --- Universe ---
    universe = SubElement(root, 'Universe')
    world_file = os.path.join(bucket_path, 'world.md')
    if not os.path.exists(world_file):
        # Try capitalized version
        world_file = os.path.join(bucket_path, 'World.md')
    if os.path.exists(world_file):
        world_desc = SubElement(universe, 'WorldDescription', format='markdown')
        content = read_file(world_file)
        # Try multiple tag names
        for tag_name in ['World', 'WorldParadistro']:
            extracted = extract_tag_content(content, tag_name)
            if extracted != content:
                content = extracted
                break
        world_desc.text = content

    # --- Characters ---
    characters = SubElement(root, 'Characters')
    chars_file = os.path.join(bucket_path, 'characters.md')
    if not os.path.exists(chars_file):
        chars_file = os.path.join(bucket_path, 'Characters.md')
    if os.path.exists(chars_file):
        content = read_file(chars_file)
        # Parse individual character blocks
        char_blocks = re.findall(r'<(\w+)>\s*(.*?)\s*</\1>', content, re.DOTALL)
        for char_name, char_content in char_blocks:
            if char_name.lower() == 'characters':
                continue
            char_elem = SubElement(characters, 'Character', id=char_name.lower())
            SubElement(char_elem, 'Name').text = char_name

            # Parse fields
            for field in ['Summary', 'Background', 'Quirks', 'Description', 'Role',
                         'Personality', 'Motivations', 'Relationships']:
                match = re.search(rf'{field}:\s*(.+?)(?=\n\w+:|$)', char_content, re.DOTALL)
                if match:
                    SubElement(char_elem, field).text = match.group(1).strip()

    # --- SpeechStyles (embedded in Characters or separate) ---
    speech_file = os.path.join(bucket_path, 'speechstyles.md')
    if not os.path.exists(speech_file):
        speech_file = os.path.join(bucket_path, 'SpeechStyles.md')
    if os.path.exists(speech_file):
        content = read_file(speech_file)
        speech_blocks = re.findall(r'<(\w+[Ss]peech)>\s*(.*?)\s*</\1>', content, re.DOTALL)
        for speech_name, speech_content in speech_blocks:
            # Find matching character element or create speech style doc
            char_base = re.sub(r'[Ss]peech$', '', speech_name).lower()
            # Try to find existing character element
            found = False
            for char_elem in characters:
                if char_elem.get('id', '').lower() == char_base:
                    speech_elem = SubElement(char_elem, 'SpeechStyle')
                    SubElement(speech_elem, 'SampleDialogue').text = speech_content.strip()
                    found = True
                    break
            if not found:
                # Add as supplementary document if no matching character
                pass

    # --- TechnicalSpecifications ---
    json_files = list(Path(bucket_path).glob('*.json'))
    if json_files:
        tech_specs = SubElement(root, 'TechnicalSpecifications')
        for jf in json_files:
            spec = SubElement(tech_specs, 'Specification',
                            id=jf.stem, format='json', type='data')
            SubElement(spec, 'Title').text = jf.stem.replace('-', ' ').replace('_', ' ').title()
            content_elem = SubElement(spec, 'Content')
            content_elem.text = read_file(str(jf))

    # --- VisualizationResources ---
    mermaid_files = list(Path(bucket_path).glob('*.mermaid'))
    if mermaid_files:
        viz = SubElement(root, 'VisualizationResources')
        for mf in mermaid_files:
            v = SubElement(viz, 'Visualization',
                          id=mf.stem, format='mermaid', type='diagram')
            SubElement(v, 'Title').text = mf.stem.replace('-', ' ').replace('_', ' ').title()
            content_elem = SubElement(v, 'Content')
            content_elem.text = read_file(str(mf))

    # --- SupplementaryDocuments ---
    supp_files = []
    for ext in ['*.txt']:
        supp_files.extend(Path(bucket_path).glob(ext))
    # Also include LoreBook
    lorebook = Path(bucket_path) / 'LoreBook.md'
    if lorebook.exists():
        supp_files.append(lorebook)

    if supp_files:
        supp_docs = SubElement(root, 'SupplementaryDocuments')
        for sf in supp_files:
            doc = SubElement(supp_docs, 'Document',
                           id=sf.stem.lower(), format=detect_format(sf.name),
                           type='reference')
            SubElement(doc, 'Title').text = sf.stem.replace('-', ' ').replace('_', ' ').title()
            content_elem = SubElement(doc, 'Content')
            content_elem.text = read_file(str(sf))

    # --- StoryContent ---
    if story_path and os.path.exists(story_path):
        page_files = sorted(Path(story_path).glob('page*.md'),
                          key=lambda p: int(re.search(r'(\d+)', p.stem).group(1))
                          if re.search(r'(\d+)', p.stem) else 0)

        if page_files:
            story = SubElement(root, 'StoryContent', type='single')
            narrative = SubElement(story, 'SingleNarrative', structure='6-page-inversion')

            struct_meta = SubElement(narrative, 'StructureMetadata')
            SubElement(struct_meta, 'Methodology').text = 'reverse-chronological'
            SubElement(struct_meta, 'StartingPage').text = str(len(page_files) - 1)
            gen_order = ','.join(str(len(page_files) - 1 - i) for i in range(len(page_files)))
            SubElement(struct_meta, 'GenerationOrder').text = gen_order

            pages = SubElement(narrative, 'Pages')
            for pf in page_files:
                page_num = int(re.search(r'(\d+)', pf.stem).group(1))
                page = SubElement(pages, 'Page', number=str(page_num), status='completed')

                content = read_file(str(pf))

                # Extract title if present
                title_match = re.search(r'^#\s*Page\s*\d+:\s*(.+)', content, re.MULTILINE)
                if title_match:
                    SubElement(page, 'Title').text = title_match.group(1).strip()

                content_elem = SubElement(page, 'Content', format='markdown')
                content_elem.text = content

                page_meta = SubElement(page, 'Metadata')
                SubElement(page_meta, 'WordCount').text = str(len(content.split()))

    # --- Write output ---
    indent(root)
    tree = ElementTree(root)

    # Use minidom for prettier output
    xml_str = tostring(root, encoding='unicode', xml_declaration=True)
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent='  ', encoding='UTF-8').decode('utf-8')

    write_file(output_path, pretty_xml)
    print(f'Exported to: {output_path}')
    print(f'File size: {os.path.getsize(output_path):,} bytes')


def import_nsl(input_path, bucket_path, story_path):
    """Import an NSL 1.1 XML file into bucket folder + story pages."""

    tree = parse(input_path)
    root = tree.getroot()

    # Handle namespace
    ns = ''
    ns_match = re.match(r'\{(.+)\}', root.tag)
    if ns_match:
        ns = f'{{{ns_match.group(1)}}}'

    def find(parent, tag):
        """Find element with or without namespace."""
        elem = parent.find(f'{ns}{tag}')
        if elem is None:
            elem = parent.find(tag)
        return elem

    def findall(parent, tag):
        """Find all elements with or without namespace."""
        elems = parent.findall(f'{ns}{tag}')
        if not elems:
            elems = parent.findall(tag)
        return elems

    os.makedirs(bucket_path, exist_ok=True)
    os.makedirs(story_path, exist_ok=True)

    files_created = []

    # --- Extract CognitiveFrameworks ---
    frameworks = find(root, 'CognitiveFrameworks')
    if frameworks is not None:
        for tag in ['NarrativeSpittoon', 'GhostWritingStyle', 'HolographicTutor']:
            elem = find(frameworks, tag)
            if elem is not None:
                content_elem = find(elem, 'Content')
                content = content_elem.text if content_elem is not None else (elem.text or '')
                filepath = os.path.join(bucket_path, f'{tag}.md')
                write_file(filepath, f'<{tag}>\n{content.strip()}\n</{tag}>\n')
                files_created.append(filepath)

    # --- Extract Universe ---
    universe = find(root, 'Universe')
    if universe is not None:
        world_desc = find(universe, 'WorldDescription')
        if world_desc is not None:
            content = world_desc.text or ''
            filepath = os.path.join(bucket_path, 'world.md')
            write_file(filepath, f'<World>\n{content.strip()}\n</World>\n')
            files_created.append(filepath)

    # --- Extract Characters ---
    characters = find(root, 'Characters')
    if characters is not None:
        char_content = '<Characters>\n'
        speech_content = '<SpeechStyles>\n'
        has_speech = False

        for char in findall(characters, 'Character'):
            char_id = char.get('id', 'unknown')
            name_elem = find(char, 'Name')
            name = name_elem.text if name_elem is not None else char_id

            char_content += f'\n<{name}>\n'
            for field in ['Summary', 'Background', 'Quirks', 'Description', 'Role',
                         'Personality', 'Motivations', 'Relationships']:
                field_elem = find(char, field)
                if field_elem is not None and field_elem.text:
                    char_content += f'{field}: {field_elem.text.strip()}\n'
            char_content += f'</{name}>\n'

            # Extract speech style
            speech_style = find(char, 'SpeechStyle')
            if speech_style is not None:
                has_speech = True
                speech_content += f'\n<{name}Speech>\n'
                sample = find(speech_style, 'SampleDialogue')
                if sample is not None and sample.text:
                    speech_content += sample.text.strip() + '\n'
                else:
                    for child in speech_style:
                        tag_name = child.tag.replace(ns, '') if ns else child.tag
                        if child.text:
                            speech_content += f'{tag_name}: {child.text.strip()}\n'
                speech_content += f'</{name}Speech>\n'

        char_content += '\n</Characters>\n'
        filepath = os.path.join(bucket_path, 'characters.md')
        write_file(filepath, char_content)
        files_created.append(filepath)

        if has_speech:
            speech_content += '\n</SpeechStyles>\n'
            filepath = os.path.join(bucket_path, 'speechstyles.md')
            write_file(filepath, speech_content)
            files_created.append(filepath)

    # --- Extract TechnicalSpecifications ---
    tech_specs = find(root, 'TechnicalSpecifications')
    if tech_specs is not None:
        for spec in findall(tech_specs, 'Specification'):
            spec_id = spec.get('id', 'spec')
            fmt = spec.get('format', 'json')
            content_elem = find(spec, 'Content')
            if content_elem is not None and content_elem.text:
                ext = '.json' if fmt == 'json' else f'.{fmt}'
                filepath = os.path.join(bucket_path, f'{spec_id}{ext}')
                write_file(filepath, content_elem.text.strip())
                files_created.append(filepath)

    # --- Extract VisualizationResources ---
    viz = find(root, 'VisualizationResources')
    if viz is not None:
        for v in findall(viz, 'Visualization'):
            v_id = v.get('id', 'diagram')
            fmt = v.get('format', 'mermaid')
            content_elem = find(v, 'Content')
            if content_elem is not None and content_elem.text:
                ext = '.mermaid' if fmt == 'mermaid' else f'.{fmt}'
                filepath = os.path.join(bucket_path, f'{v_id}{ext}')
                write_file(filepath, content_elem.text.strip())
                files_created.append(filepath)

    # --- Extract SupplementaryDocuments ---
    supp = find(root, 'SupplementaryDocuments')
    if supp is not None:
        for doc in findall(supp, 'Document'):
            doc_id = doc.get('id', 'document')
            fmt = doc.get('format', 'text')
            content_elem = find(doc, 'Content')
            if content_elem is not None and content_elem.text:
                ext_map = {'markdown': '.md', 'text': '.txt', 'json': '.json'}
                ext = ext_map.get(fmt, '.txt')
                filepath = os.path.join(bucket_path, f'{doc_id}{ext}')
                write_file(filepath, content_elem.text.strip())
                files_created.append(filepath)

    # --- Extract StoryContent ---
    story_content = find(root, 'StoryContent')
    if story_content is not None:
        # Handle single narrative
        single = find(story_content, 'SingleNarrative')
        if single is not None:
            pages_elem = find(single, 'Pages')
            if pages_elem is not None:
                for page in findall(pages_elem, 'Page'):
                    page_num = page.get('number', '0')
                    content_elem = find(page, 'Content')
                    if content_elem is not None and content_elem.text:
                        filepath = os.path.join(story_path, f'page{page_num}.md')
                        write_file(filepath, content_elem.text.strip())
                        files_created.append(filepath)

        # Handle series/volumes
        volumes_elem = find(story_content, 'Volumes')
        if volumes_elem is not None:
            for volume in findall(volumes_elem, 'Volume'):
                vol_num = volume.get('number', '1')
                vol_dir = os.path.join(story_path, f'volume{vol_num}')
                os.makedirs(vol_dir, exist_ok=True)

                pages_elem = find(volume, 'Pages')
                if pages_elem is not None:
                    for page in findall(pages_elem, 'Page'):
                        page_num = page.get('number', '0')
                        content_elem = find(page, 'Content')
                        if content_elem is not None and content_elem.text:
                            filepath = os.path.join(vol_dir, f'page{page_num}.md')
                            write_file(filepath, content_elem.text.strip())
                            files_created.append(filepath)

    # --- Generate project-instructions.md ---
    manifest_content = generate_manifest(bucket_path)
    manifest_path = os.path.join(bucket_path, 'project-instructions.md')
    write_file(manifest_path, manifest_content)
    files_created.append(manifest_path)

    print(f'Imported from: {input_path}')
    print(f'Files created: {len(files_created)}')
    for f in files_created:
        print(f'  {f}')


def generate_manifest(bucket_path):
    """Generate a project-instructions.md from bucket contents."""
    files = sorted(os.listdir(bucket_path))

    frameworks = []
    universe = []
    characters = []
    tech = []
    viz = []
    other = []

    framework_names = ['NarrativeSpittoon.md', 'GhostWritingStyle.md', 'HolographicTutor.md']
    char_names = ['characters.md', 'Characters.md', 'speechstyles.md', 'SpeechStyles.md']
    world_names = ['world.md', 'World.md']

    for f in files:
        if f in framework_names:
            frameworks.append(f)
        elif f in world_names or f.endswith('-glossary.txt'):
            universe.append(f)
        elif f in char_names:
            characters.append(f)
        elif f.endswith('.json'):
            tech.append(f)
        elif f.endswith('.mermaid'):
            viz.append(f)
        elif f not in ['project-instructions.md', 'LoreBook.md']:
            other.append(f)

    lines = ['# Project Instructions\n']

    if frameworks:
        lines.append('\n## Cognitive Framework Definition')
        for f in frameworks:
            lines.append(f'- {f}')

    if universe:
        lines.append('\n## Universe Core Documentation')
        for f in universe:
            lines.append(f'- {f}')

    if characters:
        lines.append('\n## Character Profiles')
        for f in characters:
            lines.append(f'- {f}')

    if tech:
        lines.append('\n## Technical Specifications')
        for f in tech:
            lines.append(f'- {f}')

    if viz:
        lines.append('\n## Visualization Resources')
        for f in viz:
            lines.append(f'- {f}')

    if other:
        lines.append('\n## Other Files')
        for f in other:
            lines.append(f'- {f}')

    lines.append('\n## Content Structure Tags')
    lines.append('- The setting is defined inside "world.md"')
    lines.append('- Character personality definitions are in "characters.md"')
    lines.append('- Speech patterns are defined in "speechstyles.md"')

    lines.append('\n## Processing Framework')
    lines.append('- Cross-referenced document relationships')
    lines.append('- Technical specification integration')
    lines.append('- Visualization resource utilization')

    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(
        description='NSL 1.1 Converter — Convert between bucket folders and NSL XML format'
    )
    subparsers = parser.add_subparsers(dest='command', help='Operation to perform')

    # Export subcommand
    export_parser = subparsers.add_parser('export', help='Export bucket to NSL XML')
    export_parser.add_argument('--bucket', required=True, help='Path to bucket/ directory')
    export_parser.add_argument('--story', default=None, help='Path to STORY/ directory')
    export_parser.add_argument('--output', required=True, help='Output .nsl file path')

    # Import subcommand
    import_parser = subparsers.add_parser('import', help='Import NSL XML to bucket')
    import_parser.add_argument('--input', required=True, help='Input .nsl file path')
    import_parser.add_argument('--bucket', required=True, help='Output bucket/ directory')
    import_parser.add_argument('--story', default='./STORY', help='Output STORY/ directory')

    args = parser.parse_args()

    if args.command == 'export':
        export_bucket(args.bucket, args.story, args.output)
    elif args.command == 'import':
        import_nsl(args.input, args.bucket, args.story)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
