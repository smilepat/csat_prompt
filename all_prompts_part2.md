# CSAT English Item Generation Prompts (Part 2)

> **NOTE**: 모든 문항에서 `correct_answer`는 **integer 1-5**로 통일됩니다.

---

## RC25 - 읽기 25번 (도표 분석)

```
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
  - ①~⑤는 **각 진술의 문장 맨 앞에서 시작**해야 한다.
  - **숫자 뒤에 공백 1칸**을 둔다. **문장 끝에 달아붙이는 형식 금지**.

### Language Specifications
- **Passage Length**: 115–135 words (영문 전용, 번호 포함)
- **Sentence Complexity**: Complex, with comparative/descriptive structures (~2.2 clauses/sentence)
- **Vocabulary Level**: Statistical, comparative, and data-related vocabulary.

### Vocabulary Profile
- "vocabulary_difficulty": "CSAT+O3000"
- "low_frequency_words": [] (도표 관련 통계 어휘 포함 시 기재)

### Variety of Expression (MANDATORY)
- 다섯 문장(①~⑤) 중 **최소 두 문장**은 **구체적 수치(%)**를 직접 포함.
- **최소 한 문장**은 **배수/비율 관계**(e.g., "twice", "three times")를 포함.
- **최소 한 문장**은 **변화 없음/유지** 유형을 포함(예: remained unchanged).
- **최소 한 문장**은 **순위/최고·최저** 언급을 포함(예: highest, lowest).

### Question Format Requirements
- **Stem (Korean)**: "다음 도표의 내용과 일치하지 <u>않는</u> 것은?"
- **Options**: ["①", "②", "③", "④", "⑤"] (번호만)
- **Correct Answer**: integer 1–5
- **Explanation (Korean)**: ①~⑤ 각각에 대해 도표 수치·추세 근거로 일치/불일치 판정.

### Chart Data Schema (STRICT)
{
  "type": "bar" | "line" | "stacked_bar" | "pie",
  "title": string,
  "labels": string[],
  "datasets": [
    { "label": string, "data": number[] }
  ]
}

### Required JSON Output Format
{
  "question": "다음 도표의 내용과 일치하지 <u>않는</u> 것은?",
  "passage": "115–135-word English paragraph with ①–⑤ statements.",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": 1,
  "explanation": "한국어 해설",
  "chart_data": {
    "type": "...",
    "title": "...",
    "labels": [...],
    "datasets": [...]
  },
  "vocabulary_difficulty": "CSAT+O3000",
  "low_frequency_words": []
}
```

---

## RC26 - 읽기 26번 (인물 정보 불일치)

```
Create a CSAT Reading Item 26 (Biographical Information Mismatch) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 인물 소개 텍스트와 선택지 간 사실 일치성 판단 능력 측정
- **Processing Pattern**: 텍스트 정보 추출 → 각 선택지별 사실 확인 → 불일치 요소 탐지
- **Evaluation Focus**: 인물 관련 사실 정보와 선택지 간의 정확한 대조 분석 능력

### Discourse Structure
- **Pattern**: 인물 소개 → 출생 정보 → 초기 경력 → 주요 업적 → 경력 발전 → 말년 활동 → 사망 정보 → 추가 성취
- **Flow**: 기본 정보 → 배경 → 시작점 → 전환점 → 전성기 → 후기 → 종료 → 부가 정보

### Language Specifications
- **Passage Length**: 130-150 words
- **Sentence Complexity**: Moderate, featuring chronological and descriptive sentences
- **Vocabulary Level**: Biographical and descriptive vocabulary
- **Reading Level**: Accessible narrative and expository style

### Vocabulary Profile
- "vocabulary_difficulty": "CSAT+O3000"
- "low_frequency_words": [] (인물 관련 전문 어휘 포함 시 기재)

### Question Format Requirements
- **Stem**: "{person_name_en}에 관한 다음 글의 내용과 일치하지 <u>않는</u> 것은?"
  - 인물명은 지문 표기의 영문 그대로 사용 (번역/음차 금지).
- **Options**: 5개 선택지 (모두 한국어). 구체적 사실을 진술하는 문장.
- **Correct Answer**: integer 1–5
- **불일치 선택지는 세부 정보 오류(연도, 장소, 기관명, 업적, 수상명 등)로 구성.**
- 나머지 4개는 본문과 정확히 일치.

**Required JSON Output Format:**
{
  "question": "{person_name_en}에 관한 다음 글의 내용과 일치하지 <u>않는</u> 것은?",
  "passage": "[Biographical text about a notable person in English]",
  "options": ["사실진술1", "사실진술2", "사실진술3", "사실진술4", "사실진술5"],
  "correct_answer": 1,
  "explanation": "[Korean explanation of the factual contradiction]",
  "vocabulary_difficulty": "CSAT+O3000",
  "low_frequency_words": []
}
```

---

## RC27 - 읽기 27번 (안내문 불일치)

