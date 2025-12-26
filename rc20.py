# app/prompts/items/rc20.py

"""
RC20 — Reading 20: Argument Identification (주장 파악)

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC20 유형(주장 파악)에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""
Create a CSAT Reading Item 20 (Argument Identification) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Identifying the main argument in persuasive texts
- **Cognitive Process**: Analyze argumentative structure → Extract central claim → Match with argument options
- **Difficulty Level**: Intermediate argumentative comprehension

### Text Type & Structure
- **Format**: Argumentative or persuasive text
- **Structure Pattern**: Problem presentation → Analysis → Proposed solution → Supporting reasoning
- **Content Flexibility**: Any topic suitable for argumentative treatment
- **Argument Type**: Constructive proposals or recommendations

### Language Specifications
- **Passage Length**: 130–160 words (English only)
- **Sentence Complexity**: Moderate to complex; include clear argumentative features
- **Vocabulary Level**: Argumentative and analytical vocabulary (CSAT+O3000 flavor)
- **Reading Level**: Academic argumentative style appropriate for Korean HS learners
- **Recommended Markers**: therefore, thus, however, in addition, consequently, should, must, recommend

### Question Format Requirements
- **Stem (Korean)**: "다음 글에서 필자가 주장하는 바로 가장 적절한 것은?"
- **Options (Korean, 5지)**: Each option ends with "**해야 한다**"
- **Correct Answer**: Captures the author’s **main** argument/recommendation (central claim)
- **Distractors** (4): Supporting details, opposite claims, partial/side claims, or unrelated policies

### Content Generation Guidelines
- Build a coherent argument with explicit logical connectors.
- Make the main claim recoverable via synthesis of Problem→Analysis→Solution→Support.
- Use topics relevant to Korean high school students and society (education, community, environment, digital literacy, etc.).
- Avoid culturally niche knowledge that disadvantages EFL learners.

### Language-Use Rule (override if base differs)
- passage: **English only**
- question/explanation/options: **Korean only**

### Output Validation Rules
- "passage" must be 130–160 English words; contain a **clearly identifiable central claim**.
- "options" must be exactly 5 strings, each ending with "해야 한다".
- "correct_answer" must be an integer 1–5 (1-based index).
- "explanation" (Korean) must justify why the chosen option is the **main** claim (not just evidence/example), and briefly exclude the distractors.
- No markdown, no extra commentary — **return JSON only**.
- Do not include extra fields beyond the schema.

**Required JSON Output Format:**
{
  "question": "다음 글에서 필자가 주장하는 바로 가장 적절한 것은?",
  "passage": "[130–160 word argumentative text in English]",
  "options": ["주장1해야 한다", "주장2해야 한다", "주장3해야 한다", "주장4해야 한다", "주장5해야 한다"],
  "correct_answer": 1,
  "explanation": "[Korean explanation of the central claim vs. supports/opposites/partials]"
}

Self-check before returning:
- [ ] JSON 파싱 가능 여부
- [ ] "passage" 130–160 words / English only
- [ ] 옵션 5개, 모두 "해야 한다"로 끝나는지
- [ ] correct_answer ∈ {1,2,3,4,5} (1-based)
- [ ] question/explanation: Korean only
- [ ] 중앙 주장과 근거/예시/반론 구분이 명확한지
"""

SPEC = {
    "type": "reading_argument_identification",
    "components": [
        "question",
        "passage",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count_passage": [130, 160],
        "korean_suffix_required": "해야 한다",
        "answer_indexing": "1-based",
        "require_argument_markers": True,
        "central_claim_detectable": True
    },
    "title": "읽기 20번 - 주장 파악"
}
