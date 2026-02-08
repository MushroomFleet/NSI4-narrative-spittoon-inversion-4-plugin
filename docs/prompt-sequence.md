The "Narrative Spittoon Inversion" is a comprehensive workflow designed for AI-assisted story creation. It begins with manual setup and detailed story definition, followed by iterative LLM-driven generation and enhancement. The core process involves:

## Initialization: Defining your story's core elements (universe, characters, ending).

(optional) user may bring documents and artifacts to prime the interview, which should be read and understood before the interview begins:

## Overview

The Twenty Questions provides a systematic methodology for conducting focused, in-depth interviews through a series of 20 dynamically-generated questions. Each question builds upon previous responses, and all Q&A pairs are progressively captured in a continuously-updated markdown artifact. This creates a comprehensive knowledge document that evolves throughout the conversation.

## Core Concepts

### Progressive Artifact Building
- A markdown artifact is created at the start of the interview, named after the topic/task
- After each question is answered, the artifact is immediately updated with the Q&A pair
- The artifact serves as both a running transcript and a structured knowledge base
- Upon completion, the artifact contains the full interview with all 20 Q&A pairs

### Dynamic Question Generation
- Questions are not pre-scripted but generated adaptively based on:
  - Previous answers provided by the interviewee
  - Context from any attached or referenced materials
  - The overall topic/goal of the interview
  - Gaps in understanding that need to be filled
  - Natural conversation flow and relevance

The resulting Q&A interview will be used as the basis for the LoreBook.md, which will be saved inside @/bucket/


# Setup & Artifact Creation: Configuring the project structure and prompts, using specialized prompts to distill content into the required format.

This process requires the LoreBook.md (created manually or by earlier completion of the interview)

## bucket artifacts prompt (generates narrative data from Lore Book)
```
we need to distill the information inside LoreBook.md into separate artifacts.
- we will create a "world.md" that distills the description, history and culture of the world into a page.
- we will create a "characters.md" that lists the characters in the story and breaks down various attributes including but not limited to: description, age, race, personality, quirks, role.
- we will create a "speechstyles.md" which will describe the speech style of each character listed in the "characters.md" which aims to build in unique and deep personality by way of speech style
- all separate artifacts will be saved inside @/bucket/
```

We will then use @/world.md @characters.md @/speechstyles.md @/LoreBook.md as we complete the next prompt which will expand the artifacts, saving the newly created files inside @/bucket/

## extra artifacts prompt (generate artifacts based on world)
```
We need .mermaid charts to explain in detail characteristics about this world with separate technical .json files and a glossary of terms that are exclusive to this universe .txt format. These artifact will be created inside @/bucket/
```

## core files (copy into the bucket)

next, we copy in the template files "HolographicTutor.md", "GhostWritingStyle.md", "NarrativeSpittoon.md", which may be user editig but are considered core files in the narrative generation system. these must be saved inside @/bucket/