```
Create a CSAT Reading Item 27 (Notice Mismatch) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 안내문 정보와 선택지 간 사실 일치성 판단 능력 측정
- **Processing Pattern**: 안내문 정보 추출 → 각 선택지별 사실 확인 → 불일치 요소 탐지
- **Evaluation Focus**: 공식 안내문과 선택지 간의 정확한 사실 대조 능력

### Discourse Structure
- **Pattern**: 제목/헤드라인 → 이벤트 소개 → 일정 정보 → 장소 정보 → 참가 조건 → 신청 방법 → 연락처 → 추가 안내

### Language Specifications
- **Passage Length**: 120–140 words
- **Sentence Complexity**: Simple to moderate
- **Vocabulary Level**: Informational/procedural vocabulary

### Vocabulary Profile
- "vocabulary_difficulty": "CSAT+O3000"
- "low_frequency_words": [] (행사/절차 관련 어휘 포함 시 기재)

### Formatting Instructions (ASCII-styled layout)
- Top divider line of "=" repeated at least 40 times
- EVENT TITLE in ALL CAPS
- Labeled sections: Title:, Date:, Location:, Eligibility:, Registration:, Fee:, Contact:, Note:
- Bottom divider line

### OUTPUT (STRICT)
{
  "question": "[이벤트 제목(영문)]에 관한 다음 안내문의 내용과 일치하지 <u>않는</u> 것은?",
  "passage": "[English ASCII-styled layout notice]",
  "options": ["Korean sentence 1", "Korean sentence 2", "Korean sentence 3", "Korean sentence 4", "Korean sentence 5"],
  "correct_answer": 1,
  "explanation": "[Korean explanation]",
  "vocabulary_difficulty": "CSAT+O3000",
  "low_frequency_words": []
}
```

---

## RC28 - 읽기 28번 (안내문 일치)

```
Create a CSAT Reading Item 28 (Notice Match) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 이벤트 안내문 정보와 선택지 간 사실 일치성 판단 능력 측정
- **Processing Pattern**: 안내문 정보 추출 → 각 선택지별 사실 확인 → 일치 요소 식별
- **Evaluation Focus**: 이벤트 안내문과 선택지 간의 정확한 사실 일치 능력

### Language Specifications
- **Passage Length**: 120–140 words
- **Register**: Neutral, factual
- **Style**: Informational notice with structured ASCII layout

### Vocabulary Profile
- "vocabulary_difficulty": "CSAT+O3000"
- "low_frequency_words": [] (행사/절차 관련 어휘 포함 시 기재)

### Passage Formatting Rules (STRICT)
- ASCII divider lines made of "=" at the top and bottom.
- Event title in ALL CAPS
- Labeled sections: Title:, Date:, Time:, Location:, Eligibility:, Registration:, Fee:, Program:, Benefits:, Contact:, Note:

### Question Format Requirements
- **Stem**: "[이벤트 제목(영문)]에 관한 다음 안내문의 내용과 일치하는 것은?"
- **Options**: Exactly 5 Korean sentences. Exactly 1 must match the passage.
- **Correct Answer**: integer 1–5

**Required JSON Output Format:**
{
  "question": "[Event Title]에 관한 다음 안내문의 내용과 일치하는 것은?",
  "passage": "[English ASCII notice layout]",
  "options": ["Korean sentence 1", "...", "...", "...", "..."],
  "correct_answer": 1,
  "explanation": "[Korean explanation]",
  "vocabulary_difficulty": "CSAT+O3000",
  "low_frequency_words": []
}
```

---

## RC29 - 읽기 29번 (어법 판단)

```
Create a CSAT Reading Item 29 (Grammar Judgment) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 문맥 속에서 문법 규칙의 올바른 적용 여부를 판단하는 능력 측정
- **Processing Pattern**: 문장 구조 분석 → 밑줄 친 부분의 문법적 역할 파악 → 관련 문법 규칙 적용 → 오류 식별

### Language Specifications
- **Passage Length**: 반드시 110~130 words
- **Sentence Complexity**: Complex (Avg. 2.3~2.5 clauses per sentence)
- **Vocabulary Level**: Academic and topic-specific vocabulary

### Vocabulary Profile
- "vocabulary_difficulty": "CSAT+O3000"
- "low_frequency_words": [] (학술 어휘 포함 시 기재)

### Content Generation Guidelines
- 지문에는 반드시 5개의 distinct grammar points 포함:
  1. 관계대명사/관계부사
  2. 동사 시제 또는 수일치
  3. 조동사 + 동사 원형/부정사
  4. 수동태
  5. 분사 또는 분사구문
- 각 밑줄 포인트는 **단일 단어** 또는 **짧은 어휘 단위(최대 2~3어)**
- 문법 포인트는 ①~⑤ 번호와 `<u>...</u>` 태그로 표시
- Format: "①<u>word_or_phrase</u>", "②<u>word_or_phrase</u>", ...

**Required JSON Output Format:**
{
  "question": "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?",
  "passage": "[110~130 words academic text with ① <u>...</u> through ⑤ <u>...</u> embedded]",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": 1,
  "explanation": "[Korean explanation of the grammar error]",
  "vocabulary_difficulty": "CSAT+O3000",
  "low_frequency_words": []
}
```

---

## RC30 - 읽기 30번 (어휘의 적절성 파악)

