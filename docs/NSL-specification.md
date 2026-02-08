# Narrative Spittoon Language (NSL) 1.0 Specification

## Document Information

- **Version**: 1.0
- **Status**: Draft Specification
- **Last Updated**: October 2025
- **Purpose**: Define a unified XML-based file format for Narrative Spittoon framework projects

---

## 1. Introduction

### 1.1 Overview

The Narrative Spittoon Language (NSL) is an XML-based file format standard designed to encapsulate all components of a narrative generation project using the Narrative Spittoon Inversion framework. NSL provides a semantic, extensible structure for storing narrative artifacts, cognitive frameworks, character definitions, world-building data, and supporting materials in a single portable file.

### 1.2 Design Goals

- **Unified Format**: Single file contains complete narrative bucket
- **Semantic Structure**: XML elements clearly describe content type and purpose
- **Multi-format Support**: Embed markdown, JSON, mermaid diagrams, and plain text
- **Extensibility**: New elements can be added without breaking compatibility
- **Tooling-friendly**: Enables development of parsers, editors, and generators
- **Human-readable**: Maintainable and reviewable by content creators

### 1.3 Use Cases

- Distributing complete narrative projects
- Version control of narrative assets
- Tool interoperability (editors, generators, analyzers)
- Archival and preservation of narrative frameworks
- Migration between narrative generation systems

---

## 2. File Format Specifications

### 2.1 File Properties

- **File Extension**: `.nsl`
- **MIME Type**: `application/xml` (proposed: `application/vnd.narrative-spittoon+xml`)
- **Character Encoding**: UTF-8
- **Line Endings**: Platform-agnostic (LF or CRLF)
- **XML Version**: 1.0

### 2.2 Naming Conventions

- Filename should describe the narrative project
- Use lowercase with hyphens for multi-word names
- Examples: `westwick-noir.nsl`, `moonbase-story.nsl`, `my-narrative-project.nsl`

### 2.3 File Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<NarrativeBucket version="1.0" xmlns="http://narrative-spittoon.org/nsl/1.0">
  <!-- Content sections -->
</NarrativeBucket>
```

---

## 3. XML Schema Definition

### 3.1 Root Element

#### `<NarrativeBucket>`

The root container for all narrative project data.

**Attributes:**
- `version` (required): NSL specification version (currently "1.0")
- `xmlns` (optional): XML namespace (http://narrative-spittoon.org/nsl/1.0)

**Child Elements:**
1. `<Metadata>` (required, singular)
2. `<CognitiveFrameworks>` (required, singular)
3. `<Universe>` (required, singular)
4. `<Characters>` (required, singular)
5. `<TechnicalSpecifications>` (optional, singular)
6. `<VisualizationResources>` (optional, singular)
7. `<SupplementaryDocuments>` (optional, singular)
8. `<StoryPages>` (optional, singular)

---

### 3.2 Metadata Section

#### `<Metadata>`

Contains project-level information and configuration.

**Child Elements:**

```xml
<Metadata>
  <Title>String</Title>                      <!-- required -->
  <Author>String</Author>                     <!-- optional -->
  <Created>ISO-8601 Date</Created>            <!-- optional -->
  <Modified>ISO-8601 Date</Modified>          <!-- optional -->
  <Version>String</Version>                   <!-- optional -->
  <Description>String</Description>           <!-- optional -->
  <Genre>String</Genre>                       <!-- optional -->
  <StoryStructure>String</StoryStructure>     <!-- optional -->
  <Tags>                                      <!-- optional -->
    <Tag>String</Tag>                         <!-- repeatable -->
  </Tags>
  <CustomFields>                              <!-- optional -->
    <Field key="String">Value</Field>         <!-- repeatable -->
  </CustomFields>
