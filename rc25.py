"""
RC25 — Reading 25: Chart Analysis (도표 분석)

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC25 유형(도표 분석)에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""
Create a CSAT Reading Item 25 (Chart Analysis) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY
### Assessment Objective
- **Core Skill**: 도표 데이터와 텍스트 진술 간 일치성 판단 능력 측정
- **Processing Pattern**: 도표 정보 추출 → 각 선택지별 데이터 확인 → 불일치 요소 탐지
- **Evaluation Focus**: 시각적 데이터와 언어적 진술 간의 정확한 대조 분석 능력

### Discourse Structure
- **Pattern**: 상황 설명(그래프/도표 소개) → ①~⑤ 진술을 하나의 단락 안에서 자연스럽게 제시 → 각 진술이 도표와 비교 가능해야 함
- **Flow**: 그래프 개요 설명 → 연도/항목/지역 비교 → ①~⑤ 진술 → 그 중 정확히 하나는 도표와 모순
- **Natural Embedding Rule (CRITICAL)**:
  - ①~⑤는 **각 진술의 문장 맨 앞에서 시작**해야 한다. 형식은 정확히 `①␠문장... ②␠문장... ③␠문장... ④␠문장... ⑤␠문장...`이며,
  - **숫자 뒤에 공백 1칸**을 둔다. **문장 끝에 `... ①.`처럼 달아붙이는 형식 금지**.

- **Number Placement (CRITICAL)**: Each numbered statement **must begin** with its circled numeral followed by a single space. 
  - Pattern must match: `(^|[.!?]\s)①\s.+?[.!?]\s②\s.+?[.!?]\s③\s.+?[.!?]\s④\s.+?[.!?]\s⑤\s.+?$` (DOTALL).
  - If any numeral appears **at the end of a sentence or clause** (e.g., `…, 20% ①.`), **REGENERATE**.
  - **목록·줄바꿈 금지**: ①~⑤ 앞뒤로 줄바꿈 없이, 문장 흐름 속에 쉼표·세미콜론·접속사(and, while, whereas 등)로 연결한다.
  - 각 번호 문장의 길이는 **18–25 words** 범위 안에서 균형 있게 작성한다.
  - 한 문장에서는 **최대 2개 집단(국가/지역/연도/범주)까지만** 언급한다 (인지부하 방지).
  - **Numbering Enforcement**: The passage MUST embed **all five circled numerals** exactly once and **in order** — `① ② ③ ④ ⑤` — **inline** within the same paragraph. **Do NOT** omit, reorder, repeat, or place them on separate lines. If this fails, **REGENERATE**.
  ✅ DO: “① In 2018, Country A … . ② By 2020, Country B … . ③ In 2022, … . ④ Across all … . ⑤ However, … .”
  ❌ DON’T: “… 20% ①. … unchanged ②.”  (문장 끝에 번호 금지)

### Language Specifications
- **Passage Length**: 115–135 words (영문 전용, 번호 포함)
- **Sentence Complexity**: Complex, with comparative/descriptive structures (~2.2 clauses/sentence)
- **Vocabulary Level**: Statistical, comparative, and data-related vocabulary.

### Variety of Expression (MANDATORY)
- 다섯 문장(①~⑤) 중 **최소 두 문장**은 **구체적 수치(%)**를 직접 포함.
- **최소 한 문장**은 **배수/비율 관계**(e.g., “twice”, “three times”)를 포함(근사 금지, chart_data로 정확히 뒷받침).
- **최소 한 문장**은 **변화 없음/유지** 유형을 포함(예: remained unchanged, remained constant, held steady).
- **최소 한 문장**은 **순위/최고·최저** 언급을 포함(예: highest, lowest).

### Question Format Requirements
- **Stem (Korean)**: "다음 도표의 내용과 일치하지 <u>않는</u> 것은?"
- **Options**: ["①", "②", "③", "④", "⑤"] (번호만)
- **Correct Answer**: 문자열 **"1"–"5"** 중 하나 (string)  ← RC25 스펙과 일치
- **Explanation (Korean)**: ①~⑤ 각각에 대해 도표 수치·추세 근거로 일치/불일치 판정. 정답(오답 진술)이 왜 틀렸는지 **구체 수치/증감 방향/배수 관계**를 인용하여 설명.

### Chart Data Schema (STRICT)
You MUST produce `chart_data` in one of the following STRICT schemas. 
Do NOT mix schemas. Do NOT add extra fields.

(1) GRAPH schema (bar | line | stacked_bar | pie)
- Structure:
  {
    "type": "bar" | "line" | "stacked_bar" | "pie",
    "title": string,
    "labels": string[],
    "datasets": [
      { "label": string, "data": number[] }
    ]
  }

(2) TABLE schema (table) — use ONLY if necessary
- Structure:
  {
    "type": "table",
    "title": string,
    "columns": string[],
    "rows": Array<[string, number, number]>
  }

### Graph Complexity Guardrails (CRITICAL)
- **Type**: Use **bar** or **line** (pie 금지) **unless** the task is share-of-whole only.
- **Labels**: **≥ 4** categories (e.g., age groups, activities, years).
- **Datasets**: **≥ 2** series (e.g., regions/genders/years). Single-series charts **금지**.
- **Comparative Structure**: Ensure **at least one rank inversion across series** (there exist labels A,B where Series1(A)>Series1(B) but Series2(A)<Series2(B)).
- Include **both within-series rankings** (highest/lowest inside one group) **and cross-series comparisons** (Group X vs Group Y for the same label).
- If time-series, include **≥ 3 points** per series and **non-identical trends** across series (e.g., one increases while another decreases or stagnates).

### Output Schema Guardrails
- DO NOT output fields not listed in Output Format.
- "correct_answer" MUST be a **string** in {"1","2","3","4","5"}.
- "options" MUST be exactly ["①","②","③","④","⑤"].
- **Passage Compliance Check**: Before returning JSON, self-check that the passage **contains ①②③④⑤ in order in one paragraph**. If not, **regenerate**.
- **No extra fields** (e.g., no "rationale").

### Passage–Chart Consistency Rules
- The passage’s ①–⑤ statements MUST be evaluated strictly against `chart_data`.
- Exactly **4 statements match** `chart_data` and **1 contradicts**.
- Ratios/multiples (e.g., “twice”, “three times”) must be **exact** per `chart_data` (no rounding). If not exact, use comparative wording (“more than”, “less than”) instead.
- If a statement mentions **years/time** (e.g., “in 2022”, “from 2018 to 2022”, “remained unchanged”), the chart **labels must be years**; otherwise **regenerate**.

### Variation Rules
- Vary the opener sentence.
- Mix relation types across ①–⑤ (increase/decrease, highest/lowest, unchanged, ratio/multiple, ranking, threshold like “all above 20%”).

### Required JSON Output Format
{
  "question": "다음 도표의 내용과 일치하지 <u>않는</u> 것은?",
  "passage": "115–135-word English paragraph with overview + naturally embedded ①–⑤ statements (no line breaks, no bulleting).",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": "1",
  "explanation": "한국어 해설: 각 번호 진술의 사실 여부를 수치·추세 근거로 판정, 정답은 왜 틀렸는지 명시.",
  "chart_data": {
    "type": "...",
    "title": "...",
    "labels": [...],
    "datasets": [...]
  }
}
"""