```
Create a CSAT Reading Item 30 (Vocabulary Judgment) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 글의 전체적인 논리 흐름 속에서 어휘의 문맥적 적절성을 판단하는 능력 측정
- **Processing Pattern**: 글의 주제와 문장 간 논리 관계 파악 → 밑줄 친 어휘의 의미와 문맥의 요구사항 비교 → 의미적으로 상충되는 어휘 식별

### Language Specifications
- **Passage Length**: 130-150 words
- **Sentence Complexity**: Complex, with dense logical relationships (Avg. 2.1-2.3 clauses per sentence)
- **Vocabulary Level**: Advanced academic and abstract vocabulary

### Vocabulary Profile
- "vocabulary_difficulty": "CSAT+O3000"
- "low_frequency_words": [] (밑줄 친 어휘 중 고급 어휘 기재)

### Content Generation Guidelines
- The error is often an antonym of the correct word
- 각 번호에 해당하는 어휘는 반드시 HTML 밑줄 태그(`<u>...</u>`)를 사용
- 예: ①<u>increase</u>, ②<u>reduce</u>, ...
- 지문 내 정확히 5개의 어휘가 ①~⑤ 번호와 함께 밑줄로 처리

**Required JSON Output Format:**
{
  "question": "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]",
  "passage": "[Academic text with ①<u>word1</u> ②<u>word2</u> ③<u>word3</u> ④<u>word4</u> ⑤<u>word5</u>]",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": 1,
  "explanation": "[Korean explanation of the vocabulary error]",
  "vocabulary_difficulty": "CSAT+O3000",
  "low_frequency_words": []
}
```

---

## RC31 - 읽기 31번 (빈칸 추론 - 단어/구)

```
Create a CSAT Reading Item 31 (Blank Inference - Word/Phrase) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 문맥을 통한 핵심 어휘/구 추론 능력 측정
- **Processing Pattern**: 문맥 분석 → 논리적 관계(인과, 대조 등) 파악 → 빈칸의 기능 확인 → 적절한 어휘/구 추론
- **Difficulty Target**: 중 수준 (예상 정답률 50–65%)

### Language Specifications
- **Passage Length**: 130–150 words
- **Sentence Complexity**: Complex, with dense logical relationships (Avg. 2.1–2.3 clauses per sentence)
- **Vocabulary Level**: Advanced academic and abstract vocabulary

### Vocabulary Profile
- "vocabulary_difficulty": "CSAT+O3000"
- "low_frequency_words": [] (지문 내 고급 어휘 기재)

### Content Generation Guidelines
- **The blank must be indicated ONLY by `_____` (five underscores).**
- **Do NOT use any HTML underline tags `<u>...</u>` anywhere in the passage.**
- Ensure exactly one blank in the passage.

**Required JSON Output Format:**
{
  "question": "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?",
  "passage": "[Academic text with _____ blank in English]",
  "options": ["word/phrase 1", "word/phrase 2", "word/phrase 3", "word/phrase 4", "word/phrase 5"],
  "correct_answer": 1,
  "explanation": "[Korean explanation of the logical completion]",
  "vocabulary_difficulty": "CSAT+O3000",
  "low_frequency_words": []
}
```

---

## RC32 - 읽기 32번 (빈칸 추론 - 구/절)

```
Create a CSAT Reading Item 32 (Blank Inference - Phrase/Clause) following these specifications.

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

### Vocabulary Profile
- "vocabulary_difficulty": "CSAT+AWL"
- "low_frequency_words": [] (AWL 어휘 최소 3개 기재)

### Language Specifications
- Passage Length: 130–150 words (MUST be enforced)
- Use `_____` for the blank.

### Question Format Requirements
- Stem: "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?"
- Options: 5 choices, ALL verb phrases (verb + object/complement)
  - At least one MUST contain passive voice.
  - At least one MUST contain present perfect.
  - At least one MUST contain a to-infinitive construction.

### OPTION TYPE RULES (ADVANCED - from rc322.py)
All five options MUST be **abstract conceptual clauses or abstract conceptual phrases**, not actions.

**Allowed:**
- abstract noun phrase (conceptual)
- that-clause expressing a principle (NOT a fact or example)
- conceptual to-infinitive clause (NOT purpose)
- participial conceptual clause (being shaped by ~ / having been shaped by ~)
- passive conceptual clause (are sustained by ~ / are structured by ~)

**Prohibited:**
- simple action verb phrases (e.g., "people choose to ~", "they fail to ~")
- policy recommendations (e.g., "society should ban ~")
- normative instructions (e.g., "we must promote ~")
- examples or concrete statements
- sentence fragments (e.g., "short-term benefits")

### REQUIRED GRAMMATICAL VARIETY (STRONG CONSTRAINT)
Across the 5 options, you MUST include EXACTLY:
- **1 passive conceptual clause**
- **1 present-perfect conceptual clause**
- **1 conceptual to-infinitive clause**
- Remaining 2 options MUST be either abstract noun phrases OR conceptual that-clauses

### LENGTH CONSTRAINT (MANDATORY)
Each option MUST be **9–15 words**.

**Required JSON Output Format:**
{
  "question": "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?",
  "passage": "[130–150 word academic passage with a single blank.]",
  "options": [
    "abstract conceptual phrase/clause option (9-15 words)",
    "abstract conceptual phrase/clause option (9-15 words)",
    "abstract conceptual phrase/clause option (9-15 words)",
    "abstract conceptual phrase/clause option (9-15 words)",
    "abstract conceptual phrase/clause option (9-15 words)"
  ],
  "correct_answer": 1,
  "explanation": "[한국어 해설: 정답 근거 및 오답 배제 이유]",
  "vocabulary_difficulty": "CSAT+AWL",
  "low_frequency_words": []
}
```