</Metadata>
```

**Field Definitions:**

- **Title**: Project name (e.g., "Westwick Noir Mystery")
- **Author**: Creator's name or pseudonym
- **Created**: Creation timestamp (ISO-8601 format: YYYY-MM-DDTHH:MM:SSZ)
- **Modified**: Last modification timestamp
- **Version**: Project version number (e.g., "1.0", "2.1-beta")
- **Description**: Brief project description
- **Genre**: Story genre (noir, sci-fi, fantasy, etc.)
- **StoryStructure**: Structure type (e.g., "6-page", "10-page", "20-page", "CYOA")
- **Tags**: Keyword tags for categorization
- **CustomFields**: Extensibility mechanism for user-defined metadata

---

### 3.3 Cognitive Frameworks Section

#### `<CognitiveFrameworks>`

Contains the three core instruction sets that guide narrative generation.

```xml
<CognitiveFrameworks>
  <NarrativeSpittoon format="markdown">
    <!-- Embedded markdown content -->
  </NarrativeSpittoon>
  
  <GhostWritingStyle format="markdown">
    <!-- Embedded markdown content -->
  </GhostWritingStyle>
  
  <HolographicTutor format="markdown">
    <!-- Embedded markdown content -->
  </HolographicTutor>
</CognitiveFrameworks>
```

**Attributes:**
- `format`: Content format ("markdown", "text", "xml")

**Content:**
Each framework element contains the complete instructional content as CDATA or embedded text.

**Example with CDATA:**
```xml
<NarrativeSpittoon format="markdown"><![CDATA[
# Narrative Spittoon Framework

## Implicit Causality
...
]]></NarrativeSpittoon>
```

---

### 3.4 Universe Section

#### `<Universe>`

Contains world-building and setting information.

```xml
<Universe>
  <WorldDescription format="markdown">
    <!-- Complete world description -->
  </WorldDescription>
  
  <Setting>
    <Era>String</Era>
    <Location>String</Location>
    <Environment>String</Environment>
  </Setting>
  
  <History format="markdown">
    <!-- Historical background -->
  </History>
  
  <Geography format="markdown">
    <!-- Geographic details -->
  </Geography>
  
  <Architecture format="markdown">
    <!-- Architectural style and details -->
  </Architecture>
  
  <Districts>
    <District id="unique-id">
      <Name>String</Name>
      <Description>String</Description>
      <Elevation>String</Elevation>
      <WaterLevel>String</WaterLevel>
      <SocialElements>String</SocialElements>
      <CrimeLevel>String</CrimeLevel>
      <NoirElements>String</NoirElements>
    </District>
    <!-- Repeatable -->
  </Districts>
  
  <PowerStructures format="markdown">
    <!-- Power dynamics -->
  </PowerStructures>
  
  <Technology format="markdown">
    <!-- Technological elements -->
  </Technology>
  
  <Culture format="markdown">
    <!-- Cultural atmosphere -->
  </Culture>
</Universe>
```

**Attributes:**
- `format`: Content format for flexible sections
- `id`: Unique identifier for districts and locations

---

### 3.5 Characters Section

#### `<Characters>`

Defines all characters with comprehensive attributes.

```xml
<Characters>
  <Character id="unique-character-id">
    <Name>String</Name>
    <Age>Integer</Age>
    <Heritage>String</Heritage>
    <Description>String</Description>
    <Personality>String</Personality>
    <Role>String</Role>
    
    <PhysicalAttributes>
      <Build>String</Build>
      <Height>String</Height>
      <Hair>String</Hair>
      <Eyes>String</Eyes>
      <DistinguishingMarks>String</DistinguishingMarks>
    </PhysicalAttributes>
    
    <Quirks>
      <Quirk>String</Quirk>  <!-- repeatable -->
    </Quirks>
    
    <Background format="markdown">
      <!-- Detailed background -->
    </Background>
    
    <SpeechStyle>
      <Vocabulary>String</Vocabulary>
      <SentenceStructure>String</SentenceStructure>
      
      <SpeakingPatterns>
        <Pattern>String</Pattern>  <!-- repeatable -->
      </SpeakingPatterns>
      
      <Catchphrases>
        <Phrase>String</Phrase>  <!-- repeatable -->
      </Catchphrases>
      
      <EmotionalTells>
        <WhenNervous>String</WhenNervous>
        <WhenExcited>String</WhenExcited>
        <WhenAngry>String</WhenAngry>
        <WhenSad>String</WhenSad>
      </EmotionalTells>
      
      <CulturalInfluences>String</CulturalInfluences>
    </SpeechStyle>
    
    <Relationships>
      <Relationship target="character-id" type="String">
        String
      </Relationship>  <!-- repeatable -->
    </Relationships>
  </Character>
  <!-- Repeatable -->