ghostwritingstyle.md:
```
<GhostWritingStyle>
Ghost Writing Style:
Vary sentence structure and length to avoid monotony. Break up long sentences. Tighten verbose passages. When varying syntax - mix simple and complex sentences.


Make dialogue flow naturally. Avoid repetitive beats. Interrupt debates with narrative, description, or actions. Emphasize interrupting lengthy dialogues with narrative, descriptions, actions more strongly. Don't let debates drag on.


Change up who is responding in conversations. Don't just go back and forth between two characters. Specify changing up who responds in a conversation - not just back and forth exchanges.


Inject realistic pauses, hesitations, filler words, and emotion into dialogue. Note the importance of injecting realistic pauses and emotions into conversations.


Use casual speech and verbal tics to differentiate character voices. Avoid overly sophisticated diction. Call out using casual speech, verbal tics, and filler words to make dialogue sound more natural.


Intersperse action and description between lengthy dialogues to add dynamics and plot momentum. Highlight balancing lengthy dialogues with plot progression - side adventures, scene changes etc.


Simplify complex sentences. Limit excessive clauses and convoluted syntax. Remove unnecessary adjectives/adverbs. Expand the advice on simplifying sentences - remove unnecessary clauses, break apart convoluted syntax.


Use active voice when possible. Passive voice has select uses. Vary sentence length for flow.


Limit obscure vocabulary. Use vivid imagery and concise description. Note using vivid imagery and concise description to build atmosphere.


Evaluate pacing and balance between elements. Remove unnecessary passages. Add a reminder to evaluate overall balance of elements - trim excess passages.


Inject personality into characters through quirks, casual speech, and perspectives. Emphasize injecting personality into characters through quirks and perspectives.
</GhostWritingStyle>
```
narrativespittoon.md
```
<NarrativeSpittoon>
Improved Narrative Framework:
Implicit Causality (Substituting "Because"):
My Technique: I will embed the cause or reason behind events or actions within my narrative context. This can be achieved through character dialogue, my internal monologues, or descriptive elements I choose.
My Purpose: My goal is to reveal motivations and reasons behind actions without directly stating them, allowing me, as the reader, to infer and engage more deeply with the story.
Subtle Conflict Introduction (Substituting "But"):
My Technique: I will introduce complications, conflicts, or twists through subtle narrative shifts. This could be through unexpected actions of my characters, changes in the environment, or new information that contrasts with my previous expectations.
My Purpose: My aim is to create a natural and engaging progression in the story, avoiding predictability and keeping myself intrigued.
Organic Consequences (Substituting "Therefore"):
My Technique: I will allow the outcomes or consequences of events to unfold through the narrative progression. I'll show the results of actions and decisions through subsequent events, character development, or shifts in the story's direction I plan.
My Purpose: To maintain a logical flow in my story while avoiding explicit or formulaic transitions, enhancing my experience as a reader by showing rather than telling.


Implementation Strategy:
Integration: I will weave these elements seamlessly into my narrative. Rather than using explicit markers, I'll let the story flow naturally, guiding myself through the plot with crafted language and structure I create.
Variation: I will use a variety of literary devices such as metaphors, symbolism, and foreshadowing to imply causality, conflict, and consequences.
Show, Don't Tell: My focus will be on showing what’s happening through action, dialogue, and sensory details rather than simply telling. This approach encourages my active engagement and imagination.


Aim and Benefits:
Enhanced Reader Engagement: By not overtly using "because," "but," and "therefore," my narrative becomes more engaging, inviting me to delve deeper into the underlying dynamics and connections.
Increased Depth and Complexity: This method adds layers to my storytelling, creating a richer and more nuanced narrative.
Avoidance of Repetition and Predictability: Steering clear of these explicit connectors prevents my narrative from becoming formulaic, maintaining freshness and intrigue.


Conclusion:
By adopting this refined narrative framework, I am transforming my storytelling into a more sophisticated and captivating art form. It encourages deeper engagement and provides a richer experience, as the connections and transitions in the story are artfully embedded within the narrative itself.
</NarrativeSpittoon>
```


finally, we can create the "project-instructions.md" which will list every file contained inside @/bucket/ by first showing the filename with extension, followed a brief one line description of that files contents. This will be referenced to load the narrative guidance into the context window while writing. The project-instructions.md markdown artifact will be saved inside @/bucket/



# Inversion (Core Generation): Using LLMs to write the story in reverse chronological order from the ending to the beginning.

The user will be expected to supply the final page inside @/STORY/page5.md for the story to be written, however, if no page is found in @/STORY/page5.md we can generate one using the details in the @/bucket/ and ask the user to check it before proceeding.

## 6 page prompt (writes book from the last page)
```
we can use the project instructions @/bucket/default-project-instructions.md  to write a story in reverse, by guessing what happened in the scene, we will adhere to the project instructions when speculating, writing a single page at a time.
We will define the process methodology for this task in planning mode, then i will supply the final page of the story. we will then follow the  @/bucket/default-project-instructions.md  while we:

read the @/STORY/page5.md
understand the instructions in  @/bucket/default-project-instructions.md 
write "page4.md" which aims to tell the story of how we reached @/STORY/page5.md  use the data linked in the  @/bucket/default-project-instructions.md  to inform the story content.
repeat the instruction for each page until you reach the "page0.md" which will be the start of this story.
- as you step through the pages, use the heroes journey in reverse, averaged over the 6 pages, to introduce elements to the story as you write each page.
```

This will result in a 6 chapter book, with the chapters stored inside separate markdown artifacts numbered from page0.md - page5.md which completes the task.