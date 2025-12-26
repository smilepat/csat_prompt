# app/prompts/items/rc33.py

"""
RC33 — Reading 33: Blank Inference (Phrase/Clause, High Difficulty)

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC33 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 33 (Blank Inference - Phrase/Clause, High Difficulty) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Inference of logical paradox or hidden truth from a complex narrative context.
- **Cognitive Process**: Analyzing cause-and-effect relationships and sequences of events; identifying a point of logical divergence; deducing the narrative's underlying principle.
- **Difficulty Target**: 중 수준 (예상 정답률 35.7%, 변별도 0.3)

### Abstractness & Complexity Controls
- **Abstractness Level (1–9)**: 9
- **Syntactic Complexity Targets (optional)**:
  - avg_words_per_sentence: 32.25
  - avg_clauses_per_sentence: 4.25
  - subordination_ratio: 0.5
- **Vocabulary Profile (optional)**: Very high abstractness vocabulary (highly conceptual, theoretical terms)

### Text Type & Structure
- **Format**: Academic or theoretical narrative
- **Structure Pattern**: Introduction of a concept → Development through clear, declarative sentences → A point of logical consequence or conclusion that requires inference
- **TYPE_SPECIFIC_PLACEMENT**: The blank should be positioned at a crucial point where the core argument culminates or a logical consequence is drawn from the preceding sentences.

### Type-Specific Policy
- Passage should avoid excessive nominalization, favoring clear subject-verb structures to convey logical relationships.
- The passage should explain abstract concepts through clear, sequential statements and avoid dense noun phrases.
- The correct answer must follow a clear logical cause-and-effect or narrative progression.

### Language Specifications
- **Passage Length**: 130–150 words
- **Sentence Style**: Academic cohesion, with clear prose; complexity is achieved through nuanced phrasing and logical links rather than nominalizations.
- **TYPE_SPECIFIC_MARKUP**: Use `_____` (five underscores) to indicate the blank.

### Question Format Requirements
- **Stem**: "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은? [3점]"
- **Options**: 5개 선택지, 모두 고난도 논리적 구/절
- **Correct Answer**: The option that logically and coherently concludes the clear narrative progression.
- **Distractors Policy (KR)**: 정답과 반대되는 논리, 부분적으로 타당하나 전체 논리를 벗어난 내용, 지엽적 세부 정보에만 초점을 맞춘 내용을 포함하여 매력적인 오답을 구성.

**Required JSON Output Format:**
{
  "question": "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은? [3점]",
  "passage": "[130–150 word academic passage in English with a single blank, composed of clear, narrative sentences with minimal nominalization.]",
  "options": ["sophisticated phrase/clause 1", "sophisticated phrase/clause 2", "sophisticated phrase/clause 3", "sophisticated phrase/clause 4", "sophisticated phrase/clause 5"],
  "correct_answer": [1-5],
  "explanation": "[한국어 해설: 정답 근거 및 오답 배제 이유]"
}
"""

SPEC = {
    "type": "reading_blank_phrase_clause_hard",
    "components": [
        "question",
        "passage",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count_passage": [130, 150],
        "passage_format": "blank_filling",
        "answer_indexing": "1-based",
        "abstractness_level": 9,
        "difficulty": "high"
    },
    "title": "읽기 33번 - 빈칸 추론 (구/절, 고난도)"
}
