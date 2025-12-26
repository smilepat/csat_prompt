# app/prompts/items/lc11.py

"""
LC11 — Listening 11: Short Response Inference

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 LC11 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Listening Item 11 (Short Response Inference) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Inferring appropriate responses to final statements in short dialogues
- **Cognitive Process**: Follow dialogue context → Analyze final statement → Select logical response
- **Difficulty Level**: Advanced contextual inference requiring pragmatic understanding

### Discourse Type & Structure
- **Format**: Brief two-person dialogue (2-3 exchanges)
- **Structure Pattern**: Situation setup → Problem/request → Final statement requiring response
- **Content Flexibility**: Any everyday situation requiring immediate, contextually appropriate responses
- **Interaction Type**: Problem-solving, request-response, or social interaction

### Language Specifications
- **Transcript Length**: 60-80 words (approximately 30-40 seconds)
- **Sentence Complexity**: Simple to moderate with clear contextual cues
- **Vocabulary Level**: Everyday conversational vocabulary
- **Speech Rate**: Natural conversational pace

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: permit", "예: schedule"]

### Formatting Instructions for Transcript
- 대화문은 M: (남자 화자), W: (여자 화자) 표기를 사용한다.
- 남자가 먼저 말하고, 여자가 마지막에 말하며, 그 마지막 발화가 문제에서 응답해야 하는 대상이 된다.
- 대화는 2~3턴으로 구성하되, 마지막 발화는 반드시 여자의 대사로 끝난다.

### Question Format Requirements
- **Stem**: "대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오. [3점]"
- **Options**: 5 English response options
- **Correct Answer**: Must be the most contextually appropriate and natural response
- **Distractors**: Contextually inappropriate, logically inconsistent, or socially awkward responses

### Content Generation Guidelines
- Create realistic everyday scenarios requiring immediate responses
- Ensure the final statement clearly sets up the need for a specific type of response
- Include contexts familiar to Korean students (daily life, services, social situations)
- Use natural conversational patterns and appropriate social registers

**Required JSON Output Format:**
{
  "question": "대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오. [3점]",
  "transcript": "[60-80 word short dialogue with M:/W: indicators]",
  "options": ["Response 1", "Response 2", "Response 3", "Response 4", "Response 5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of why the response is appropriate]"
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
        "word_count": [60, 80],
        "duration_seconds": [30, 40],
        "response_inference": True
    },
    "title": "듣기 11번 - 짧은 대화 응답"
}