</Characters>
```

**Attributes:**
- `id`: Unique character identifier (kebab-case recommended)
- `target`: References another character by ID
- `type`: Relationship type (friend, rival, family, etc.)

---

### 3.6 Technical Specifications Section

#### `<TechnicalSpecifications>`

Contains structured data in JSON or other formats.

```xml
<TechnicalSpecifications>
  <Specification id="unique-spec-id" format="json" type="locations">
    <!-- Embedded JSON -->
  </Specification>
  
  <Specification id="unique-spec-id" format="json" type="technology">
    <!-- Embedded JSON -->
  </Specification>
  
  <Specification id="unique-spec-id" format="json" type="custom">
    <!-- Embedded JSON -->
  </Specification>
  <!-- Repeatable -->
</TechnicalSpecifications>
```

**Attributes:**
- `id`: Unique specification identifier
- `format`: Data format ("json", "xml")
- `type`: Specification category (locations, technology, characters, custom)

**Example:**
```xml
<Specification id="westwick-locations" format="json" type="locations"><![CDATA[
{
  "districts": {
    "the_heights": {
      "name": "The Heights",
      ...
    }
  }
}
]]></Specification>
```

---

### 3.7 Visualization Resources Section

#### `<VisualizationResources>`

Contains diagrams and visual representations.

```xml
<VisualizationResources>
  <Visualization id="unique-viz-id" format="mermaid" type="flowchart">
    <Title>String</Title>
    <Description>String</Description>
    <Content><![CDATA[
      <!-- Mermaid diagram code -->
    ]]></Content>
  </Visualization>
  <!-- Repeatable -->
</VisualizationResources>
```

**Attributes:**
- `id`: Unique visualization identifier
- `format`: Diagram format ("mermaid", "dot", "plantuml", "svg")
- `type`: Diagram type (flowchart, graph, sequence, class, etc.)

---

### 3.8 Supplementary Documents Section

#### `<SupplementaryDocuments>`

Additional supporting materials and reference documents.

```xml
<SupplementaryDocuments>
  <Document id="unique-doc-id" format="markdown" type="glossary">
    <Title>String</Title>
    <Description>String</Description>
    <Content><![CDATA[
      <!-- Document content -->
    ]]></Content>
  </Document>
  
  <Document id="unique-doc-id" format="text" type="narrative-hooks">
    <Title>String</Title>
    <Description>String</Description>
    <Content><![CDATA[
      <!-- Document content -->
    ]]></Content>
  </Document>
  <!-- Repeatable -->
</SupplementaryDocuments>
```

**Attributes:**
- `id`: Unique document identifier
- `format`: Content format (markdown, text, html)
- `type`: Document category (glossary, narrative-hooks, procedures, reference, custom)

---

### 3.9 Story Pages Section

#### `<StoryPages>`

Optional section for storing generated story content.

```xml
<StoryPages structure="6-page">
  <Page number="0" status="completed">
    <Title>String</Title>
    <Content format="markdown"><![CDATA[
      <!-- Page content -->
    ]]></Content>
    <Metadata>
      <Created>ISO-8601 Date</Created>
      <WordCount>Integer</WordCount>
      <Notes>String</Notes>
    </Metadata>
  </Page>
  <!-- Repeatable -->
