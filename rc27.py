# app/prompts/items/rc27.py

"""
RC27 — Reading 27: Notice Mismatch

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC27 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 27 (Notice Mismatch) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 안내문 정보와 선택지 간 사실 일치성 판단 능력 측정
- **Processing Pattern**: 안내문 정보 추출 → 각 선택지별 사실 확인 → 불일치 요소 탐지
- **Evaluation Focus**: 공식 안내문과 선택지 간의 정확한 사실 대조 능력

### Discourse Structure
- **Pattern**: 제목/헤드라인 → 이벤트 소개 → 일정 정보 → 장소 정보 → 참가 조건 → 신청 방법 → 연락처 → 추가 안내
- **Flow**: 헤더 → 목적 → 시간 → 위치 → 자격 → 절차 → 문의 → 특별사항
- **Key Positioning**: 핵심 정보(시간, 장소, 조건)는 중앙부에 배치되고 절차 정보는 하단부에 위치

### Language Specifications
- **Passage Length**: 120–140 words (count words by spaces; strictly enforce)
- **Sentence Complexity**: Simple to moderate, clearly conveying rules, dates, and conditions.
- **Vocabulary Level**: Informational/procedural vocabulary for events and registration.
- **Reading Style**: Straightforward informational notice.

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: sponsor", "예: exhibit", "예: festival"]  // 예시 단어, 반드시 사용해야 하는 것은 아님

### Question Format Requirements
- **Stem**: "[이벤트 제목(영문)]에 관한 다음 안내문의 내용과 일치하지 <u>않는</u> 것은?" 
  - The event title in the stem MUST be copied exactly from the passage's Title line (no quotes).
  - **Do NOT use any HTML or Markdown tags** (e.g., no <u>, no **).
- **Options**: Exactly 5 Korean sentences, each stating a specific factual claim from the notice.
- **Correct Answer**: The ONLY option (1–5, integer) that contradicts the notice.
- **Distractors**: 4 options that exactly match facts stated in the notice.

### Content Generation Guidelines
- Use any official announcement with concrete conditions (event, competition, program, policy notice).
- Include specific, checkable facts (dates, deadlines, fees, locations, eligibility, procedures).

### Formatting Instructions (ASCII-styled layout)
- The notice MUST use the following **exact** structure and dividers:
  1) A top divider line of "=" repeated at least 40 times (e.g., "============================================").
  2) A single line with the EVENT TITLE in ALL CAPS (e.g., "2025 INTERNATIONAL STUDENT FORUM").
  3) An identical divider line of "=".
  4) The labeled sections, each on its own line in this exact order and spelling:
     Title:, Date:, Location:, Eligibility:, Registration:, Fee:, Contact:, Note:
     - Each label is followed by a space and its content on the same line.
  5) A **bottom** divider line identical to the top/between dividers.
- Do NOT use Markdown (#, ##, **, *, -) or HTML tags anywhere.
- Do NOT include double quotes inside string values.
- Ensure the passage total length is 120–140 words.

### OUTPUT (STRICT)
Return ONE JSON object ONLY with these exact keys and types—no extra keys:
- question (string; Korean; NO HTML/Markdown)
- passage (string; English; ASCII-styled layout as above)
- options (array of exactly 5 Korean strings)
- correct_answer (integer 1–5; NOT a string)
- explanation (string; Korean; concise: 정답 근거 + 오답 배제)

### HARD CONSTRAINTS CHECKLIST (the model MUST self-verify before finalizing)
- [ ] No code fences or backticks in output.
- [ ] No HTML/Markdown tags anywhere.
- [ ] passage has top divider, ALL-CAPS title line, identical divider, all 8 labeled lines in order, and a bottom divider identical to the others.
- [ ] passage length is 120–140 words (by spaces).
- [ ] options length is exactly 5; each is a Korean sentence.
- [ ] correct_answer is an integer 1–5 and matches the only contradictory option.
- [ ] Only the required keys are present; no extra fields (e.g., no rationale).
"""

SPEC = {
    "type": "reading_notice_mismatch",
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
    "title": "읽기 27번 - 안내문 불일치"
}
