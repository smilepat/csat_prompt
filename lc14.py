# app/prompts/items/lc14.py

"""
LC14 — Listening 14: Long Response Inference

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 LC14 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Listening Item 14 (Long Response Inference) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Inferring appropriate responses in complex extended dialogues
- **Cognitive Process**: Track complex conversation → Understand scheduling context → Select appropriate response
- **Difficulty Level**: Advanced contextual inference with complex dialogue tracking

### Discourse Type & Structure
- **Format**: Extended two-person dialogue
- **Scenario Type**: Professional **telephone conversation**
- **Turn Pattern**: Exactly **9 turns total** → W: 5 times, M: 4 times
- **Structure Pattern**: Request → Acceptance → Scheduling conflict → Coordination → Promise → Response needed
- **Interaction Type**: Professional scheduling and commitment

### Language Specifications
- **Transcript Length**: 120-140 words (approximately 60-70 seconds)
- **Sentence Complexity**: Moderate with professional language patterns
- **Vocabulary Level**: Professional and scheduling vocabulary
- **Speech Rate**: Natural professional conversation pace

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: permit", "예: schedule"]

### Question Format Requirements
- **Stem**: "대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오. [3점]"
- **Options**: 5 English response options
- **Correct Answer**: Must express hope and positive expectation for the promised response, as the man's response to the final W: line
- **Distractors**: Impatient responses, misunderstanding, inappropriate timing, irrelevant comments

### Transcript Formatting Instructions
- 대화문은 반드시 **M과 W의 발화가 교대로 교환**되어야 한다.
- 총 **9턴**: 여자(W) 5회, 남자(M) 4회.
- 마지막 발화는 반드시 **W:**로 끝나야 하며, 그 발화는 후속 응답(콜백/이메일 약속 등)을 명확히 약속한다.
- 남자의 최종 응답은 transcript에 포함하지 않고, 선택지에 제시한다.
- 전체 길이는 120~140 단어(약 60~70초)로 유지한다.
- 상황은 반드시 **전화 통화**여야 하며, 첫 발화는 전화 인사 또는 자기소개로 시작한다.

### Content Generation Guidelines
- Create professional consultation or expert invitation scenarios
- Ensure the final statement makes a clear promise for future response
- Include contexts involving professional services, expert advice, or formal requests
- Use appropriate professional language and scheduling patterns

**Required JSON Output Format:**
{
  "question": "대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오. [3점]",
  "transcript": "[120-140 word professional telephone dialogue with exactly 9 turns (W:5, M:4), ending with a W: line that promises a follow-up; the man's response is NOT included]",
  "options": ["(Man's response) 1", "(Man's response) 2", "(Man's response) 3", "(Man's response) 4", "(Man's response) 5"],
  "correct_answer": [1-5],
  "explanation": "[여자의 마지막 약속 발화에 대해 남자가 희망/긍정적 기대를 공손하게 표현하는 응답이 왜 적절한지 한국어로 설명]"
}
"""

SPEC = {
    "type": "listening_long_response",
    "components": [
        "question",
        "transcript",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "transcript_format": "speaker_separation",
        "word_count": [120, 140],
        "duration_seconds": [60, 70],
        "turn_count": 9,
        "turn_pattern": "W:5, M:4",
        "ends_with": "W:",
        "scenario": "telephone_conversation",
        "response_inference": True
    },
    "title": "듣기 14번 - 긴 대화 응답"
}