</StoryPages>
```

**Attributes:**
- `structure`: Story structure type (6-page, 10-page, 20-page, CYOA)
- `number`: Page sequence number (0-based or 1-based depending on structure)
- `status`: Page status (completed, draft, outline, placeholder)
- `format`: Content format (markdown, text, html)

---

## 4. Data Types and Constraints

### 4.1 String Types

- **String**: Unicode text, no length restriction unless specified
- **ID**: Lowercase alphanumeric with hyphens, must be unique within scope
- **ISO-8601 Date**: Standard date/time format (YYYY-MM-DDTHH:MM:SSZ)

### 4.2 Numeric Types

- **Integer**: Whole number (e.g., age, word count)

### 4.3 Enumerated Types

**Format Types:**
- `markdown` - Markdown formatted text
- `text` - Plain text
- `json` - JSON data structure
- `yaml` - YAML data structure
- `xml` - XML data structure
- `html` - HTML formatted text
- `mermaid` - Mermaid diagram syntax
- `dot` - GraphViz DOT syntax
- `svg` - Scalable Vector Graphics

**Document Types:**
- `glossary` - Terminology definitions
- `narrative-hooks` - Story prompts and hooks
- `procedures` - Systematic procedures
- `reference` - Reference materials
- `custom` - User-defined category

---

## 5. Validation Rules

### 5.1 Required Elements

The following elements are required in every NSL file:
- `<NarrativeBucket>` with version attribute
- `<Metadata>` with `<Title>`
- `<CognitiveFrameworks>` with all three frameworks
- `<Universe>` with at least `<WorldDescription>`
- `<Characters>` with at least one `<Character>`

### 5.2 ID Uniqueness

All `id` attributes must be unique within their scope:
- Character IDs unique within `<Characters>`
- District IDs unique within `<Districts>`
- Specification IDs unique within `<TechnicalSpecifications>`
- Visualization IDs unique within `<VisualizationResources>`
- Document IDs unique within `<SupplementaryDocuments>`

### 5.3 Reference Integrity

- Relationship `target` attributes must reference valid character IDs
- Cross-references between sections should use valid IDs

### 5.4 Content Encoding

- Use CDATA sections for content containing special XML characters
- Ensure UTF-8 encoding throughout
- Escape XML entities when not using CDATA: `&amp;` `&lt;` `&gt;` `&quot;` `&apos;`

---

## 6. Usage Examples

### 6.1 Minimal NSL File

```xml
<?xml version="1.0" encoding="UTF-8"?>
<NarrativeBucket version="1.0">
  <Metadata>
    <Title>My Story Project</Title>
    <Created>2025-10-18T08:00:00Z</Created>
  </Metadata>
  
  <CognitiveFrameworks>
    <NarrativeSpittoon format="markdown"><![CDATA[
# Narrative Spittoon Framework
[Framework content here]
    ]]></NarrativeSpittoon>
    
    <GhostWritingStyle format="markdown"><![CDATA[
# Ghost Writing Style
[Style guide content here]
    ]]></GhostWritingStyle>
    
    <HolographicTutor format="markdown"><![CDATA[
# Holographic Tutor
[Evaluation framework here]
    ]]></HolographicTutor>
  </CognitiveFrameworks>
  
  <Universe>
    <WorldDescription format="markdown"><![CDATA[
# World Setting
A mysterious world where...
    ]]></WorldDescription>
  </Universe>
  
  <Characters>
    <Character id="protagonist">
      <Name>Jane Doe</Name>
      <Age>32</Age>
      <Description>A determined investigator</Description>
      <Role>Protagonist</Role>
      <SpeechStyle>
        <Vocabulary>Professional but accessible</Vocabulary>
      </SpeechStyle>
    </Character>
  </Characters>
