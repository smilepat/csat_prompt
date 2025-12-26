# app/prompts/items/rc35.py

"""
RC35 — Reading 35: Irrelevant Sentence

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC35 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 35 (Irrelevant Sentence) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 글의 통일성을 해치는 문장 식별 능력 측정
- **Processing Pattern**: 주제 파악 → 각 문장의 관련성 평가 → 논리적 이탈 문장 식별
- **Evaluation Focus**: 글의 일관성과 논리적 전개 속에서 미묘하게 어긋나는 문장을 찾아내는 능력

### Discourse Structure
- **Introductory Paragraph**: 반드시 **2~3절 이상으로 연결된 Complex sentence**로 주제 제시 (조건절, 인과절, 대조절 포함).
- **Main Passage (①~⑤)**:
  - ① 주제 관련 구체적 설명 또는 사례  
  - ② 주제 확장/일반화  
  - ③ 또는 ④: **무관 문장** (겉보기에 관련 있어 보이지만 실제 주제에서 벗어남)  
  - 나머지 문장: 주제와 긴밀히 연결  
  - ⑤ 결론 또는 주제 강화  

### Language Specifications
- **Passage Length**: 120–140 words
- **Sentence Complexity**: 평균 2.2절 이상, 주제문은 반드시 복합문
- **Vocabulary Level**: Academic, expository style
- **Reading Style**: Argumentative or expository, high cohesion

### Vocabulary Profile
"vocabulary_difficulty": "AWL",
"low_frequency_words": ["예: collaboration", "예: innovation", "예: comprehensive"]  // 예시 단어, 반드시 사용해야 하는 것은 아님

### Question Format Requirements
- **Stem**: "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?"
- **Options**: ①~⑤
- **Correct Answer**: 반드시 ①~⑤ 중 정확히 하나
- **Distractors**: 나머지 4개 문장은 주제를 강화

### Content Generation Guidelines
- 무관 문장은 **①~⑤ 중 하나**에만 배치해야 함.  
- 무관 문장은 **겉보기에 주제와 관련 있어 보이지만**, 실제로는 논리적 초점을 흐리거나 다른 주제로 전환함.  
  - ❌ 주제와 완전히 무관한 분야(예: 독서 지문에 운동 이야기) → 피하기  
  - ✅ 주제와 부분적으로 연관 있으나, 중심 논리와 어긋나는 내용 (예: 독서의 가치 지문에 출판사의 마케팅 전략 언급)  
- **각 문장은 반드시 같은 단락 안에서 공백으로만 구분되며, 절대 줄바꿈(\\n) 없이 연속해서 이어져야 함.**
- 번호는 **①, ②, ③, ④, ⑤** 순서대로 문장 앞에만 붙인다.

**Required JSON Output Format:**
{
  "question": "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?",
  "passage": "[Introductory complex sentence paragraph] ① ... ② ... ③ ... ④ ... ⑤ ...",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of why the chosen sentence is irrelevant]",
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": ["예: collaboration", "예: innovation", "예: comprehensive"]
}
"""

SPEC = {
    "type": "reading_irrelevant_sentence",
    "components": [
        "question",
        "passage",
        "options",
        "correct_answer",
        "explanation",
        "vocabulary_difficulty",
        "low_frequency_words"
    ],
    "processing_hints": {
        "word_count_passage": [120, 140],
        "passage_format": "intro_complex_sentence + sentence_numbers_inline",
        "answer_indexing": "1-based"
    },
    "title": "읽기 35번 - 무관한 문장 찾기"
}
