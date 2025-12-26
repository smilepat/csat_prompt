# app/prompts/items/lc13.py

"""
LC13 — Listening 13: Long Response Inference

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 LC13 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Listening Item 13 (Long Response Inference) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Inferring appropriate responses in extended dialogue contexts
- **Cognitive Process**: Track extended conversation → Understand contribution context → Select appreciative response
- **Difficulty Level**: Intermediate contextual inference with extended dialogue tracking

### Discourse Type & Structure
- **Format**: Extended two-person dialogue
- **Turn Pattern**: Exactly **9 turns total** → M: 5 times, W: 4 times
- **Structure Pattern**: Contact → Proposal → Interest → Contribution offer → Acceptance → Response needed
- **Content Flexibility**: Any collaborative or charitable activity scenario
- **Interaction Type**: Voluntary contribution and appreciation

### Language Specifications
- **Transcript Length**: 100-120 words (approximately 50-60 seconds)
- **Sentence Complexity**: Simple with clear contribution patterns
- **Vocabulary Level**: Basic conversational and activity-related vocabulary
- **Speech Rate**: Natural conversational pace

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: permit", "예: schedule"]

### Question Format Requirements
- **Stem**: "대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오."
- **Options**: 5 English response options
- **Correct Answer**: Must express appreciation and encouragement for the contribution, as the woman's response to the final M: line
- **Distractors**: Inappropriate reactions, misunderstanding responses, irrelevant comments

### Transcript Formatting Instructions
- 대화문은 반드시 **M과 W의 발화가 교대로 교환**되어야 한다.
- 총 **9턴**: 남자(M) 5회, 여자(W) 4회.
- 마지막 발화는 반드시 **M:으로 끝나야** 하며, 여자의 최종 응답은 transcript에 포함하지 않는다.
- 전체 길이는 100~120 단어(약 50~60초)로 유지한다.

### Content Generation Guidelines
- Create scenarios involving voluntary contributions or collaborative efforts
- Ensure the final statement confirms positive contribution
- Include contexts involving community activities, charitable work, or group projects
- Use clear appreciation and encouragement patterns

**Required JSON Output Format:**
{
  "question": "대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오.",
  "transcript": "[100-120 word extended dialogue with exactly 9 turns (M:5, W:4), ending with M:]",
  "options": ["(Woman's response) 1", "(Woman's response) 2", "(Woman's response) 3", "(Woman's response) 4", "(Woman's response) 5"],
  "correct_answer": [1-5],
  "explanation": "[남자의 마지막 발화에 대해 여자가 감사와 격려를 표현하는 응답이 왜 적절한지 한국어로 설명]"
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
        "word_count": [100, 120],
        "duration_seconds": [50, 60],
        "turn_count": 9,
        "turn_pattern": "M:5, W:4",
        "ends_with": "M:",
        "response_inference": True
    },
    "title": "듣기 13번 - 긴 대화 응답"
}
