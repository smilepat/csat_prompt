# app/prompts/items/rc43_45.py

"""
RC43_45 — Reading 43-45: Long Reading Set (Paragraph Order + Reference + Content)

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC43_45 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 43–45 (Long Reading Set) in perfect JSON format.

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- Core Skill: Identify paragraph order, referent resolution, and content correctness from a 4-paragraph long reading passage.
- Processing: Understand narrative arc → resolve referents (pronouns & noun phrases) → identify correct order → check specific facts.
- Evaluation: Assess comprehension of narrative structure, referent clarity for characters, and detailed content in one set.
- Special Note for Item 44: Exactly one pronoun among (a)–(e) must refer to a different character (Person B), while the other four pronouns refer to Person A. Person A and Person B MUST be the same gender.

### Character Guidelines
- Use only these names:
  - Female set: Sarah, Chloe, Emma, Mia
  - Male set: Alex, Ben, Jack, Leo
- Choose one gender set only (all-female or all-male).
- Person A and Person B must come from the same chosen set.
- Do not use names outside these sets.

### Story Theme Guidelines
- Randomly select one theme: 'artistic struggle', 'scientific discovery', 'sports rivalry', 'a community project', 'a family secret'.

### Language Specifications
- Passage Length: 400–450 words total (each paragraph 95–115 words).
- Sentence Complexity: Moderate (~2 clauses per sentence).
- Vocabulary Level: CEFR B2 with 2–3 C1 words.

### FORMATTING RULES FOR Q44 UNDERLINES (STRICT)
- Insert exactly five underlined pronouns, labeled (a)~(e) in this format:
  - `(a) <u>she</u>` or `(a) <u>he</u>`
  - The label MUST come **before** the underlined pronoun, never after.
  - Do NOT output `<u>she</u> (a)` or `<u>he</u> (b)` — this is incorrect.
- Placement:
  - (A): include exactly one `(a) <u>pronoun</u>`
  - (B): include exactly one `(b) <u>pronoun</u>`
  - (C): include exactly one `(c) <u>pronoun</u>`
  - (D): include exactly two `(d) <u>pronoun</u>` and `(e) <u>pronoun</u>`
- Allowed forms: strictly lowercase, one-word → `he`, `him`, `she`, `her`.
- Case Variety Rule: At least one objective case (him/her) among the five.
- Absolute Gender Consistency: All five pronouns must be either `he/him` OR `she/her`, never mixed.

### Vocabulary Profile
"vocabulary_difficulty": "AWL"

### Reference Resolution Design (Q44)
- Person A introduced by name in Paragraph A.
- Person B introduced elsewhere in the passage, same gender set.
- Exactly 4 pronouns → Person A; exactly 1 → Person B.
- The "different" pronoun can be at any of (a)~(e). **Do not always assign it to (e).**
- Randomization Emphasis: Vary which of (a)~(e) is Person B across different generations.
- One-Name Window: In each sentence with (a)~(e), mention only one of {Person A, Person B}.
- Nearest Name Wins: Pronoun must clearly refer to the nearest named person.
- Local Subject Default: Prefer subject pronoun (`he`/`she`), but include at least one objective (`him`/`her`).

### Question Format
- Q43: Paragraph order.
- Q44: Reference resolution.
- Q45: Content accuracy.

### Explanation Output Rules
- Q44 explanation MUST explicitly map each label to its referent in double quotes:
  - Example: `(a) → "Sarah", (b) → "Sarah", (c) → "Sarah", (d) → "Sarah", (e) → "Chloe"`
- Also explain why the different one is not the same.
- Q45 explanation MUST check each option and show why the false option is wrong.

### Distractor Design (Q45)
- One option must be false but plausible (role swap, cause-effect twist, or fact distortion).

### OUTPUT FORMAT
Respond ONLY with:

{
  "item_type": "RC_SET",
  "set_instruction": "[43~45] 다음 글을 읽고, 물음에 답하시오.",
  "passage_parts": {
    "A": "... include (a) <u>pronoun</u> ...",
    "B": "... include (b) <u>pronoun</u> ...",
    "C": "... include (c) <u>pronoun</u> ...",
    "D": "... include (d) <u>pronoun</u> and (e) <u>pronoun</u> ..."
  },
  "questions": [
    {
      "question_number": 43,
      "question": "주어진 글 (A)에 이어질 내용을 순서에 맞게 배열한 것으로 가장 적절한 것은?",
      "options": ["B-D-C", "C-B-D", "C-D-B", "D-B-C", "D-C-B"],
      "correct_answer": 1,
      "explanation": "한국어 설명: 단락 전개 순서가 시간적/인과적 흐름에 따라 B-D-C임을 설명."
    },
    {
      "question_number": 44,
      "question": "밑줄 친 (a)~(e) 중에서 가리키는 대상이 나머지 넷과 다른 것은?",
      "options": ["(a)", "(b)", "(c)", "(d)", "(e)"],
      "correct_answer": 1,
      "explanation": "Must explicitly map (a)~(e) to character names in double quotes, and state why the chosen one is different."
    },
    {
      "question_number": 45,
      "question": "윗글에 관한 내용으로 적절하지 않은 것은?",
      "options": [
        "True statement 1",
        "True statement 2",
        "True statement 3",
        "True statement 4",
        "False/distorted statement"
      ],
      "correct_answer": 5,
      "explanation": "각 보기의 사실 여부를 단락의 단서로 확인하여 5번이 잘못된 진술임을 설명."
    }
  ]
}

### FINAL SELF-CHECK
- Exactly 5 pronouns labeled (a)–(e), label before pronoun.
- At least one objective case.
- 4 map to Person A, 1 to Person B (randomized label).
- Each antecedent clear and local.
- Paragraphs 95–115 words each.
- JSON valid.
"""

SPEC = {
    "type": "reading_set",
    "set_size": 3,
    "start_number": 43,
    "components": [
        "item_type",
        "set_instruction",
        "passage_parts",
        "questions"
    ],
    "processing_hints": {
        "word_count_per_paragraph": [95, 115],
        "total_words": [400, 450],
        "passage_format": "labeled_paragraphs_with_pronouns",
        "character_consistency": "same_gender"
    },
    "title": "읽기 43-45번 - 장문 독해 (지칭 추론 - 복합 유형)"
}