SPEC = {
    "type": "chart_analysis_rc25",
    "components": [
        "question",
        "passage",
        "options",
        "correct_answer",
        "explanation",
        "chart_data"
    ],
    "processing_hints": {
        # Passage constraints
        "word_count_passage": [115, 135],
        "english_only_passage": True,
        "single_paragraph_required": True,
        "inline_numbering_required": True,            # ①~⑤ inline
        "numbering_order_regex": r"①.*?②.*?③.*?④.*?⑤",
        "each_numeral_once": True,
        "no_linebreak_near_numbers": True,
        "sentence_length_range_per_number": [18, 25], # per ①~⑤
        "max_entities_per_sentence": 2,               # groups/years/categories ≤ 2

        # Options & answer constraints
        "options_fixed": ["①","②","③","④","⑤"],
        "answer_indexing": "1-based",
        "answer_must_be_string_1_5": True,
        "explanation_language": "ko",

        # Content variety constraints
        "require_two_numeric_statements": True,       # at least 2 sentences contain explicit %
        "require_ratio_statement": True,              # e.g., twice, three times (exact)
        "require_unchanged_statement": True,          # remained unchanged / constant / held steady
        "require_rank_statement": True,               # highest/lowest

        # Chart constraints
        "chart_schema": "graph_or_table",
        "chart_types_allowed": ["bar", "line", "stacked_bar", "pie", "table"],
        "chart_min_datasets": 2,
        "chart_min_labels": 4,
        "time_series_min_points": 3,
        "require_rank_inversion": True,
        "prefer_bar_or_line": True,
        "disallow_pie_unless_share_only": True,

        # Consistency checks
        "require_one_false_statement": True,          # exactly one contradicts
        "regenerate_if_time_mention_without_year_axis": True,
        "no_extra_fields": True
    },
    "title": "읽기 25번 - 도표 분석",
    "special_features": ["chart_analysis", "rc25_fast_precheck_ready"]
}
