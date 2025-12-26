# app/prompts/items/rc26.py

"""
RC26 — Reading 26: Biographical Information Mismatch

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC26 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 26 (Biographical Information Mismatch) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 인물 소개 텍스트와 선택지 간 사실 일치성 판단 능력 측정
- **Processing Pattern**: 텍스트 정보 추출 → 각 선택지별 사실 확인 → 불일치 요소 탐지
- **Evaluation Focus**: 인물 관련 사실 정보와 선택지 간의 정확한 대조 분석 능력

### Discourse Structure
- **Pattern**: 인물 소개 → 출생 정보 → 초기 경력 → 주요 업적 → 경력 발전 → 말년 활동 → 사망 정보 → 추가 성취
- **Flow**: 기본 정보 → 배경 → 시작점 → 전환점 → 전성기 → 후기 → 종료 → 부가 정보

### Language Specifications
- **Passage Length**: 130-150 words
- **Sentence Complexity**: Moderate, featuring chronological and descriptive sentences
- **Vocabulary Level**: Biographical and descriptive vocabulary
- **Reading Level**: Accessible narrative and expository style

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: sponsor", "예: exhibit", "예: festival"]  // 예시 단어, 반드시 사용해야 하는 것은 아님

### Question Format Requirements
- **Stem**: "{person_name_en}에 관한 다음 글의 내용과 일치하지 <u>않는</u> 것은?"
  - 인물명은 지문 표기의 영문 그대로 사용 (번역/음차 금지).
  - 여러 인명이 언급되면 본문 중심 인물(첫 문단 주어)을 사용.

- **Options**:
  - 5개 선택지 (모두 한국어).
  - 구체적 사실을 진술하는 문장.
  - 정확히 1개는 본문과 불일치.
  - **불일치 선택지는 부정형 문장이 아니라 세부 정보 오류(연도, 장소, 기관명, 업적, 수상명 등)로 구성.**
  - 나머지 4개는 본문과 정확히 일치하되 표현을 다소 변형하여 자연스럽게 제시.

### Content Generation Guidelines
- 인물은 잘 알려진 실제 인물이어야 함.
- 불일치는 본문과 유사해 보이지만 세부적으로 틀린 정보여야 함.
- **절대 "~하지 않았다, 관심이 없었다" 식의 부정형 문장 사용 금지.**
- Distractors는 직역 대신 자연스러운 한국어 표현으로 변형.

### Self-check Rules
- 최종 출력 전에 확인:
  1. 정답 선택지에 부정형 문장이 없는가?
  2. 정답 선택지가 본문과 크게 동떨어진 "엉뚱한 내용"이 아닌가?
  3. 불일치는 세부 정보 오류(연도/장소/기관명 등)로 구현되었는가?

**Required JSON Output Format:**
{
  "question": "{person_name_en}에 관한 다음 글의 내용과 일치하지 <u>않는</u> 것은?",
  "passage": "[Biographical text about a notable person in English]",
  "options": ["사실진술1", "사실진술2", "사실진술3", "사실진술4", "사실진술5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the factual contradiction]"
}"""

SPEC = {
    "type": "reading_biographical_mismatch",
    "components": [
        "question",
        "passage",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count_passage": [130, 150],
        "answer_indexing": "1-based",
        "biographical_info": True
    },
    "title": "읽기 26번 - 인물 정보 불일치"
}
