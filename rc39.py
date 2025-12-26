# app/prompts/items/rc39.py

"""
RC39 — Reading 39: Sentence Insertion

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC39 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 39 (Sentence Insertion) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 주어진 문장의 적절한 삽입 위치 파악 능력 측정
- **Processing Pattern**: 주어진 문장 분석 → 글의 논리적 흐름 파악 → 각 삽입 위치별 적합성 검토 → 최적 위치 선택
- **Evaluation Focus**: 담화 표지와 내용의 논리적 연결을 통한 문장 삽입 위치의 정확한 파악 능력

### Discourse Structure
- **Pattern**: 주어진 문장(박스) → 5개의 삽입 위치가 표시된 본문
- **Flow**: 독립적 문장 → 삽입 위치 ① → 문단1 → 삽입 위치 ② → 문단2 → 삽입 위치 ③ → 문단3 → 삽입 위치 ④ → 문단4 → 삽입 위치 ⑤
- **Key Positioning**: 주어진 문장이 글의 논리적 흐름에 가장 자연스럽게 연결되는 위치를 찾아야 함

### Language Specifications
- **Passage Length**: 120-140 words
- **Sentence Complexity**: Moderate to complex, with strong logical cohesion that creates a single correct insertion point. (Avg. 2.0+ clauses per sentence)
- **Vocabulary Level**: Academic vocabulary with an emphasis on discourse markers and cohesive devices.
- **Reading Level**: Academic expository or argumentative style.

### Vocabulary Profile
"vocabulary_difficulty": "AWL"

### Question Format Requirements
- **Stem**: "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은? [3점]"
- **Options**: 5개 선택지 (①②③④⑤), 각각 본문의 삽입 위치
- **Correct Answer**: 논리적으로 가장 자연스러운 삽입 위치
- **Distractors**: 부분적으로는 연결되나 전체적으로 부자연스러운 위치들

### Content Generation Guidelines
- Any complex topic with sophisticated logical flow and development
- Any subject requiring advanced sequential reasoning or abstract relationships
- Any concept with subtle transition points and complex argumentation
- The passage must include five insertion points marked exactly as **( ① )**, **( ② )**, **( ③ )**, **( ④ )**, **( ⑤ )** (with parentheses and spacing).
- Do not use any alternative markers such as (1), [1], {1}, or plain ① without parentheses.
- The given sentence must fit naturally into only one of these points.
- Do not use alternative markers like (1) or [1].

**Required JSON Output Format:**
{
  "question": "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은? [3점]",
  "given_sentence": "[Independent sentence to be inserted]",
  "passage": "[Text with ①②③④⑤ insertion points in English]",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the logical insertion point]"
}
"""

SPEC = {
    "type": "reading_sentence_insertion",
    "components": [
        "question",
        "given_sentence",
        "passage",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count_passage": [120, 140],
        "passage_format": "insertion_points",
        "given_sentence_highlight": True,
        "answer_indexing": "1-based",
        "difficulty": "3점"
    },
    "title": "읽기 39번 - 문장 위치 추론"
}
