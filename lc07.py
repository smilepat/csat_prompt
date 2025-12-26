# app/prompts/items/lc07.py

"""
LC07 — Listening 7: Reason Identification

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 LC07 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Listening Item 7 (Reason Identification) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Identifying specific reasons for inability to participate in events
- **Cognitive Process**: Track invitation → Identify refusal → Extract actual reason from multiple possibilities
- **Difficulty Level**: Intermediate comprehension requiring reason discrimination

### Discourse Type & Structure
- **Format**: Two-person dialogue about event participation
- **Structure Pattern**: Invitation/suggestion → Interest but inability → Reason exploration → Actual reason revelation
- **Content Flexibility**: Any social event or activity invitation scenario
- **Interaction Type**: Social invitation and polite refusal with explanation

### Language Specifications
- **Transcript Length**: 90-110 words (approximately 45-55 seconds)
- **Sentence Complexity**: Moderate with causal expressions and explanations
- **Vocabulary Level**: Social and explanatory vocabulary
- **Speech Rate**: Natural conversational pace with clear reason indicators

### Vocabulary Profile
"vocabulary_difficulty": "CSAT",
"low_frequency_words": []

### Question Format Requirements
- **Stem**: "대화를 듣고, [남자/여자]가 [이벤트]에 갈 수 <u>없는</u> 이유를 고르시오."
- **Options**: 5 Korean reason statements using causal expressions
- **Correct Answer**: Must be the actual reason explicitly stated by the speaker
- **Distractors**: Suggested but rejected reasons, related but incorrect reasons, opposite situations

### Content Generation Guidelines
- Create realistic social invitation scenarios
- Include multiple potential reasons but make one clearly correct
- Ensure the actual reason is explicitly stated, not just implied
- Use contexts relevant to Korean student social life

**Required JSON Output Format:**
{
  "question": "대화를 듣고, [남자/여자]가 [이벤트]에 갈 수 <u>없는</u> 이유를 고르시오.",
  "transcript": "[90-110 word invitation dialogue with M:/W: indicators]",
  "options": ["이유1때문에", "이유2해야 해서", "이유3때문에", "이유4해야 해서", "이유5때문에"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the reason]"
}
"""

SPEC = {
    "type": "listening_reason_identification",
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
    "title": "듣기 7번 - 이유 파악"
}