---

## RC33 - 읽기 33번 (빈칸 추론 - 구/절, 고난도)

```
Create a CSAT Reading Item 33 (Blank Inference - Phrase/Clause, High Difficulty) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Inference of logical paradox or hidden truth from a complex narrative context.
- **Cognitive Process**: Analyzing cause-and-effect relationships and sequences of events; identifying a point of logical divergence; deducing the narrative's underlying principle.
- **Difficulty Target**: 상 수준 (예상 정답률 25–35%, 변별도 0.3 이상)

### Abstractness & Complexity Controls
- **Abstractness Level (1–9)**: 9
- **Syntactic Complexity Targets**:
  - avg_words_per_sentence: 28–32
  - avg_clauses_per_sentence: 3.5–4.5
  - subordination_ratio: 0.5

### Vocabulary Profile
- "vocabulary_difficulty": "CSAT+AWL"
- "low_frequency_words": [] (AWL 어휘 최소 4개 기재)

### Language Specifications
- **Passage Length**: 130–150 words
- **Sentence Style**: Academic cohesion, with clear prose; complexity is achieved through nuanced phrasing and logical links
- Use `_____` (five underscores) to indicate the blank.

### Type-Specific Policy
- Passage should avoid excessive nominalization, favoring clear subject-verb structures
- The correct answer must follow a clear logical cause-and-effect or narrative progression

### Question Format Requirements
- **Stem**: "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은? [3점]"
- **Options**: 5개 선택지, 모두 고난도 논리적 구/절
- **Correct Answer**: The option that logically and coherently concludes the clear narrative progression.
- **Distractors Policy**: 정답과 반대되는 논리, 부분적으로 타당하나 전체 논리를 벗어난 내용, 지엽적 세부 정보에만 초점을 맞춘 내용

**Required JSON Output Format:**
{
  "question": "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은? [3점]",
  "passage": "[130–150 word academic passage in English with a single blank, composed of clear sentences with minimal nominalization.]",
  "options": ["sophisticated phrase/clause 1", "sophisticated phrase/clause 2", "sophisticated phrase/clause 3", "sophisticated phrase/clause 4", "sophisticated phrase/clause 5"],
  "correct_answer": 1,
  "explanation": "[한국어 해설: 정답 근거 및 오답 배제 이유]",
  "vocabulary_difficulty": "CSAT+AWL",
  "low_frequency_words": []
}
```

---

## RC34 - 읽기 34번 (빈칸 추론 - 주제문/술부)

```
Create a CSAT Reading Item 34 (Blank Inference - Topic Sentence Predicate) following these specifications:

## ABSOLUTE RULES (DO NOT VIOLATE)
1. The blank (_____) MUST appear **only in the very first sentence** of the passage.
   - The first sentence MUST begin with a clear subject (e.g., "Global cooperation," "Technological innovations," "Traditional practices"), followed by `_____`.
   - The blank must cover the **entire predicate** of the first sentence.
   - DO NOT place the blank in the middle or at the end of the passage.
   - If the blank is not in the first-sentence predicate, the output is INVALID.

2. Passage length MUST be between **130 and 150 words**.

3. Sentence complexity MUST match the following targets:
   - Average ≈ 21.9 words per sentence
   - Average ≈ 2.75 clauses per sentence
   - Subordination ratio ≈ 0.5 or higher
   - You MUST include complex sentences with relative clauses, subordinate clauses, or participial constructions.

4. Vocabulary MUST include several words from the **Academic Word List (AWL)**.
   - At least **3 AWL words** must appear.
   - If AWL words are missing, the output is INVALID.

### Vocabulary Profile
- "vocabulary_difficulty": "AWL"
- "low_frequency_words": [] (AWL 어휘 최소 3개 기재, 예: integrate, facilitate, exemplify)

## Discourse Structure
- First sentence: Subject + `_____` (general principle predicate)
- Body: Example 1 → Example 2 → Example 3 (all supporting the general principle)
- Final sentence: Reaffirmation of the principle, using AWL vocabulary.

## Question Format Requirements
- **Stem (Korean)**: "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은? [3점]"
- **Options**: 모든 선택지는 빈칸 앞부분에 제시된 주어 + (조동사)에 이어질 수 있는 완전한 술부(predicate)로 이루어져야 함.
- **Correct Answer**: 글 전체의 귀납적 결론을 가장 정확하게 서술하는 선택지
- **Distractors**: 일부 사례에만 적용되거나, 주된 논리와 상반되는 내용

**Required JSON Output Format:**
{
  "question": "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은? [3점]",
  "passage": "[130–150 word academic passage beginning with subject + _____.]",
  "options": ["predicate option 1", "predicate option 2", "predicate option 3", "predicate option 4", "predicate option 5"],
  "correct_answer": 1,
  "explanation": "[한국어 해설: 정답 근거 및 오답 배제 이유]",
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": ["integrate", "facilitate", "exemplify"]
}
```

---

