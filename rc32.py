# app/prompts/items/rc32.py

"""
RC32 — Reading 32: Blank Inference (Phrase/Clause)

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC32 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 32 (Blank Inference - Phrase/Clause) following these specifications.

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Inference of a key phrase or clause within a complex context.
- **Cognitive Process**: Complex context analysis → multi-layered logic comprehension → identifying the blank's core function → inferring high-level content.
- **Difficulty Target**: 상 수준 (예상 정답률 15–20%, 변별도 0.3 이상)

### Abstractness & Complexity Controls
- **Abstractness Level (1–9)**: MUST be 8 (high abstractness, theoretical reasoning required)
- **Syntactic Complexity Targets**:
  - Each sentence MUST average around 19 words.
  - Each sentence MUST contain about 2.2 clauses.
  - Subordination ratio MUST be ~0.4.
  - If the passage is simpler, regenerate.
- **Vocabulary Profile**: MUST use CSAT+AWL vocabulary.

### Text Type & Structure
- **Format**: Academic or theoretical discourse
- **Structure Pattern**: Introduction of a concept → theoretical background → a point of logical consequence or conclusion that requires inference → specific explanation → example presentation → conclusion.
- **TYPE_SPECIFIC_PLACEMENT**: The blank should be positioned at a crucial point of logical transition, requiring a high-level inference.

### Type-Specific Policy
- The passage MUST have a clear, logical flow.
- The correct answer MUST be a phrase or clause that perfectly completes the argument.

### Language Specifications
- Passage Length: 130–150 words (MUST be enforced)
- Sentence Style: Academic cohesion with complex logical development.
- Use `_____` for the blank.

### Question Format Requirements
- Stem: "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?"
- Options: 5 choices, ALL verb phrases (verb + object/complement)
  - At least one MUST contain passive voice.
  - At least one MUST contain present perfect.
  - At least one MUST contain a to-infinitive construction.
- **Options (Korean, 5지)**:
  - **DISTRACTOR_POLICY_KR**: 겉으로 관련되어 보이나 논리적으로 부정확하거나 지엽적인 내용을 포함한 오답을 구성.
  - **TYPE_SPECIFIC_OPTIONS_KR**: 모든 선택지는 동사구(verb phrase) 형태로 만들어져야 함 (예: 동사 + 목적어, 동사 + 목적어 + 목적보어 등).
- Correct Answer: The option that logically and coherently completes the argument.
- Distractors: Seem relevant but logically inaccurate or too narrow.

**Required JSON Output Format:**
{
  "question": "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?",
  "passage": "[130–150 word academic passage in English with a single blank.]",
  "options": [
    "verb phrase option",
    "verb phrase option",
    "verb phrase option",
    "verb phrase option",
    "verb phrase option"
  ],
  "correct_answer": [1-5],
  "explanation": "[한국어 해설: 정답 근거 및 오답 배제 이유]"
}
"""

SPEC = {
    "type": "reading_blank_phrase_clause",
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
        "abstractness_level": 8
    },
    "title": "읽기 32번 - 빈칸 추론 (구/절)"
}
