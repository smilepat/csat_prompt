"""
RC41_42 — Reading 41–42: Long Reading Set (Minimal Edit from Existing Passage)

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC41_42 세트(장문 독해: 41 제목, 42 어휘 적절성)에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""
Create a CSAT Reading Set for Items 41–42 (Long Reading Set) by **MINIMALLY EDITING** the provided passage, then producing two questions: **Q41 (Title)** and **Q42 (Vocabulary Appropriateness)**.

## ITEM CHARACTERISTICS & METHODOLOGY
### Assessment Objectives
- **Q41 (Title)**: Inferring the most appropriate **title** that synthesizes the passage’s central idea.
- **Q42 (Vocabulary)**: Identifying the **contextually inappropriate** underlined word among five marked positions.

### Input Guard & Editing Scope (STRICT Minimal Edit)
- Use **ONLY** the provided passage as the content basis.
- Preserve original **claims, facts,** and **line of reasoning**.
- **Do NOT** change topic, add new examples, or reorder ideas.
- Allowed edits (minimal):
  1) Insert **paragraph breaks** at natural boundaries (topic shift, method→example, example→implication, conclusion).
  2) Insert **exactly five markers** with underlined words: (a) <u>word</u> … (e) <u>word</u>.
  3) Replace at most **ONE** existing word (or add **ONE**) solely to create the single misfit required by Q42.
  4) At most **two** tiny function-word fixes if needed for grammar.
- Disallowed: deleting sentences, adding new claims/examples, duplicating content.

### Paragraphing Rules (STRICT)
- Final passage must have **≥ 2 paragraphs** (preferred **3–4**).
- Paragraph separators: **exactly one blank line** (`\n\n`).
- Distribute the five markers across **≥ 2 paragraphs**; **no single paragraph** may contain **3 or more** markers (max 2 per paragraph).

### Marker & Underline Rules (STRICT)
- You MUST insert **exactly five** markers with the following **exact pattern**: `\([a-e]\)\s*<u>[A-Za-z\-]+</u>`
  - Lowercase marker letters only: **(a)(b)(c)(d)(e)**.
  - Each underline is **ONE** English word only (no spaces/punctuation inside).
- Suggested discourse roles to guide placement:
  - (a) concept introduction, (b) mechanism/process, (c) transition/cause–effect,
  - (d) example/evidence, (e) conclusion/generalization.
- Exactly **ONE** of the five underlined words MUST be **contextually inappropriate**; the other **four MUST be appropriate**.

### Length & Language
- Passage: **English only**; keep overall length close to original (**±10%**).
- Questions & explanations: **Korean**.

## QUESTION SPECIFICATIONS
### Q41 — Title Inference
- **Stem (Korean)**: "윗글의 제목으로 가장 적절한 것은?"
- **Options (English, 5지)**:
  - Write exactly **5 English title statements**, **without numbering or bullets**.
  - Each option should be concise, **5–10 words**.
- **Correct Answer Rule**:
  - `"correct_answer"` must be a **string** in `"1"`–`"5"`.
  - Index corresponds to the most integrative title only.

### Q42 — Vocabulary Appropriateness
- **Stem (Korean)**: "밑줄 친 (a)~(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]"
- **Options (fixed)**: exactly `["(a)", "(b)", "(c)", "(d)", "(e)"]`.
- **Correct Answer Rule**:
  - `"correct_answer"` must be a **string** in `"1"`–`"5"`, pointing to the misfit marker.
- **Explanation (Korean)**:
  - Explicitly justify **WHY** the chosen underlined word is a misfit in context, mentioning the relevant sentence/discourse role mismatch.

## OUTPUT VALIDATION RULES
1. Passage contains **exactly 5** occurrences of markers with underlined single words: `(a) <u>...</u>` … `(e) <u>...</u>`.
2. **≥ 2 paragraphs**, separated by **one blank line** (`\n\n`); markers spread across **≥ 2** paragraphs; **no paragraph has ≥ 3 markers**.
3. Exactly **ONE** underlined word is a **misfit**; other four are **appropriate**.
4. **Q41** options: 5 English titles (no numbering/bullets); **Q42** options: fixed as above.
5. Both `"correct_answer"` fields are **strings** in `{"1","2","3","4","5"}`.
6. Questions and explanations are **Korean**; passage is **English only**.
7. Output is **valid JSON**; **no extra keys** beyond the defined schema.

## REQUIRED JSON OUTPUT FORMAT
Return **only** the following JSON object:
{
  "set_instruction": "[41~42] 다음 글을 읽고, 물음에 답하시오.",
  "passage": "[Edited passage with (a) <u>...</u> ... (e) <u>...</u>, split into ≥2 paragraphs with blank lines.]",
  "questions": [
    {
      "question_number": 41,
      "question": "윗글의 제목으로 가장 적절한 것은?",
      "options": ["Title 1", "Title 2", "Title 3", "Title 4", "Title 5"],
      "correct_answer": "1",
      "explanation": "[한국어 해설: 제목 선택 근거]"
    },
    {
      "question_number": 42,
      "question": "밑줄 친 (a)~(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]",
      "options": ["(a)", "(b)", "(c)", "(d)", "(e)"],
      "correct_answer": "1",
      "explanation": "[한국어 해설: 선택한 밑줄 어휘가 왜 부적절한지, 해당 문장/담화 기능과의 불일치 근거]"
    }
  ]
}

## FINAL SELF-CHECK (REJECT INTERNALLY IF ANY FAILS)
- Exactly 5 matches of the pattern for markers/underlines: `(a) <u`, `(b) <u`, `(c) <u`, `(d) <u`, `(e) <u`.
- Each underline is **one** word only.
- Markers spread across **≥ 2** paragraphs; **no paragraph** contains **3 or more** markers.
- Exactly **one** misfit underlined word; **four** appropriate.
- Q41 options = 5 English titles; Q42 options fixed; both `"correct_answer"` fields are strings in `{"1","2","3","4","5"}`.
- Output is valid JSON; no extra commentary.
---
Use this passage ONLY:
```passage
<PASSAGE>
```"""

SPEC = {
    "type": "set",
    "set_size": 2,
    "start_number": 41,
    "components": ["passage", "questions"],
    "processing_hints": {
        "passage": "vocabulary_marking_with_underline",
        "paragraphing": "at_least_two_paragraphs",
        "markers_required": ["(a)", "(b)", "(c)", "(d)", "(e)"],
        "exactly_one_misfit": True,
        "q41_options_english_titles": True,
        "q42_options_fixed_a_to_e": True,
        "answer_indexing": "1-based",
        "answer_must_be_string_1_5": True,
        "explanations_language": "ko",
        "english_only_passage": True
    },
    "title": "읽기 41-42번 - 장문 독해 (기존 지문 최소 수정·세트화)"
}