## RC35 - 읽기 35번 (무관한 문장 찾기)

```
Create a CSAT Reading Item 35 (Irrelevant Sentence) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 글의 통일성을 해치는 문장 식별 능력 측정
- **Processing Pattern**: 주제 파악 → 각 문장의 관련성 평가 → 논리적 이탈 문장 식별

### Discourse Structure
- **Introductory Paragraph**: 반드시 **2~3절 이상으로 연결된 Complex sentence**로 주제 제시 (조건절, 인과절, 대조절 포함)
- **Main Passage (①~⑤)**:
  - ① 주제 관련 구체적 설명 또는 사례
  - ② 주제 확장/일반화
  - ③ 또는 ④: **무관 문장** (겉보기에 관련 있어 보이지만 실제 주제에서 벗어남)
  - 나머지 문장: 주제와 긴밀히 연결
  - ⑤ 결론 또는 주제 강화

### Language Specifications
- **Passage Length**: 120–140 words
- **Sentence Complexity**: 평균 2.2절 이상, 주제문은 반드시 복합문
- **Vocabulary Level**: Academic, expository style
- **Reading Style**: Argumentative or expository, high cohesion

### Vocabulary Profile
- "vocabulary_difficulty": "AWL"
- "low_frequency_words": [] (AWL 어휘 최소 2개 기재)

### Content Generation Guidelines
- 무관 문장은 **①~⑤ 중 하나**에만 배치해야 함.
- 무관 문장은 **겉보기에 주제와 관련 있어 보이지만**, 실제로는 논리적 초점을 흐리거나 다른 주제로 전환함.
  - ❌ 주제와 완전히 무관한 분야(예: 독서 지문에 운동 이야기) → 피하기
  - ✅ 주제와 부분적으로 연관 있으나, 중심 논리와 어긋나는 내용 (예: 독서의 가치 지문에 출판사의 마케팅 전략 언급)
- **각 문장은 반드시 같은 단락 안에서 공백으로만 구분되며, 절대 줄바꿈(\\n) 없이 연속해서 이어져야 함.**
- 번호는 **①, ②, ③, ④, ⑤** 순서대로 문장 앞에만 붙인다.

**Required JSON Output Format:**
{
  "question": "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?",
  "passage": "[Introductory complex sentence paragraph] ① ... ② ... ③ ... ④ ... ⑤ ...",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": 1,
  "explanation": "[Korean explanation of why the chosen sentence is irrelevant]",
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": ["collaboration", "innovation"]
}
```

---

## RC36 - 읽기 36번 (글의 순서 배열 - 기본)

```
Create a CSAT Reading Item 36 (Paragraph Ordering - Standard) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 논리적 글의 순서 파악 능력 측정
- **Processing Pattern**: 주어진 문단 분석 → 각 단락의 기능 파악(예시, 부연, 결론 등) → 논리적 연결(대명사, 연결어) 추적 → 최적 배열 도출
- **Difficulty Target**: 중 수준 (예상 정답률 55–70%)

### Discourse Structure
- **Pattern**: 주어진 도입 문단(박스) → 순서가 섞인 (A), (B), (C) 단락
- **Flow**: 고정된 시작(원칙/개념 제시) → 세 개의 단락을 논리적 순서(예: 일반→구체, 원인→결과)로 배열
- **Key Positioning**: 도입 문단이 전체의 맥락을 설정하고, 나머지 세 단락은 대명사, 지시어, 연결어 등을 통해 논리적 순서를 추론해야 함

### Language Specifications
- **Passage Length**: 130-150 words (total across all paragraphs)
- **Sentence Complexity**: Moderate to complex, with explicit logical connectors (pronouns, discourse markers) to signal paragraph order. (Avg. 2.0-2.2 clauses per sentence)
- **Vocabulary Level**: Academic and transitional vocabulary
- **Reading Level**: Academic expository or argumentative style

### Vocabulary Profile
- "vocabulary_difficulty": "AWL"
- "low_frequency_words": [] (담화 표지어 및 학술 어휘 기재)

### Content Type Guidelines (RC36 Specific)
- **주제 유형**: 학술적/이론적 개념 설명 (심리학, 사회학, 교육학 등)
- **연결 방식**: 개념 정의 → 특징 설명 → 적용/예시
- **핵심 담화 표지**: This, These, Such, For example, In other words, Therefore

**Required JSON Output Format:**
{
  "question": "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
  "intro_paragraph": "[Introductory paragraph in a box - sets up the main concept]",
  "passage_parts": {
    "(A)": "[Paragraph A content]",
    "(B)": "[Paragraph B content]",
    "(C)": "[Paragraph C content]"
  },
  "options": ["(A)-(C)-(B)", "(B)-(A)-(C)", "(B)-(C)-(A)", "(C)-(A)-(B)", "(C)-(B)-(A)"],
  "correct_answer": 1,
  "explanation": "[Korean explanation of the logical order]",
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": []
}
```

---

## RC37 - 읽기 37번 (글의 순서 배열 - 고난도)

