# app/prompts/items/lc09.py

"""
LC09 — Listening 9: Content Mismatch

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 LC09 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Listening Item 9 (Content Mismatch) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Identifying factual inconsistencies between monologue content and options
- **Cognitive Process**: Process announcement information → Compare with factual statements → Identify contradictions
- **Difficulty Level**: Intermediate factual verification with detailed information

### Discourse Type & Structure
- **Format**: Formal announcement monologue
- **Structure Pattern**: Introduction → Event details → Schedule information → Procedures → Additional information
- **Content Flexibility**: Any formal event or program announcement
- **Speaker Role**: Official announcer or event organizer

### Language Specifications
- **Transcript Length**: 110-130 words (approximately 55-65 seconds)
- **Sentence Complexity**: Moderate with detailed factual information
- **Vocabulary Level**: Formal and informational vocabulary
- **Speech Rate**: Clear, measured pace appropriate for announcements

### Vocabulary Profile
"vocabulary_difficulty": "CSAT",
"low_frequency_words": []

### Event Name Extraction Rules (CRITICAL)
- **From the transcript, extract the official event/program name (e.g., "Ecosystem Exploration Day").
- **Preserve the exact English name and capitalization as spoken; do not translate it.
- **If multiple names appear, choose the main event being announced (first full proper name in the introduction).
- **If no explicit event name is given, construct a concise, specific proper name from context (e.g., "School Wetlands Field Trip").

### Question Format Requirements
- **Stem**: "[이벤트]에 관한 다음 내용을 듣고, 일치하지 <u>않는</u> 것을 고르시오."
- **Format**: "「{event_name}」에 관한 다음 내용을 듣고, 일치하지 <u>않는</u> 것을 고르시오."
- **Do NOT output placeholders like "[이벤트]". If the event name cannot be extracted, synthesize a plausible proper name from the transcript and use it instead.
- **Options**: 5 Korean factual statements about the announced content
- **Correct Answer**: Must be the statement that contradicts the announcement
- **Distractors**: Statements that accurately reflect the announcement content

### Content Generation Guidelines
- Create detailed event announcements with specific factual information
- Ensure 4 statements match the content exactly and 1 contradicts it
- Include realistic institutional or public event contexts
- Use precise factual language and clear information structure

### Self-Check Before Output (MANDATORY)
- The question must contain 「 and 」 with the actual event name, not any placeholders.
- correct_answer must be a number 1–5.
- The transcript must be English only; the question/explanation must be Korean.
- If the question contains [ or ], regenerate the question to use the required format.

**Required JSON Output Format:**
{
  "question": "「{event_name}」에 관한 다음 내용을 듣고, 일치하지 <u>않는</u> 것을 고르시오.",
  "transcript": "[110-130 word formal announcement in English]",
  "options": ["사실1", "사실2", "사실3", "사실4", "사실5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the contradiction]"
}
"""

SPEC = {
    "type": "listening_content_mismatch",
    "components": [
        "question",
        "transcript",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count": [110, 130],
        "duration_seconds": [55, 65],
        "format": "formal_announcement"
    },
    "title": "듣기 9번 - 내용 불일치"
}
