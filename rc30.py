# app/prompts/items/rc30.py

"""
RC30 — Reading 30: Vocabulary Appropriateness Judgment

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC30 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 30 (Vocabulary Judgment) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 글의 전체적인 논리 흐름 속에서 어휘의 문맥적 적절성을 판단하는 능력 측정
- **Processing Pattern**: 글의 주제와 문장 간 논리 관계 파악 → 밑줄 친 어휘의 의미와 문맥의 요구사항 비교 → 의미적으로 상충되는 어휘 식별
- **Evaluation Focus**: 반의어 관계, 인과관계, 논리적 모순 등을 통해 문맥상 부적절한 어휘를 정확히 찾아내는 능력

### Discourse Structure
- **Pattern**: 설명문 또는 논설문 형식의 글
- **Flow**: 일관된 주제와 논리적 흐름을 가진 글 안에서, 문맥상 판단이 필요한 5개의 어휘를 배치
- **Key Positioning**: 5개의 밑줄 친 어휘가 텍스트 전반에 걸쳐 분산 배치되며, 주로 논리적 전환점이나 핵심 개념어에 위치함

### Language Specifications
- **Passage Length**: 130-150 words
- **Sentence Complexity**: Complex, with dense logical relationships (e.g., cause-effect, contrast) to support inference. (Avg. 2.1-2.3 clauses per sentence)
- **Vocabulary Level**: Advanced academic and abstract vocabulary.
- **Reading Level**: High academic complexity, focused on logical inference.

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: sponsor", "예: exhibit", "예: festival"]  // 예시 단어, 반드시 사용해야 하는 것은 아님

### Question Format Requirements
- **Stem**: "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]"
- **Options**: 5개 선택지 (①②③④⑤), 지문 내 번호가 선택지를 대신함
- **Correct Answer**: 글의 전체적인 논리 흐름과 상충되는 유일한 어휘
- **Distractors**: 문맥상 의미가 적절하며 글의 논리를 지지하는 어휘들 (4개)

### Content Generation Guidelines
- Any academic or explanatory topic with a clear logical flow and conceptual depth
- Any phenomenon requiring analysis of causes, effects, and mechanisms where logical consistency is key
- Any subject involving contrasting ideas or logical progressions
- The error is often an antonym of the correct word (e.g., 'increase' instead of 'decrease', 'stronger' instead of 'weaker')
- 각 번호에 해당하는 어휘는 반드시 HTML 밑줄 태그(`<u>...</u>`)를 사용해 표기하십시오.
- 예: ①<u>increase</u>, ②<u>reduce</u>, ...
- 지문 내 정확히 5개의 어휘가 ①~⑤ 번호와 함께 밑줄로 처리되어야 합니다.
- 번호와 밑줄은 항상 붙여서 표기하며, 띄어쓰기 없이 사용하십시오.

**Required JSON Output Format:**
{
  "question": "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]",
  "passage": "[Academic text with ①<u>word1</u> ②<u>word2</u> ③<u>word3</u> ④<u>word4</u> ⑤<u>word5</u> placed throughout the text]",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the vocabulary error]"
}
"""

SPEC = {
    "type": "reading_vocabulary_judgment",
    "components": [
        "question",
        "passage",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count_passage": [130, 150],
        "passage_format": "vocabulary_underline",
        "answer_indexing": "1-based"
    },
    "title": "읽기 30번 - 어휘의 적절성 파악"
}