```
Create a CSAT Reading Item 37 (Paragraph Ordering - Advanced) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 논리적 글의 순서 파악 능력 측정 (고난도)
- **Processing Pattern**: 주어진 문단 분석 → 각 단락의 기능 파악(예시, 부연, 결론 등) → 논리적 연결(대명사, 연결어) 추적 → 최적 배열 도출
- **Difficulty Target**: 상 수준 (예상 정답률 35–50%, 3점 문항)

### Discourse Structure
- **Pattern**: 주어진 도입 문단(박스) → 순서가 섞인 (A), (B), (C) 단락
- **Flow**: 고정된 시작(현상 제시) → 세 개의 단락을 논리적 순서(예: 원인→실험→결과, 가설→검증→결론)로 배열
- **Key Positioning**: 도입 문단이 전체의 맥락을 설정하고, 나머지 세 단락은 대명사, 지시어, 연결어 등을 통해 논리적 순서를 추론해야 함

### Language Specifications
- **Passage Length**: 130-150 words (total across all paragraphs)
- **Sentence Complexity**: Moderate to complex, with explicit logical connectors (pronouns, discourse markers) to signal paragraph order. (Avg. 2.0-2.2 clauses per sentence)
- **Vocabulary Level**: Academic and transitional vocabulary
- **Reading Level**: Academic expository or argumentative style

### Vocabulary Profile
- "vocabulary_difficulty": "AWL"
- "low_frequency_words": [] (담화 표지어 및 학술 어휘 기재)

### Content Type Guidelines (RC37 Specific - Differentiator from RC36)
- **주제 유형**: 과학적/실험적 주제 (가설 검증, 연구 결과 해석)
- **연결 방식**: 현상 관찰 → 원인 분석/실험 설계 → 결과 도출
- **핵심 담화 표지**: However, As a result, Consequently, This finding, The results showed
- **난이도 차별화**:
  - 더 긴 문장 구조
  - 더 추상적인 개념
  - 대명사 지시 대상이 더 복잡함

**Required JSON Output Format:**
{
  "question": "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은? [3점]",
  "intro_paragraph": "[Introductory paragraph in a box - presents a phenomenon or research question]",
  "passage_parts": {
    "(A)": "[Paragraph A content]",
    "(B)": "[Paragraph B content]",
    "(C)": "[Paragraph C content]"
  },
  "options": ["(A)-(C)-(B)", "(B)-(A)-(C)", "(B)-(C)-(A)", "(C)-(A)-(B)", "(C)-(B)-(A)"],
  "correct_answer": 1,
  "explanation": "[Korean explanation of the logical order - must reference specific discourse markers and pronoun references]",
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": []
}
```

---

## RC38 - 읽기 38번 (문장 위치 추론 - 기본)

```
Create a CSAT Reading Item 38 (Sentence Insertion - Standard) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 주어진 문장의 적절한 삽입 위치 파악 능력 측정
- **Processing Pattern**: 주어진 문장 분석 → 글의 논리적 흐름 파악 → 각 삽입 위치별 적합성 검토 → 최적 위치 선택
- **Difficulty Target**: 중 수준 (예상 정답률 55–70%)

### Discourse Structure
- **Pattern**: 주어진 문장(박스) → 5개의 삽입 위치가 표시된 본문
- **Flow**: 독립적 문장 → 삽입 위치 ① → 문단1 → 삽입 위치 ② → 문단2 → 삽입 위치 ③ → 문단3 → 삽입 위치 ④ → 문단4 → 삽입 위치 ⑤
- **Key Positioning**: 주어진 문장이 글의 논리적 흐름에 가장 자연스럽게 연결되는 위치를 찾아야 함

### Language Specifications
- **Passage Length**: 120-140 words
- **Sentence Complexity**: Moderate to complex, with strong logical cohesion that creates a single correct insertion point. (Avg. 2.0+ clauses per sentence)
- **Vocabulary Level**: Academic vocabulary with an emphasis on discourse markers and cohesive devices
- **Reading Level**: Academic expository or argumentative style

### Vocabulary Profile
- "vocabulary_difficulty": "AWL"
- "low_frequency_words": [] (담화 표지어 및 학술 어휘 기재)

### Content Generation Guidelines (RC38 Specific)
- **주제 유형**: 일반적인 설명문/논설문
- **주어진 문장 유형**: 예시, 부연 설명, 대조적 진술
- **연결 단서**: This, These, However, For example, Such + N
- The passage must include five insertion points marked exactly as **( ① )**, **( ② )**, **( ③ )**, **( ④ )**, **( ⑤ )**.
- The given sentence must fit naturally into only one of these points.
- Do not use alternative markers like (1) or [1].

**Required JSON Output Format:**
{
  "question": "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?",
  "given_sentence": "[Independent sentence to be inserted - contains clear cohesive devices]",
  "passage": "[Text with ( ① ) ( ② ) ( ③ ) ( ④ ) ( ⑤ ) insertion points in English]",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": 1,
  "explanation": "[Korean explanation of the logical insertion point - must reference specific cohesive devices]",
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": []
}
```

---

## RC39 - 읽기 39번 (문장 위치 추론 - 고난도)

