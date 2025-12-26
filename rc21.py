# app/prompts/items/rc21.py

"""
RC21 — Reading 21: Underlined Expression Inference (함축 의미 추론)

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC21 유형(밑줄 친 표현의 의미 추론)에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""
Create a CSAT Reading Item 21 (Underlined Expression Inference) following these specifications.

## ITEM CHARACTERISTICS & METHODOLOGY
### Assessment Objective
- **Core Skill**: Inferring the contextual meaning of metaphorical or idiomatic expressions
- **Cognitive Process**: Analyze surrounding context → Interpret figurative expression → Select meaning consistent with passage
- **Difficulty Target**: 중상 수준 (예상 정답률 40–55%, 변별도 0.3–0.4)

### Text Type & Structure
- **Format**: Academic explanatory passage (history, science, philosophy, culture, society)
- **Structure Pattern**: Concept introduction → Analysis → Use of metaphorical expression → Explanation/contrast
- **Expression Placement (HARD)**: The underlined metaphorical/idiomatic expression **must appear in the final 1–2 sentences**, summarizing or concluding the argument.

### Expression Selection Policy
- ❌ Do NOT use **"the tip of the iceberg."**
- Use another widely recognized idiom/metaphor appropriate for CSAT.

### Language Specifications
- **Passage Length**: 150–180 words (English only)
- **Sentence Complexity**: Complex sentences with academic cohesion
- **Vocabulary Level**: CSAT+O3000 academic vocabulary
- **Underline exactly one** expression with `<u> ... </u>` in the passage.

### Question Format Requirements
- **Stem (Korean)**: "밑줄 친 <u>EXPRESSION</u>이 다음 글에서 의미하는 바로 가장 적절한 것은? [3점]"
- **Options (English, 5지)**:  
  - 5 plain-text statements **in English** (no numbering/bullets).  
  - Include: literal meaning, partial meaning, opposite meaning, unrelated meaning, correct figurative meaning.
  - All options must be written in English.  

### Correct Answer Rule (HARD)
- `"correct_answer"` **MUST** be a number in the range 1–5.  
- Accepted formats: **integer** (e.g., `5`) or **numeric string** (e.g., `"5"`).  
- ❌ Do NOT output the option text itself.  
- ❌ Do NOT output words, phrases, or anything other than the index number.

### Explanation (Korean)
- Provide concise rationale:  
  - 정답 근거: 본문 맥락 + 표현의 비유적 의미.  
  - 오답 배제: 각 보기별 간단한 배제 이유.  

### Output Validation Rules
1. Passage word count: 150–180 (English only).  
2. Exactly one `<u> ... </u>` expression, also used in the stem.  
3. Options: 5 **English** plain-text strings (no numbering/bullets).  
4. `"correct_answer"`: integer 1–5 or string `"1"`–`"5"`.  
5. Explanation: Korean only.  
6. No extra fields beyond the schema.  

**Required JSON Output Format:**
{
  "question": "밑줄 친 <u>EXPRESSION</u>이 다음 글에서 의미하는 바로 가장 적절한 것은? [3점]",
  "passage": "[150–180 word academic passage with <u>EXPRESSION</u> in English]",
  "options": ["...", "...", "...", "...", "..."],
  "correct_answer": 5,
  "explanation": "[한국어 해설: 정답 근거 및 오답 배제 이유]"
}
"""

SPEC = {
    "type": "reading_underlined_inference",
    "components": [
        "question",
        "passage",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count_passage": [150, 180],
        "underline_required": True,
        "underline_in_stem_sync": True,
        "ban_expressions": ["the tip of the iceberg"],
        "options_language": "English",  # ✅ 옵션 언어 명시
        "options_plain_text_only": True,
        "answer_indexing": "1-based",
        "answer_must_be_numeric": True
    },
    "title": "읽기 21번 - 함축 의미 추론"
}