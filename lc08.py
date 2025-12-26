# app/prompts/items/lc08.py

"""
LC08 — Listening 8: Not Mentioned Information

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 LC08 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Listening Item 8 (Not Mentioned) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Identifying information not mentioned in event-related dialogue
- **Cognitive Process**: Track mentioned information → Compare with options → Identify omissions
- **Difficulty Level**: Intermediate information tracking with systematic checking

### Discourse Type & Structure
- **Format**: Two-person dialogue about event information
- **Structure Pattern**: Event discovery → Information gathering → Detail confirmation → Additional inquiries
- **Content Flexibility**: Any event, program, or activity with multiple informational aspects
- **Interaction Type**: Information exchange and inquiry

### Language Specifications
- **Transcript Length**: 90-110 words (approximately 45-55 seconds)
- **Sentence Complexity**: Moderate with information-dense content
- **Vocabulary Level**: Informational and descriptive vocabulary
- **Speech Rate**: Natural pace with clear information delivery

### Vocabulary Profile
"vocabulary_difficulty": "CSAT",
"low_frequency_words": []

### Question Format Requirements
- **Stem**: "대화를 듣고, [Event/Program/Activity in English]에 관해 언급되지 <u>않은</u> 것을 고르시오."
- **Options**: 5 Korean information categories related to the topic
- **Correct Answer**: Must be the information category not mentioned in the dialogue
- **Distractors**: Information categories explicitly mentioned in the dialogue

### Content Generation Guidelines
- Create information-rich dialogues about events or programs
- Ensure 4 information categories are clearly mentioned and 1 is omitted
- Include realistic event contexts with typical information needs
- Use systematic information patterns familiar to Korean students

**Required JSON Output Format:**
{
  "question": "대화를 듣고, [Event/Program/Activity in English]에 관해 언급되지 <u>않은</u> 것을 고르시오.",
  "transcript": "[90-110 word information dialogue with M:/W: indicators]",
  "options": ["정보항목1", "정보항목2", "정보항목3", "정보항목4", "정보항목5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of what was not mentioned]"
}
"""

SPEC = {
    "type": "listening_not_mentioned",
    "components": [
        "question",
        "transcript",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "transcript_format": "speaker_separation",
        "word_count": [90, 110],
        "duration_seconds": [45, 55]
    },
    "title": "듣기 8번 - 언급되지 않은 것"
}
