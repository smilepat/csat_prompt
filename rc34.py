# app/prompts/items/rc34.py

"""
RC34 — Reading 34: Blank Inference (Topic Sentence Predicate)

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC34 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 34 (Blank Inference - Topic Sentence Predicate) following these specifications:

## ABSOLUTE RULES (DO NOT VIOLATE)
1. The blank (_____) MUST appear **only in the very first sentence** of the passage.
   - The first sentence MUST begin with a clear subject (e.g., "Global cooperation," "Technological innovations," "Traditional practices"), followed by `_____`.
   - The blank must cover the **entire predicate** of the first sentence.
   - DO NOT place the blank in the middle or at the end of the passage.
   - If the blank is not in the first-sentence predicate, the output is INVALID.

2. Passage length MUST be between **130 and 150 words**.
   - If it is shorter or longer, the output is INVALID.

3. Sentence complexity MUST match the following targets:
   - Average ≈ 21.9 words per sentence
   - Average ≈ 2.75 clauses per sentence
   - Subordination ratio ≈ 0.5 or higher
   - You MUST include complex sentences with relative clauses, subordinate clauses, or participial constructions.

4. Vocabulary MUST include several words from the **Academic Word List (AWL)**, such as:
   - integrate, facilitate, exemplify, commodify, resonate, sustain, embody, demonstrate, transformation, mechanism.
   - At least **3 AWL words** must appear.
   - If AWL words are missing, the output is INVALID.

### Vocabulary Profile
"vocabulary_difficulty": "AWL"

## ITEM CHARACTERISTICS & METHODOLOGY
- **Assessment Objective**: Infer the correct predicate that generalizes multiple examples into a unifying principle.
- **Cognitive Process**: 사례 분석 → 공통 원리 추상화 → 일반화된 술부 도출
- **Difficulty Target**: 최상 수준 (예상 정답률 26.8%, 변별도 0.2–0.3)

## Discourse Structure
- First sentence: Subject + `_____` (general principle predicate)
- Body: Example 1 → Example 2 → Example 3 (all supporting the general principle)
- Final sentence: Reaffirmation of the principle, using AWL vocabulary.

## Question Format Requirements
- **Stem (Korean)**: "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은? [3점]"
- **Options (Korean, 5지)**:
  - **DISTRACTOR_POLICY_KR**: 일부 사례에만 적용되거나, 주된 논리와 상반되는 내용을 담는 등 논리적으로 부정확한 오답을 구성.
  - **TYPE_SPECIFIC_OPTIONS_KR**: 모든 선택지는 빈칸 앞부분에 제시된 주어 + (조동사)에 이어질 수 있는 완전한 술부(predicate)로 이루어져야 함.
- **Correct Answer**: 글 전체의 귀납적 결론을 가장 정확하게 서술하는 선택지
- **Explanation (Korean)**:
  - 정답 근거: 본문 맥락 + 유형별 핵심 근거 명시
  - 오답 배제: 각 보기별 왜 틀렸는지 1–2문장 설명

## OUTPUT CONTRACT OVERRIDE (STRICT)
- **This item overrides the BASE output keys.**
- Use **exactly** the following top-level JSON keys and value types.
- **Do NOT** use "stimulus" or "question_stem" keys.
- The output must be a **single JSON object** with **no extra text**.

{
  "question": "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은? [3점]",
  "passage": "[130–150 word academic passage in English beginning with a sentence that has a blank after the subject.]",
  "options": ["...", "...", "...", "...", "..."],
  "correct_answer": 1,
  "explanation": "[한국어 해설: 정답 근거 및 오답 배제 이유]",
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": []
}

## SELF-CHECK BEFORE RETURNING
- JSON parses with a standard parser.
- Keys **exactly** match the contract above.
- `correct_answer` is an integer in [1,5].
- `passage` is 130–150 words; first sentence has **subject + `_____` as predicate**.
- At least 3 AWL words appear.
- Options are 5, mutually exclusive, and grammatically fit after the subject.
- Explanation in Korean justifies the key and rules out distractors.
"""

SPEC = {
    "type": "reading_blank_topic_predicate",
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
        "word_count_passage": [130, 150],
        "passage_format": "blank_filling",
        "blank_position": "first_sentence_predicate",
        "answer_indexing": "1-based",
        "vocabulary_profile": "AWL"
    },
    "title": "읽기 34번 - 빈칸 추론 (주제문/술부)"
}