```
Create a CSAT Reading Item 39 (Sentence Insertion - Advanced) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 주어진 문장의 적절한 삽입 위치 파악 능력 측정 (고난도)
- **Processing Pattern**: 주어진 문장 분석 → 글의 논리적 흐름 파악 → 각 삽입 위치별 적합성 검토 → 최적 위치 선택
- **Difficulty Target**: 상 수준 (예상 정답률 35–50%, 3점 문항)

### Discourse Structure
- **Pattern**: 주어진 문장(박스) → 5개의 삽입 위치가 표시된 본문
- **Flow**: 복잡한 논리 구조 → 삽입 위치 판단이 더 까다로움

### Language Specifications
- **Passage Length**: 120-140 words
- **Sentence Complexity**: Complex, with subtle logical connections (Avg. 2.2+ clauses per sentence)
- **Vocabulary Level**: Advanced academic vocabulary
- **Reading Level**: High academic complexity

### Vocabulary Profile
- "vocabulary_difficulty": "AWL"
- "low_frequency_words": [] (고급 학술 어휘 기재)

### Content Generation Guidelines (RC39 Specific - Differentiator from RC38)
- **주제 유형**: 추상적/철학적 개념, 복잡한 인과관계
- **주어진 문장 유형**: 역접, 논리적 귀결, 핵심 주장
- **연결 단서**: Nevertheless, In contrast, As a consequence, This paradox
- **난이도 차별화**:
  - 주어진 문장의 연결 단서가 더 미묘함
  - 여러 위치가 부분적으로 가능해 보이나 하나만 완벽함
  - 대명사/지시어의 지시 대상 파악이 더 복잡함
- The passage must include five insertion points marked exactly as **( ① )**, **( ② )**, **( ③ )**, **( ④ )**, **( ⑤ )** (with parentheses and spacing).
- The given sentence must fit naturally into only one of these points.

**Required JSON Output Format:**
{
  "question": "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은? [3점]",
  "given_sentence": "[Complex sentence with subtle cohesive devices]",
  "passage": "[Text with ( ① ) ( ② ) ( ③ ) ( ④ ) ( ⑤ ) insertion points in English]",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": 1,
  "explanation": "[Korean explanation - must explain why other positions are partially plausible but incorrect]",
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": []
}
```

---

## RC40 - 읽기 40번 (요약문 완성)

```
Create a CSAT Reading Item 40 (Summary Completion) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 글의 핵심 내용을 파악하여 영어 요약문의 두 빈칸을 완성하는 능력 측정
- **Processing Pattern**: 글 전체 내용 파악 → 핵심 개념과 그 관계 추출 → 요약문 구조 분석 → (A), (B) 빈칸에 적절한 영어 표현 추론
- **Evaluation Focus**: 글 전체를 조직하는 두 개념의 **논리적 관계(대비, 인과, 메커니즘–결과, 조건–결과 등)**를 정확히 요약하는 능력

### Discourse Structure
- **Pattern**: 복잡한 개념 설명 → 구체적 사례/메커니즘 → 결과/효과 → 종합적 의미
- **Flow**: 현상 소개 → 세부 설명 → 작동 원리 → 영향/결과 → 전체적 함의
- **Key Positioning**: (A), (B)는 반드시 글 전체의 **두 축**이어야 하며, 단순 속성 나열이나 단선적 인과만으로는 부족함

### Language Specifications
- **Passage Length**: The passage must consist of **9–11 sentences**.
  - Each sentence should be **information-dense and 18–22 words long**.
  - Overall passage length: approximately **150–170 words**.
  - Avoid producing fewer than 9 sentences or more than 11 sentences.
- **Sentence Complexity**: 복잡하고 정보 밀도가 높을 것
- **Vocabulary Level**: 학술적이고 추상적인 어휘 포함
- **Reading Level**: 고난도 종합 추론 요구

### Vocabulary Profile
- "vocabulary_difficulty": "AWL"
- "low_frequency_words": [] (AWL 어휘 최소 3개 기재)

### Summary Template Structure
- One complete English sentence summarizing the passage
- (A), (B)는 <u>    (A)    </u>, <u>    (B)    </u>로 표기
- 두 개념의 **관계나 대비**가 반드시 드러나야 함 (단순 열거 금지)
- (A) and (B) must represent the two core concepts that organize the entire passage.
- The blanks (A) and (B) must be placed in positions where they share the same grammatical category (e.g., both nouns, both verbs, both adjectives).

### STRICT LENGTH & COMPLEXITY REQUIREMENTS
- The summary template must always contain **at least three clauses** (one main clause + two subordinate clauses).
- The template must include **at least two different subordinating connectors** (e.g., although, because, while, if, what, when, even though, unless).
- Sentence length must be **25–35 words**.
- **Avoid noun-only templates whenever possible.** At least half of all generated items must use **verb-verb** or **adjective-adjective** structures.

### Option Format
- All options must follow the format **"(A): word - (B): word"**.
- Each option must be a **single English word only** (no multi-word phrases).
- (A) and (B) must share the same grammatical category, consistent with the Summary Template.
- Permitted categories: Verb-Verb, Adjective-Adjective, Noun-Noun
- Distractors must be partially plausible but ultimately fail to capture the passage's overall meaning.
- At least one distractor should have (A) correct but (B) incorrect, and another should have (B) correct but (A) incorrect.

**Required JSON Output Format:**
{
  "question": "다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은? [3점]",
  "passage": "[150-170 word academic passage, 9-11 sentences]",
  "summary_template": "[25-35 word summary with <u>    (A)    </u> and <u>    (B)    </u> blanks, containing 3+ clauses]",
  "options": [
    "(A): word - (B): word",
    "(A): word - (B): word",
    "(A): word - (B): word",
    "(A): word - (B): word",
    "(A): word - (B): word"
  ],
  "correct_answer": 1,
  "explanation": "[Korean explanation - must explain the relationship between (A) and (B)]",
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": []
}
```

