# app/prompts/items/lc12.py

"""
LC12 — Listening 12: Short Response Inference

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 LC12 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Listening Item 12 (Short Response Inference) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Inferring appropriate responses to final statements in short dialogues
- **Cognitive Process**: Follow dialogue context → Analyze final statement → Select logical response
- **Difficulty Level**: Intermediate contextual inference with clear response patterns

### Discourse Type & Structure
- **Format**: Brief two-person dialogue (2-3 exchanges)
- **Structure Pattern**: Proposal → Concern expression → Reassurance → Response needed
- **Content Flexibility**: Any situation involving initial hesitation followed by reassurance
- **Interaction Type**: Invitation acceptance after concern resolution

### Language Specifications
- **Transcript Length**: 50-70 words (approximately 25-35 seconds)
- **Sentence Complexity**: Simple with clear reassurance patterns
- **Vocabulary Level**: Basic conversational vocabulary
- **Speech Rate**: Natural conversational pace

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: permit", "예: schedule"]

### Question Format Requirements
- **Stem**: "대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오."
- **Options**: 5 English response options
- **Correct Answer**: Must show acceptance after reassurance, as the man's response to the final W: line
- **Distractors**: Continued hesitation, irrelevant responses, inappropriate reactions

### Transcript Formatting Instructions
- 대화문은 W: (여자 화자), M: (남자 화자) 표기를 사용한다.
- 여자가 먼저 말하고, 남자가 마지막에 말하며, 그 마지막 발화가 문제에서 응답해야 하는 대상이 된다.
- 대화는 2~3턴으로 구성하되, 마지막 발화는 반드시 남자의 대사로 끝난다.
- 대화문 표기는 W: (여자), M: (남자)를 사용한다.
- 여자가 먼저 말하고, 마지막 발화도 반드시 여자의 대사(W:)로 끝난다.
- 남자의 응답은 transcript에 포함하지 않으며, 보기가 남자의 응답 후보가 된다.
- (검증) transcript의 마지막 줄은 반드시 `W:`로 시작해야 한다.

### Content Generation Guidelines
- Create scenarios where initial concerns are addressed and resolved
- Ensure the final statement provides clear reassurance
- Include contexts involving activities, programs, or invitations
- Use clear concern-resolution patterns

**Required JSON Output Format:**
{
  "question": "대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오.",
  "transcript": "[50-70 word dialogue with W:/M: indicators; ends with a W: line; the man's response is NOT included]",
  "options": ["Response 1", "Response 2", "Response 3", "Response 4", "Response 5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the response logic]"
}
"""

SPEC = {
    "type": "listening_short_response",
    "components": [
        "question",
        "transcript",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "transcript_format": "speaker_separation",
        "word_count": [50, 70],
        "duration_seconds": [25, 35],
        "response_inference": True,
        "ends_with": "W:"
    },
    "title": "듣기 12번 - 짧은 대화 응답"
}
