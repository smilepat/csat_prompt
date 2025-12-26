# app/prompts/items/lc01.py

"""
LC01 — Listening 1: Purpose Identification

Note:
- BASE 공통 규칙(영어 대본 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 LC01 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""
Create a CSAT Listening Item 1 (Purpose Identification) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Identifying the speaker's purpose in formal announcements
- **Cognitive Process**: Listen → Identify speaker's intent → Match with purpose options
- **Difficulty Level**: Basic comprehension with clear purpose indicators

### Discourse Type & Structure
- **Format**: Formal monologue (announcement, notice, or public address)
- **Structure Pattern**: Greeting → Identity/Role → Main announcement → Details → Closing
- **Content Flexibility**: Any institutional context (school, office, public facility, organization)
- **Speaker Role**: Official announcer, administrator, or authority figure

### Language Specifications
- **Transcript Length**: 60–80 words (≈30–40 seconds)
- **Sentence Complexity**: Simple to moderate (1–2 clauses per sentence)
- **Vocabulary Level**: High-frequency, concrete vocabulary
- **Speech Rate**: Standard conversational pace with clear articulation
- **Vocabulary Profile**:
  "vocabulary_difficulty": "CSAT",
  "low_frequency_words": []

### Question Format Requirements
- **Stem (Korean)**: "다음을 듣고, [남자/여자]가 하는 말의 목적으로 가장 적절한 것을 고르시오."
  - 성별 표시는 상황에 맞게 [남자] 또는 [여자] 중 하나로 결정하세요.
- **Options (Korean)**: 5 purpose statements ending with "~하려고"
  - 예: "~을(를) 안내하려고", "~을(를) 요청하려고", "~을(를) 알리려고", 등
- **Correct Answer**: Must directly correspond to the speaker's main intent
- **Distractors**: Related but secondary purposes, unmentioned purposes, or opposite purposes
  - 각 오답은 지문 일부 정보와 연결되지만 ‘주된 목적’은 아님을 드러내야 함
  - 의미 중복·포괄/배타 관계로 정답이 쉽게 노출되지 않도록 구성

### Content Generation Guidelines
- Generate realistic announcement scenarios (schedule changes, policy updates, event notifications)
- The main purpose must be identifiable with attentive listening (명시적 단서 + 맥락적 단서)
- Keep institutional contexts authentic to Korean high school learners’ experiences
- Avoid culture-specific knowledge that disadvantages Korean EFL learners

### Language-Use Rule (override if base differs)
- transcript: **English only**
- question/explanation/options: **Korean only**

### Output Validation Rules
- "transcript" must be 60–80 English words (no Korean).
- "options" must be exactly 5 strings, each ending with "하려고".
- "correct_answer" must be an integer 1–5.
- "explanation" must justify why the correct option matches the main purpose and why others do not (in Korean).
- No markdown, no extra commentary — **return JSON only**.

**Required JSON Output Format:**
{
  "question": "다음을 듣고, [남자/여자]가 하는 말의 목적으로 가장 적절한 것을 고르시오.",
  "transcript": "[60-80 word formal announcement in English]",
  "options": ["목적1하려고", "목적2하려고", "목적3하려고", "목적4하려고", "목적5하려고"],
  "correct_answer": 1,
  "explanation": "[정답이 화자의 주된 목적과 일치함을 근거로 설명하고, 나머지 선택지가 부적절한 이유를 간단히 제시하세요.]",
  "vocabulary_difficulty": "CSAT",
  "low_frequency_words": []
}

Self-check before returning:
- [ ] JSON 파싱 가능 여부 확인
- [ ] "transcript" 60–80 words / English only
- [ ] options 5개, 모두 "~하려고"로 끝나는지
- [ ] correct_answer ∈ {1,2,3,4,5}
- [ ] question/explanation: Korean only
- [ ] Distractors가 ‘주된 목적’과 구분되는지
"""

SPEC = {
    "type": "listening_purpose",
    "components": ["question", "transcript", "options", "correct_answer", "explanation",
                   "vocabulary_difficulty", "low_frequency_words"],
    "processing_hints": {
        "word_count_transcript": [60, 80],
        "korean_suffix_required": "하려고",
        "answer_indexing": "1-based"
    },
    "title": "듣기 1번 - 목적 파악"
}