---

## RC41_42 - 읽기 41-42번 (장문 독해 세트)

```
Create a CSAT Reading Set for Items 41–42 (Long Reading Set) by **MINIMALLY EDITING** the provided passage, then producing two questions: **Q41 (Title)** and **Q42 (Vocabulary Appropriateness)**.

## ITEM CHARACTERISTICS & METHODOLOGY
### Assessment Objectives
- **Q41 (Title)**: Inferring the most appropriate **title** that synthesizes the passage's central idea.
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

### Vocabulary Profile
- "vocabulary_difficulty": "AWL"
- "low_frequency_words": [] (밑줄 친 어휘 중 고급 어휘 기재)

### Length & Language
- Passage: **English only**; keep overall length close to original (**±10%**).
- Questions & explanations: **Korean**.

## QUESTION SPECIFICATIONS
### Q41 — Title Inference
- **Stem (Korean)**: "윗글의 제목으로 가장 적절한 것은?"
- **Options (English, 5지)**:
  - Write exactly **5 English title statements**, **without numbering or bullets**.
  - Each option should be concise, **5–10 words**.
  - The **correct option** must be an **abstract noun phrase** or include nominal endings such as **-ing / -ion / -ity / -ness**.
- **Correct Answer Rule**: integer 1–5

### Q42 — Vocabulary Appropriateness
- **Stem (Korean)**: "밑줄 친 (a)~(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]"
- **Options (fixed)**: exactly `["(a)", "(b)", "(c)", "(d)", "(e)"]`.
- **Correct Answer Rule**: integer 1–5
- **Explanation (Korean)**: Explicitly justify **WHY** the chosen underlined word is a misfit in context, mentioning the relevant sentence/discourse role mismatch.

## REQUIRED JSON OUTPUT FORMAT
{
  "set_instruction": "[41~42] 다음 글을 읽고, 물음에 답하시오.",
  "passage": "[Edited passage with (a) <u>...</u> ... (e) <u>...</u>, split into ≥2 paragraphs with blank lines.]",
  "questions": [
    {
      "question_number": 41,
      "question": "윗글의 제목으로 가장 적절한 것은?",
      "options": ["Title 1", "Title 2", "Title 3", "Title 4", "Title 5"],
      "correct_answer": 1,
      "explanation": "[한국어 해설: 제목 선택 근거]"
    },
    {
      "question_number": 42,
      "question": "밑줄 친 (a)~(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]",
      "options": ["(a)", "(b)", "(c)", "(d)", "(e)"],
      "correct_answer": 1,
      "explanation": "[한국어 해설: 선택한 밑줄 어휘가 왜 부적절한지, 해당 문장/담화 기능과의 불일치 근거]"
    }
  ],
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": []
}

## FINAL SELF-CHECK (REJECT INTERNALLY IF ANY FAILS)
- Exactly 5 matches of the pattern for markers/underlines.
- Each underline is **one** word only.
- Markers spread across **≥ 2** paragraphs; **no paragraph** contains **3 or more** markers.
- Exactly **one** misfit underlined word; **four** appropriate.
- Q41 options = 5 English titles; Q42 options fixed.
- Both `"correct_answer"` fields are integers 1–5.
- Output is valid JSON; no extra commentary.
```

---

## RC43_45 - 읽기 43-45번 (장문 독해 - 복합 유형)

```
Create a CSAT Reading Item 43–45 (Long Reading Set) in perfect JSON format.

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

### Vocabulary Profile
- "vocabulary_difficulty": "AWL"
- "low_frequency_words": [] (C1 레벨 어휘 기재)

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
  ],
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": []
}

### FINAL SELF-CHECK
- Exactly 5 pronouns labeled (a)–(e), label before pronoun.
- At least one objective case.
- 4 map to Person A, 1 to Person B (randomized label).
- Each antecedent clear and local.
- Paragraphs 95–115 words each.
- All correct_answer fields are integers 1–5.
- JSON valid.
```

---

# 개선 요약

본 문서에 반영된 개선사항:

1. **`correct_answer` 타입 통일**: 모든 문항에서 `integer 1-5`로 통일
2. **RC36/RC37 차별화**:
   - RC36: 기본 난이도, 학술적/이론적 개념 설명, 개념-특징-적용 구조
   - RC37: 고난도(3점), 과학적/실험적 주제, 가설-검증-결론 구조
3. **RC38/RC39 차별화**:
   - RC38: 기본 난이도, 일반적 설명문, 명확한 연결 단서
   - RC39: 고난도(3점), 추상적 개념, 미묘한 연결 단서
4. **Vocabulary 필드 추가**: 모든 문항에 `vocabulary_difficulty`, `low_frequency_words` 필드 추가
5. **RC32 고급 버전 반영**: `rc322.py`의 상세 규칙(추상적 구/절, 문법 다양성, 길이 제약) 통합

---

# 끝
