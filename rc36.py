# app/prompts/items/rc36.py

"""
RC36 — Reading 36: Paragraph Ordering

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC36 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 36 (Paragraph Ordering) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 논리적 글의 순서 파악 능력 측정
- **Processing Pattern**: 주어진 문단 분석 → 각 단락의 기능 파악(예시, 부연, 결론 등) → 논리적 연결(대명사, 연결어) 추적 → 최적 배열 도출
- **Evaluation Focus**: 담화 표지와 내용의 논리적 흐름을 통한 문단 순서의 정확한 배열 능력

### Discourse Structure
- **Pattern**: 주어진 도입 문단(박스) → 순서가 섞인 (A), (B), (C) 단락
- **Flow**: 고정된 시작(원칙/개념 제시) → 세 개의 단락을 논리적 순서(예: 일반→구체, 원인→결과)로 배열
- **Key Positioning**: 도입 문단이 전체의 맥락을 설정하고, 나머지 세 단락은 대명사, 지시어, 연결어 등을 통해 논리적 순서를 추론해야 함

### Language Specifications
- **Passage Length**: 130-150 words (total across all paragraphs)
- **Sentence Complexity**: Moderate to complex, with explicit logical connectors (pronouns, discourse markers) to signal paragraph order. (Avg. 2.0-2.2 clauses per sentence)
- **Vocabulary Level**: Academic and transitional vocabulary.
- **Reading Level**: Academic expository or argumentative style.   

### Vocabulary Profile
"vocabulary_difficulty": "AWL"

### Question Format Requirements
- **Stem**: "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?"
- **Options**: 5개 선택지, 모두 (A)-(C)-(B) 형태의 순서 조합
- **Correct Answer**: 논리적으로 가장 자연스러운 단락 순서
- **Distractors**: 부분적으로는 논리적이나 전체적으로 부자연스러운 순서들

### Content Generation Guidelines
- Any academic or explanatory topic with a clear logical progression
- Any subject requiring sequential development or logical order
- Any concept with problem-solution or cause-effect relationships
- Each paragraph must be clearly labeled as (A), (B), and (C) and contain distinct content.

**Required JSON Output Format:**
{
  "question": "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
  "intro_paragraph": "[Introductory paragraph in a box]",
  "passage_parts": {
    "(A)": "[Paragraph A content]",
    "(B)": "[Paragraph B content]",
    "(C)": "[Paragraph C content]"
  },
  "options": ["(A)-(C)-(B)", "(B)-(A)-(C)", "(B)-(C)-(A)", "(C)-(A)-(B)", "(C)-(B)-(A)"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the logical order]"
}
"""

SPEC = {
    "type": "reading_paragraph_ordering",
    "components": [
        "question",
        "intro_paragraph",
        "passage_parts",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count_total": [130, 150],
        "passage_format": "paragraph_labels",
        "answer_indexing": "1-based"
    },
    "title": "읽기 36번 - 글의 순서 배열"
}
