# app/prompts/items/rc18.py

"""
RC18 — Reading 18: Purpose Identification

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC18 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""
Create a CSAT Reading Item 18 (Purpose Identification) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Identifying the primary communicative purpose of a formal notice or announcement
- **Cognitive Process**: Analyze background situation → Trace cause and anticipated outcomes → Infer the writer’s main intent → Match with the most accurate purpose option
- **Difficulty Target**: 중상 (예상 정답률 81–95%, 변별도 0.1–0.2)

### Abstractness & Complexity Controls
- **Abstractness Level (1–9)**: 3
- **Syntactic Complexity Targets (optional)**:
  - avg_words_per_sentence: 18.8
  - avg_clauses_per_sentence: 2.3
  - subordination_ratio: 0.5
- **Vocabulary Profile (optional)**: CSAT+O3000

### Text Type & Structure
- **Format**: Official notice, public letter, or announcement
- **Structure Pattern (mandatory 5-step logic)**:
  A. 상황 설명 (Context Setup) →
  B. 원인 설명 (Cause/Reason) →
  C. 기대 내용 (Expected outcome/anticipation) →
  D. 결론 (Key decision/action) →
  E. 정서적 마무리 (Closure: thanks/request/next steps)

### Purpose Location Strategy (HARD)
- The **main communicative intent must become fully clear only in D–E** after A–C build-up.
- **Do NOT** reveal the final action/purpose in the **first sentence**. If violated, regenerate internally.

### Greeting & Closing (HARD)
- Passage MUST:
  1) Begin with exactly one of:
     - `Dear [Name],`
     - `To whom it may concern,`
  2) End with a formal closing:
     - `Sincerely,` (or `Regards,`, `Best regards,`) **followed by a sender name or department**.
- If greeting or closing is missing, **regenerate internally** and return only the final valid JSON.
- No informal greetings (e.g., “Hello,” “Hi,”).

### Language Specifications
- **Passage Length**: 120–150 words (English only)
- **Register**: Formal, institutional tone
- **Sentence Style**: Compound–complex preferred; align with syntactic targets
- **Key Language Features**:
  - Causal markers: “due to”, “as a result”, “because of”
  - Anticipatory phrasing: “many looked forward to”, “we had planned to”
  - Intent verbs (appear late): “announce”, “inform”, “notify”, “postpone”, “cancel”
  - Closure tone: “we regret…”, “we appreciate your understanding”, “thank you for your cooperation”
- **Vocabulary Profile**:
  "vocabulary_difficulty": "CSAT+O3000",
  "low_frequency_words": ["sponsor", "exhibit", "festival"]

### Question Format Requirements
- **Stem (Korean)**: "다음 글의 목적으로 가장 적절한 것은?"
- **Options (Korean, 5지)**:
  - Action-based 목적 표현, 모두 “~하려고”로 끝남
  - Include **1 correct** option reflecting the **D–E** purpose
  - Include **4 distractors**:
    1) early-context: A 또는 초반 정보에 근거한 오해 유도
    2) partial cause: B의 원인 정보만 확대 해석
    3) misinference: C의 기대를 목적과 혼동
    4) irrelevant: 문맥과 무관한 공공 목적
- **Correct Answer**:
  - Provide the **1-based index (1–5)** that matches the primary function stated/implicated in **D–E**.

### Output Validation Rules
- "passage" must be 120–150 English words (no Korean).
- "options" must be exactly 5 strings, each ending with "하려고".
- "correct_answer" must be an integer 1–5 (1-based index).
- "explanation" (Korean): D–E 구간의 핵심 의도 문장 근거 + A–C(원인/기대) 흐름 요약, 오답 배제 근거 포함.
- No markdown, no extra commentary — **return JSON only**.
- No extra fields beyond the schema.

**Required JSON Output Format:**
{
  "question": "다음 글의 목적으로 가장 적절한 것은?",
  "passage": "[120–150 word formal communication in English]",
  "options": ["목적1하려고", "목적2하려고", "목적3하려고", "목적4하려고", "목적5하려고"],
  "correct_answer": 1,
  "explanation": "[Korean rationale referencing D–E as the decisive purpose location]",
  "vocabulary_difficulty": "CSAT+O3000",
  "low_frequency_words": ["sponsor", "exhibit", "festival"]
}

Self-check before returning:
- [ ] JSON 파싱 가능 여부
- [ ] "passage" 120–150 words / English only
- [ ] options 5개, 모두 "하려고"로 끝나는지
- [ ] correct_answer ∈ {1,2,3,4,5} (1-based)
- [ ] question/explanation: Korean only
- [ ] 목적이 D–E에서 분명해지는지(초반 노출 금지)
- [ ] Distractors가 ‘주된 목적’과 구분되는지
"""

SPEC = {
    "type": "reading_purpose",
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
        "word_count_passage": [120, 150],
        "korean_suffix_required": "하려고",
        "answer_indexing": "1-based",
        "greeting_required": True,
        "closing_required": True,
        "purpose_late_enforcement": True
    },
    "title": "읽기 18번 - 목적 파악"
}
