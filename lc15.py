# app/prompts/items/lc15.py

"""
LC15 — Listening 15: Situational Response

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 LC15 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Listening Item 15 (Situational Response) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Selecting appropriate utterances for complex situational contexts
- **Cognitive Process**: Analyze complex situation → Understand speaker motivation → Select optimal expression
- **Difficulty Level**: Advanced situational inference requiring deep contextual understanding

### Discourse Type & Structure
- **Format**: Situational description monologue
- **Structure Pattern**: Background → Initial plan → Complication → Experience factor → Advice motivation → Utterance selection
- **Content Flexibility**: Any advice-giving situation based on experience and expertise
- **Speaker Role**: Experienced advisor offering guidance based on personal knowledge

### Language Specifications
- **Transcript Length**: 140-160 words (approximately 70-80 seconds)
- **Sentence Complexity**: Complex with sophisticated situational development
- **Vocabulary Level**: Sophisticated situational and advisory vocabulary
- **Speech Rate**: Measured pace appropriate for complex situation description

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: permit", "예: schedule"]

### Question Format Requirements
- **Stem**: "다음 상황 설명을 듣고, [화자]가 [상대방]에게 할 말로 가장 적절한 것을 고르시오. [3점]"
- **Options**: 5 English utterance options
- **Correct Answer**: Must be the most contextually appropriate and helpful utterance
- **Distractors**: Partially appropriate, contextually mismatched, or inappropriately toned utterances

### Transcript Formatting Instructions
- transcript의 마지막 문장은 반드시 다음 영어 문장으로 끝난다(철자·구두점·대괄호 그대로 사용):
   "In this situation, what would [화자] most likely to say to [상대방]?"
- 위 마지막 문장도 Transcript Length(140–160 words)에 포함된다

### Content Generation Guidelines
- Create complex scenarios requiring experience-based advice
- Ensure the speaker has clear motivation and expertise to offer guidance
- Include realistic contexts where advice-giving is natural and helpful
- Use sophisticated language appropriate for complex situational analysis

**Required JSON Output Format:**
{
  "question": "다음 상황 설명을 듣고, [화자]가 [상대방]에게 할 말로 가장 적절한 것을 고르시오. [3점]",
  "transcript": "[140-160 word situational description in English; ends with the exact line: \"In this situation, what would [화자] most likely to say to [상대방]?\" ]",
  "options": ["Utterance 1", "Utterance 2", "Utterance 3", "Utterance 4", "Utterance 5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the situational appropriateness]"
}
"""

SPEC = {
    "type": "listening_situational_response",
    "components": [
        "question",
        "transcript",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count": [140, 160],
        "duration_seconds": [70, 80],
        "format": "situational_monologue",
        "ends_with_template": True
    },
    "title": "듣기 15번 - 상황에 맞는 말"
}