</NarrativeBucket>
```

### 6.2 Complete NSL File Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<NarrativeBucket version="1.0" xmlns="http://narrative-spittoon.org/nsl/1.0">
  <Metadata>
    <Title>Westwick Noir: Shadows and Tides</Title>
    <Author>J. Smith</Author>
    <Created>2025-10-18T08:00:00Z</Created>
    <Modified>2025-10-18T08:15:00Z</Modified>
    <Version>1.0</Version>
    <Description>A noir detective story set in a semi-flooded city</Description>
    <Genre>Noir, Mystery, Alternate History</Genre>
    <StoryStructure>6-page</StoryStructure>
    <Tags>
      <Tag>noir</Tag>
      <Tag>detective</Tag>
      <Tag>retrofuturistic</Tag>
    </Tags>
  </Metadata>
  
  <CognitiveFrameworks>
    <!-- Three framework definitions -->
  </CognitiveFrameworks>
  
  <Universe>
    <WorldDescription format="markdown"><![CDATA[
# Westwick: Noir City Profile
...
    ]]></WorldDescription>
    
    <Setting>
      <Era>Alternate 1950s America</Era>
      <Location>Boston area, coastal New England</Location>
      <Environment>Semi-flooded coastal city</Environment>
    </Setting>
    
    <Districts>
      <District id="the-heights">
        <Name>The Heights</Name>
        <Elevation>45-60 feet above sea level</Elevation>
        <WaterLevel>None</WaterLevel>
        <Description>Wealthy district on high ground</Description>
      </District>
    </Districts>
  </Universe>
  
  <Characters>
    <Character id="maya-chen">
      <Name>Maya Chen-Williams</Name>
      <Age>34</Age>
      <Heritage>Chinese and African American</Heritage>
      <Description>Tall, athletic forensic archaeologist</Description>
      <Role>Forensic archaeologist</Role>
      
      <SpeechStyle>
        <Vocabulary>Academic and precise</Vocabulary>
        <Catchphrases>
          <Phrase>Context is everything.</Phrase>
          <Phrase>Historically speaking...</Phrase>
        </Catchphrases>
      </SpeechStyle>
    </Character>
  </Characters>
  
  <TechnicalSpecifications>
    <Specification id="locations" format="json" type="locations"><![CDATA[
{
  "districts": {
    "the_heights": {...}
  }
}
    ]]></Specification>
  </TechnicalSpecifications>
  
  <VisualizationResources>
    <Visualization id="city-layout" format="mermaid" type="graph">
      <Title>Westwick City Layout</Title>
      <Description>District relationships and elevation map</Description>
      <Content><![CDATA[
graph TD
  A[The Heights] --> B[The Stilts]
  B --> C[The Shallows]
      ]]></Content>
    </Visualization>
  </VisualizationResources>
  
  <SupplementaryDocuments>
    <Document id="glossary" format="markdown" type="glossary">
      <Title>Westwick Glossary</Title>
      <Description>Setting-specific terminology</Description>
      <Content><![CDATA[
# Westwick Glossary
- **Lunar tech**: Technology derived from moon research
- **The Depths**: Completely flooded district
      ]]></Content>
    </Document>
  </SupplementaryDocuments>
  
  <StoryPages structure="6-page">
    <Page number="5" status="completed">
      <Title>The Final Confrontation</Title>
      <Content format="markdown"><![CDATA[
The fog rolled in thick that night...
      ]]></Content>
      <Metadata>
        <Created>2025-10-18T08:00:00Z</Created>
        <WordCount>1500</WordCount>
      </Metadata>
    </Page>
  </StoryPages>
</NarrativeBucket>
```

---

## 7. Best Practices

### 7.1 Content Organization

1. **Use CDATA sections** for multi-line content and content with special characters
2. **Keep IDs descriptive** and consistent (use kebab-case)
3. **Include comprehensive metadata** for better project management
4. **Document custom fields** in comments or project documentation

### 7.2 Formatting Guidelines

1. **Indent consistently** (2 or 4 spaces recommended)
2. **One section per line** for better diff visibility
3. **Group related elements** logically
4. **Add comments** to explain complex structures

### 7.3 Version Control

1. **Store NSL files** in version control systems (Git)
2. **Use meaningful commit messages** when updating narrative elements
3. **Tag releases** with semantic versioning
4. **Consider splitting** very large files (though NSL encourages single-file)

### 7.4 Extensibility

1. **Use `<CustomFields>`** in Metadata for project-specific data
2. **Add new optional sections** at root level for future extensions
3. **Prefix custom elements** with your namespace to avoid conflicts
4. **Document extensions** in accompanying documentation

---

## 8. Migration Guide

### 8.1 From Folder-Based Bucket to NSL

**Step 1: Create NSL Structure**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<NarrativeBucket version="1.0">
  <!-- Sections will be populated -->
