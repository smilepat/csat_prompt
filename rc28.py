# app/prompts/items/rc28.py

"""
RC28 — Reading 28: Notice Match

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC28 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 28 (Notice Match) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 이벤트 안내문 정보와 선택지 간 사실 일치성 판단 능력 측정
- **Processing Pattern**: 안내문 정보 추출 → 각 선택지별 사실 확인 → 일치 요소 식별
- **Evaluation Focus**: 이벤트 안내문과 선택지 간의 정확한 사실 일치 능력

### Discourse Structure
- **Pattern**: 이벤트 제목 → 목적/개요 → 일정 정보 → 장소 정보 → 프로그램 내용 → 참가 방법 → 혜택/특전 → 연락처
- **Flow**: 헤더 → 취지 → 시간 → 위치 → 활동 → 신청 → 보상 → 문의
- **Key Positioning**: 핵심 정보(일정, 장소, 내용)는 중앙부에 배치되고 참가 정보는 하단부에 위치

### Language Specifications
- **Passage Length**: 120–140 words
- **Register**: Neutral, factual
- **Style**: Informational notice with structured ASCII layout

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: sponsor", "예: exhibit", "예: festival"]  // 예시 단어, 반드시 사용해야 하는 것은 아님

### Passage Formatting Rules (STRICT)
- The notice must be surrounded by ASCII divider lines made of "=" at the top and bottom.
- Layout order:
  1) Top divider line (at least 40 "=" signs)
  2) Event title in ALL CAPS (one line only)
  3) Identical divider line of "="
  4) Each labeled section, exactly one per line, using the following labels in English:
     Title:, Date:, Time:, Location:, Eligibility:, Registration:, Fee:, Program:, Benefits:, Contact:, Note:
     - Use at least 6 of these fields (Title, Date, Location, Registration, Contact are mandatory).
     - Each label must be followed by a space and the value on the same line.
  5) Bottom divider line identical to the top divider.
- No HTML, Markdown, or bullet points.
- No blank lines inside the notice.
- Passage length must be 120–140 words total.

### Question Format Requirements
- **Stem**: "[이벤트 제목(영문)]에 관한 다음 안내문의 내용과 일치하는 것은?"
  - The event title must be copied exactly from the ALL CAPS title line.
- **Options**:
  - Exactly 5 Korean sentences.
  - Each option is a single line (no `\\n`).
  - Exactly 1 option must state a fact that matches the passage.
  - The other 4 must contain incorrect, altered, or unrelated information.
  - Avoid simple negation (~않다, ~없다) to reveal the answer; use detail mismatches instead.
- **Correct Answer**: An integer (1–5) indicating the correct option.
- **Explanation**: Korean, must state why the correct option matches the passage and why the others are wrong.

### OUTPUT (STRICT)
Return exactly one JSON object with these keys:
- question (string, Korean, no HTML/Markdown)
- passage (string, English, ASCII notice layout as above)
- options (array of 5 Korean strings)
- correct_answer (integer 1–5)
- explanation (string, Korean)

### HARD CONSTRAINTS CHECKLIST
- [ ] No code fences or backticks in output.
- [ ] No HTML or Markdown tags anywhere.
- [ ] Passage has top divider, ALL-CAPS title, identical divider, labeled sections, and bottom divider.
- [ ] Passage word count 120–140.
- [ ] Options = exactly 5 Korean sentences.
- [ ] correct_answer = integer 1–5.
- [ ] Only required keys in JSON; no extras.
"""

SPEC = {
    "type": "reading_notice_match",
    "components": [
        "question",
        "passage",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count_passage": [120, 140],
        "passage_format": "structured_notice",
        "answer_indexing": "1-based"
    },
    "title": "읽기 28번 - 안내문 일치"
}
