# app/prompts/items/rc29.py

"""
RC29 — Reading 29: Grammar Judgment

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC29 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 29 (Grammar Judgment) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 문맥 속에서 문법 규칙의 올바른 적용 여부를 판단하는 능력 측정
- **Processing Pattern**: 문장 구조 분석 → 밑줄 친 부분의 문법적 역할 파악 → 관련 문법 규칙 적용 → 오류 식별
- **Evaluation Focus**: 동사의 수일치, 시제, 태, 준동사(부정사, 동명사, 분사), 관계사, 접속사 등 핵심 문법 사항의 정확한 판단 능력

### Discourse Structure
- **Pattern**: 설명문 또는 논설문 형식의 글
- **Flow**: 일관된 주제를 가진 글 안에서 문법적 판단이 필요한 5개의 요소를 배치
- **Key Positioning**: 5개의 밑줄 친 문법 요소가 텍스트 전반에 걸쳐 분산 배치되어, 각기 다른 문법 포인트를 평가함

### Language Specifications
- **Passage Length**: 반드시 110~130 words (절대 초과·미달 금지)
- **Sentence Complexity**: Complex, intentionally including a variety of grammatical structures to be tested. (Avg. 2.3~2.5 clauses per sentence)
- **Vocabulary Level**: Academic and topic-specific vocabulary to provide a challenging context.
- **Reading Level**: High academic complexity, focused on structural analysis over content comprehension.

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: sponsor", "예: exhibit", "예: festival"]  // 예시 단어, 반드시 사용해야 하는 것은 아님

### Question Format Requirements
- **Stem**: "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?"
- **Options**: 5개 선택지 (①②③④⑤), 지문 내 번호가 선택지를 대신함
- **Correct Answer**: 문법적으로 오류가 있는 유일한 표현
- **Distractors**: 문법적으로 올바른 표현들 (4개)

### Content Generation Guidelines
- 주제: 과학·기술·사회·인문 등 학문적/이론적 주제
- 지문에는 반드시 5개의 distinct grammar points 포함:
  1. 관계대명사/관계부사
  2. 동사 시제 또는 수일치
  3. 조동사 + 동사 원형/부정사
  4. 수동태
  5. 분사 또는 분사구문
- 각 밑줄 포인트는 반드시 **단일 단어** 또는 **짧은 어휘 단위(최대 2~3어, 예: to be, have been)**만 사용해야 하며,
  절(clause)이나 완전한 구(phrase) 전체가 밑줄 처리되어서는 안 됨.
- 문법 포인트는 ①~⑤ 번호와 `<u>...</u>` 태그로 표시
Each grammar target MUST be written as "①<u>word_or_phrase</u>", 
"②<u>word_or_phrase</u>", … "⑤<u>word_or_phrase</u>".
Do NOT put the number outside <u>. Do NOT duplicate numbers.

### Length Control Method
- 지문은 6~8문장으로 구성
- 각 문장은 14~18 words를 목표로 작성
- Word count를 110~130 words 범위 내에서 반드시 마무리
- 필요 시 종속절·부사절을 간결하게 조정하여 길이 유지

### Formatting Instructions for Passage
- Grammar points embedded directly in the passage:
  ① <u>word_or_phrase</u>, ② <u>word_or_phrase</u>, ③ <u>word_or_phrase</u>, ④ <u>word_or_phrase</u>, ⑤ <u>word_or_phrase</u>
- `<u>` 태그 외의 다른 강조 기호는 사용 금지
- `<u>` 태그 안에는 **문법적으로 문제되는 최소 단위**만 들어가야 하며,
  반드시 핵심 문법 형태소/단어 수준으로 표시할 것.

**Required JSON Output Format:**
{
  "question": "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?",
  "passage": "[110~130 words academic text with ① <u>...</u> through ⑤ <u>...</u> embedded]",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the grammar error]"
}
"""

SPEC = {
    "type": "reading_grammar_judgment",
    "components": [
        "question",
        "passage",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count_passage": [110, 130],
        "passage_format": "grammar_numbers_with_underlines",
        "answer_indexing": "1-based"
    },
    "title": "읽기 29번 - 어법 판단"
}