</NarrativeBucket>
```

**Step 2: Migrate Metadata**
- Extract project information from README or project-instructions.md
- Convert to `<Metadata>` section

**Step 3: Migrate Cognitive Frameworks**
- Copy NarrativeSpittoon.md → `<NarrativeSpittoon>`
- Copy GhostWritingStyle.md → `<GhostWritingStyle>`
- Copy HolographicTutor.md → `<HolographicTutor>`
- Wrap content in CDATA sections

**Step 4: Migrate World Building**
- Copy World.md → `<Universe><WorldDescription>`
- Extract structured data into appropriate subsections

**Step 5: Migrate Characters**
- Convert Characters.md/json → `<Characters>` section
- Map fields to NSL character structure
- Integrate SpeechStyles.md data into `<SpeechStyle>` subsections

**Step 6: Migrate Technical Specs**
- Copy JSON files → `<TechnicalSpecifications>`
- Assign appropriate `type` attributes

**Step 7: Migrate Visualizations**
- Copy .mermaid files → `<VisualizationResources>`
- Include titles and descriptions

**Step 8: Migrate Supplementary Docs**
- Copy glossaries, procedures, hooks → `<SupplementaryDocuments>`
- Assign appropriate `type` attributes

**Step 9: Optional - Migrate Story Pages**
- Copy generated pages → `<StoryPages>`
- Preserve page numbering and status

### 8.2 Automated Conversion

A conversion tool should:
1. Read folder structure
2. Parse each file according to format
3. Map to NSL structure
4. Generate valid NSL XML
5. Validate against schema
6. Output .nsl file

---

## 9. Tools and Ecosystem

### 9.1 Reference Implementation

Future tools should support:
- **NSL Parser**: Read and validate NSL files
- **NSL Writer**: Generate NSL from data structures
- **NSL Validator**: Check conformance to specification
- **NSL Converter**: Migrate folder structures to NSL

### 9.2 Editor Support

Recommended features:
- XML validation with NSL schema
- Syntax highlighting for embedded formats (markdown, JSON, mermaid)
- Character/world browser interface
- Visual diagram rendering
- Export to folder structure

### 9.3 Integration Points

NSL files can integrate with:
- AI narrative generation systems
- Story planning tools
- Character management software
- World-building applications
- Version control systems
- Collaborative writing platforms

---

## 10. Future Considerations

### 10.1 Potential Extensions

- **NSL 2.0**: Enhanced multimedia support (images, audio)
- **Localization**: Multi-language support in single file
- **Encryption**: Sensitive content protection
- **Compression**: Built-in compression for large files
- **Remote References**: Link to external resources
- **Collaborative Annotations**: Change tracking and comments

### 10.2 Backward Compatibility

Future versions should:
- Support reading NSL 1.0 files
- Provide migration paths
- Maintain core structure
- Add optional elements only

---

## 11. Appendix

### 11.1 Complete Schema Summary

```
NarrativeBucket (version)
├── Metadata (required)
│   ├── Title (required)
│   ├── Author
│   ├── Created
│   ├── Modified
│   ├── Version
│   ├── Description
│   ├── Genre
│   ├── StoryStructure
│   ├── Tags
│   │   └── Tag (repeatable)
│   └── CustomFields
│       └── Field (repeatable)
│
├── CognitiveFrameworks (required)
│   ├── NarrativeSpittoon (required)
│   ├── GhostWritingStyle (required)
│   └── HolographicTutor (required)
│
├── Universe (required)
│   ├── WorldDescription (required)
│   ├── Setting
│   │   ├── Era
│   │   ├── Location
│   │   └── Environment
│   ├── History
│   ├── Geography
│   ├── Architecture
│   ├── Districts
│   │   └── District (repeatable)
│   ├── PowerStructures
│   ├── Technology
│   └── Culture
│
├── Characters (required)
│   └── Character (repeatable, at least one)
│       ├── Name
│       ├── Age
│       ├── Heritage
│       ├── Description
│       ├── Personality
│       ├── Role
│       ├── PhysicalAttributes
│       ├── Quirks
│       ├── Background
│       ├── SpeechStyle
│       │   ├── Vocabulary
│       │   ├── SentenceStructure
│       │   ├── SpeakingPatterns
│       │   ├── Catchphrases
│       │   ├── EmotionalTells
│       │   └── CulturalInfluences
│       └── Relationships
│
├── TechnicalSpecifications
│   └── Specification (repeatable)
│
├── VisualizationResources
│   └── Visualization (repeatable)
│
├── SupplementaryDocuments
│   └── Document (repeatable)
│
└── StoryPages
    └── Page (repeatable)
```

### 11.2 Glossary

- **Narrative Bucket**: Complete collection of narrative project artifacts
- **Cognitive Framework**: Instructional module guiding narrative generation
- **NSL**: Narrative Spittoon Language
- **CDATA**: Character Data section for preserving special characters in XML

### 11.3 References

- XML 1.0 Specification: https://www.w3.org/TR/xml/
- ISO-8601 Date Format: https://www.iso.org/iso-8601-date-and-time-format.html
- UTF-8 Encoding: https://www.unicode.org/

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-18 | Initial specification release |

---

**End of Specification**
