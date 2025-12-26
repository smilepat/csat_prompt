# app/prompts/items/lc10.py

"""
LC10 — Listening 10: Chart Information

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 LC10 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Listening Item 10 (Chart Information) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- Core Skill: Integrating auditory criteria with visual chart information for elimination and final selection
- Cognitive Process: Sequential elimination → Apply each criterion in order → Narrow down to final choice
- Difficulty Level: Intermediate multi-modal information integration

### Discourse Type & Structure
- Format: Two-person dialogue about selection from chart options
- Structure Pattern: Need identification → Chart consultation → Criteria specification → Step-by-step elimination → Final decision
- Content Flexibility: Any selection scenario with multiple criteria (products, services, options)
- Interaction Type: Collaborative decision-making with criteria application

### Language Specifications
- Transcript Length: 90-110 words (approximately 45-55 seconds)
- Sentence Complexity: Moderate with comparative and conditional expressions
- Vocabulary Level: Comparative and criteria-based vocabulary
- Speech Rate: Natural pace with clear criteria articulation

### Vocabulary Profile
"vocabulary_difficulty": "CSAT",
"low_frequency_words": []

### Question Format Requirements
- Stem: "다음 표를 보면서 대화를 듣고, [화자]가 구입할 [상품]을 고르시오."
- Options: 5 chart entries representing different combinations of attributes
- Correct Answer: Must be the option that satisfies all stated criteria
- Distractors: Options that satisfy some but not all criteria

---

## ADDITIONAL STRUCTURAL CONSTRAINTS

### Listening Item Structure (LC10 Chart)
1. Chart: 5 items × 4 attributes.
2. Transcript: Criteria must be presented strictly in the same order as chart columns (Attribute 1 → 2 → 3 → 4).
3. Sequential Elimination:
   - At each stage, exactly **one option** must be eliminated.
   - Process: 5 → 4 → 3 → 2 → 1 remaining.

### Elimination Rules by Attribute
- **Attribute 1 (Price/Fee)**: Must use either an upper limit (≤ B) or a unique extreme (lowest/highest) so that exactly one option is eliminated.
- **Attribute 2 (Length/Weight/People/Time)**: Must use either a lower bound (≥ N) or a time condition (e.g., after T) to eliminate exactly one option.
- **Attribute 3 (Category like Color/Material)**: Must use a restriction such as "no X," with the distribution designed so that among the remaining 3, only one has X → leaving 2 candidates.
- **Attribute 4 (Binary Feature such as Yes/No, A/B)**: The final 2 candidates must be identical in Attributes 1–3 but opposite in Attribute 4. The speaker preference at the end decides the unique correct answer.

### Final Selection Rule
- After applying Attribute 1–3, exactly two options remain.
- These two options must have identical values in Attributes 1–3 but opposite values in Attribute 4.
- The final dialogue statement must explicitly state a preference for Attribute 4, ensuring a unique answer.

---

## STRICT OUTPUT CONTRACT (DO NOT VIOLATE)
- Output JSON only. No extra text.
- Must include: item_type, question, transcript, chart_data, options, correct_answer, explanation.
- item_type must be "LC_CHART".
- transcript: English dialogue (90-110 words) with speaker markers M:/W:.
- chart_data must be exactly this shape (no markdown, no object-array, no datasets):
  {
    "headers": ["Item", "Attribute 1", "Attribute 2", "Attribute 3", "Attribute 4"],
    "rows": [
              ["1", "...", "...", "...", "..."],
              ["2", "...", "...", "...", "..."],
              ["3", "...", "...", "...", "..."],
              ["4", "...", "...", "...", "..."],
              ["5", "...", "...", "...", "..."]
            ]
  }
- The first header (identifier) is fixed to "Item" and the values must be "1"~"5".
- All headers and rows must be in English only (ASCII).
- All cells must be strings (or numbers) only; HTML/markdown prohibited.
- options must be exactly ["1","2","3","4","5"] (same identifiers).
- correct_answer must be an integer 1–5 (number).
- explanation must be in Korean and must justify why the chosen row satisfies all stated criteria from the dialogue.
"""

SPEC = {
    "type": "listening_chart",
    "components": [
        "item_type",
        "question",
        "transcript",
        "chart_data",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "transcript_format": "speaker_separation",
        "word_count": [90, 110],
        "duration_seconds": [45, 55],
        "chart_integration": True,
        "sequential_elimination": True
    },
    "title": "듣기 10번 - 표 정보 확인"
}
