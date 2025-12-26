"""
RC24 — Reading 24: Title Inference (제목 추론)

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC24 유형(제목 추론)에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""
Create a CSAT Reading Item 24 (Title Inference) following these specifications.

## ITEM CHARACTERISTICS & METHODOLOGY
### Assessment Objective
- **Core Skill**: Inferring the most appropriate **title** that captures and synthesizes the passage’s central idea.
- **Cognitive Process**: Identify contrast or development → Integrate all information → Express synthesis as an abstract title.
- **Difficulty Target**: 중상 (예상 정답률·변별도는 시스템 가이드에 준함)

### Text Type & Structure
- **Format**: Complex expository or analytical text (topics may include science, society, culture, technology, or philosophy).
- **Choose ONE structure pattern** and maintain it throughout:
  1) **Contrast–Synthesis**: Present a common assumption → show contrasting evidence → conclude with a synthesized insight.
  2) **Problem–Solution**: Present a realistic issue → explain an effective solution → synthesize the implication.
  3) **Historical–Analytical**: Connect a present phenomenon with historical context → analyze continuity and innovation → synthesize a balanced conclusion.
- **Opening Section (HARD)**: Must include a clear contrast between common belief and actual fact, using patterns like:
  - “It is natural to assume … However, …”
  - “People often believe … yet …”
- **Conclusion (HARD)**: Final 1–2 sentences must contain a synthesis connector (e.g., therefore, thus, overall, in sum, taken together) and summarize the integrated perspective.

### Language Specifications
- **Passage Length**: 150–180 words (English only)
- **Style**: Academic cohesion; moderate-to-high syntactic complexity; logical flow
- **Vocabulary Level**: CSAT+O3000 academic vocabulary (advanced yet readable)

### Question & Options
- **Stem (Korean)**: "다음 글의 제목으로 가장 적절한 것은?"
- **Options (English, 5지)**:
  - Write exactly **5 English title statements**, **without numbering or bullets**.
  - Each option should be concise, 5–10 words.
  - The **correct option** must be an **abstract noun phrase** or include nominal endings such as **-ing / -ion / -ity / -ness**.
  - **Wrong options** should vary naturally, including:
    - focusing only on one minor aspect,
    - being too general or too specific,
    - or shifting to a tangentially related concept.

### Correct Answer Rule (HARD)
- `"correct_answer"` must be a **string** between `"1"`–`"5"`.
- The answer index corresponds to the best integrative title only.
- Do **not** output the title text again inside `"correct_answer"`.

### Explanation (Korean)
- Provide concise reasoning:
  - **정답 근거**: 본문 전체의 결론(통합된 관점)을 기반으로 왜 선택지가 가장 적절한지 설명.
  - **오답 배제**: 각 선택지가 왜 부적절한지 간단히 기술 (핵심 이유만 1–2문장씩).

### Output Validation Rules
1. Passage: 150–180 words, English only.
2. Contains a clear contrast trigger near the beginning (“It is natural to assume … However …” or equivalent).
3. Includes at least one contrast cue (“however”, “yet”, “while”, “whereas”) and one synthesis cue (“therefore”, “thus”, “overall”, “in sum”, “taken together”) near the conclusion.
4. Exactly 5 English title options, with no numbering or bullets.
5. `"correct_answer"`: string `"1"`–`"5"`.
6. `"explanation"`: written in **Korean**, containing both **정답 근거** and **오답 배제**.
7. No extra fields beyond the defined schema.

**Required JSON Output Format:**
{
  "question": "다음 글의 제목으로 가장 적절한 것은?",
  "passage": "[150–180 word analytical passage in English]",
  "options": ["...", "...", "...", "...", "..."],
  "correct_answer": "1",
  "explanation": "[한국어 해설: 정답 근거 및 오답 배제 이유]"
}
"""

SPEC = {
    "type": "reading_title_inference",
    "components": [
        "question",
        "passage",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count_passage": [150, 180],
        "english_only_passage": True,
        "require_commonsense_trigger": True,
        "require_contrast_cue": True,
        "require_synthesis_in_conclusion": True,
        "options_plain_text_only": True,
        "options_english_only": True,
        "title_abstract_required": True,
        "answer_indexing": "1-based",
        "answer_must_be_string_1_5": True,
        "explanation_language": "ko"
    },
    "title": "읽기 24번 - 제목 추론"
}
