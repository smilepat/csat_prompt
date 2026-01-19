# CSAT English Item Generation Prompts (Part 2)

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

### Variety of Expression (MANDATORY)
- 다섯 문장(①~⑤) 중 **최소 두 문장**은 **구체적 수치(%)**를 직접 포함.
- **최소 한 문장**은 **배수/비율 관계**(e.g., "twice", "three times")를 포함.
- **최소 한 문장**은 **변화 없음/유지** 유형을 포함(예: remained unchanged).
- **최소 한 문장**은 **순위/최고·최저** 언급을 포함(예: highest, lowest).

### Question Format Requirements
- **Stem (Korean)**: "다음 도표의 내용과 일치하지 <u>않는</u> 것은?"
- **Options**: ["①", "②", "③", "④", "⑤"] (번호만)
- **Correct Answer**: 문자열 **"1"–"5"** 중 하나 (string)
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
  "correct_answer": "1",
  "explanation": "한국어 해설",
  "chart_data": {
    "type": "...",
    "title": "...",
    "labels": [...],
    "datasets": [...]
  }
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

### Question Format Requirements
- **Stem**: "{person_name_en}에 관한 다음 글의 내용과 일치하지 <u>않는</u> 것은?"
  - 인물명은 지문 표기의 영문 그대로 사용 (번역/음차 금지).
- **Options**: 5개 선택지 (모두 한국어). 구체적 사실을 진술하는 문장.
- **불일치 선택지는 세부 정보 오류(연도, 장소, 기관명, 업적, 수상명 등)로 구성.**
- 나머지 4개는 본문과 정확히 일치.

**Required JSON Output Format:**
{
  "question": "{person_name_en}에 관한 다음 글의 내용과 일치하지 <u>않는</u> 것은?",
  "passage": "[Biographical text about a notable person in English]",
  "options": ["사실진술1", "사실진술2", "사실진술3", "사실진술4", "사실진술5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the factual contradiction]"
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
  "correct_answer": [1-5 integer],
  "explanation": "[Korean explanation]"
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

### Passage Formatting Rules (STRICT)
- ASCII divider lines made of "=" at the top and bottom.
- Event title in ALL CAPS
- Labeled sections: Title:, Date:, Time:, Location:, Eligibility:, Registration:, Fee:, Program:, Benefits:, Contact:, Note:

### Question Format Requirements
- **Stem**: "[이벤트 제목(영문)]에 관한 다음 안내문의 내용과 일치하는 것은?"
- **Options**: Exactly 5 Korean sentences. Exactly 1 must match the passage.
- **Correct Answer**: An integer (1–5)

**Required JSON Output Format:**
{
  "question": "[Event Title]에 관한 다음 안내문의 내용과 일치하는 것은?",
  "passage": "[English ASCII notice layout]",
  "options": ["Korean sentence 1", "...", "...", "...", "..."],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation]"
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
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the grammar error]"
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
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the vocabulary error]"
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

### Language Specifications
- **Passage Length**: 130–150 words
- **Sentence Complexity**: Complex, with dense logical relationships (Avg. 2.1–2.3 clauses per sentence)
- **Vocabulary Level**: Advanced academic and abstract vocabulary

### Content Generation Guidelines
- **The blank must be indicated ONLY by `_____` (five underscores).**
- **Do NOT use any HTML underline tags `<u>...</u>` anywhere in the passage.**
- Ensure exactly one blank in the passage.

**Required JSON Output Format:**
{
  "question": "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?",
  "passage": "[Academic text with _____ blank in English]",
  "options": ["word/phrase 1", "word/phrase 2", "word/phrase 3", "word/phrase 4", "word/phrase 5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the logical completion]"
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
- **Abstractness Level (1–9)**: MUST be 8
- **Syntactic Complexity Targets**:
  - Each sentence MUST average around 19 words.
  - Each sentence MUST contain about 2.2 clauses.
  - Subordination ratio MUST be ~0.4.
- **Vocabulary Profile**: MUST use CSAT+AWL vocabulary.

### Language Specifications
- Passage Length: 130–150 words (MUST be enforced)
- Use `_____` for the blank.

### Question Format Requirements
- Stem: "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?"
- Options: 5 choices, ALL verb phrases (verb + object/complement)
  - At least one MUST contain passive voice.
  - At least one MUST contain present perfect.
  - At least one MUST contain a to-infinitive construction.

**Required JSON Output Format:**
{
  "question": "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?",
  "passage": "[130–150 word academic passage with a single blank.]",
  "options": [
    "verb phrase option",
    "verb phrase option",
    "verb phrase option",
    "verb phrase option",
    "verb phrase option"
  ],
  "correct_answer": [1-5],
  "explanation": "[한국어 해설: 정답 근거 및 오답 배제 이유]"
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
- **Difficulty Target**: 중 수준 (예상 정답률 35.7%, 변별도 0.3)

### Abstractness & Complexity Controls
- **Abstractness Level (1–9)**: 9
- **Syntactic Complexity Targets (optional)**:
  - avg_words_per_sentence: 32.25
  - avg_clauses_per_sentence: 4.25
  - subordination_ratio: 0.5

### Language Specifications
- **Passage Length**: 130–150 words
- **Sentence Style**: Academic cohesion, with clear prose
- Use `_____` (five underscores) to indicate the blank.

### Question Format Requirements
- **Stem**: "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은? [3점]"
- **Options**: 5개 선택지, 모두 고난도 논리적 구/절
- **Correct Answer**: The option that logically and coherently concludes the clear narrative progression.

**Required JSON Output Format:**
{
  "question": "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은? [3점]",
  "passage": "[130–150 word academic passage in English with a single blank.]",
  "options": ["sophisticated phrase/clause 1", "sophisticated phrase/clause 2", "sophisticated phrase/clause 3", "sophisticated phrase/clause 4", "sophisticated phrase/clause 5"],
  "correct_answer": [1-5],
  "explanation": "[한국어 해설: 정답 근거 및 오답 배제 이유]"
}
```

---

## RC34 - 읽기 34번 (빈칸 추론 - 주제문/술부)

```
Create a CSAT Reading Item 34 (Blank Inference - Topic Sentence Predicate) following these specifications:

## ABSOLUTE RULES (DO NOT VIOLATE)
1. The blank (_____) MUST appear **only in the very first sentence** of the passage.
   - The first sentence MUST begin with a clear subject, followed by `_____`.
   - The blank must cover the **entire predicate** of the first sentence.
   - DO NOT place the blank in the middle or at the end of the passage.

2. Passage length MUST be between **130 and 150 words**.

3. Sentence complexity MUST match the following targets:
   - Average ≈ 21.9 words per sentence
   - Average ≈ 2.75 clauses per sentence
   - Subordination ratio ≈ 0.5 or higher

4. Vocabulary MUST include several words from the **Academic Word List (AWL)**.
   - At least **3 AWL words** must appear.

### Vocabulary Profile
"vocabulary_difficulty": "AWL"

## Discourse Structure
- First sentence: Subject + `_____` (general principle predicate)
- Body: Example 1 → Example 2 → Example 3 (all supporting the general principle)
- Final sentence: Reaffirmation of the principle, using AWL vocabulary.

## Question Format Requirements
- **Stem (Korean)**: "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은? [3점]"
- **Options**: 모든 선택지는 빈칸 앞부분에 제시된 주어에 이어질 수 있는 완전한 술부(predicate)

**Required JSON Output Format:**
{
  "question": "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은? [3점]",
  "passage": "[130–150 word academic passage beginning with subject + _____.]",
  "options": ["...", "...", "...", "...", "..."],
  "correct_answer": 1,
  "explanation": "[한국어 해설: 정답 근거 및 오답 배제 이유]",
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": []
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
- **Introductory Paragraph**: 반드시 **2~3절 이상으로 연결된 Complex sentence**로 주제 제시
- **Main Passage (①~⑤)**:
  - ① 주제 관련 구체적 설명 또는 사례
  - ② 주제 확장/일반화
  - ③ 또는 ④: **무관 문장** (겉보기에 관련 있어 보이지만 실제 주제에서 벗어남)
  - ⑤ 결론 또는 주제 강화

### Language Specifications
- **Passage Length**: 120–140 words
- **Sentence Complexity**: 평균 2.2절 이상, 주제문은 반드시 복합문

### Content Generation Guidelines
- 무관 문장은 **겉보기에 주제와 관련 있어 보이지만**, 실제로는 논리적 초점을 흐리거나 다른 주제로 전환
- **각 문장은 공백으로만 구분되며, 줄바꿈 없이 연속**
- 번호는 **①, ②, ③, ④, ⑤** 순서대로 문장 앞에만 붙인다.

**Required JSON Output Format:**
{
  "question": "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?",
  "passage": "[Introductory complex sentence] ① ... ② ... ③ ... ④ ... ⑤ ...",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of why the chosen sentence is irrelevant]",
  "vocabulary_difficulty": "AWL",
  "low_frequency_words": ["예: collaboration", "예: innovation", "예: comprehensive"]
}
```

---

## RC36 - 읽기 36번 (글의 순서 배열)

```
Create a CSAT Reading Item 36 (Paragraph Ordering) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 논리적 글의 순서 파악 능력 측정
- **Processing Pattern**: 주어진 문단 분석 → 각 단락의 기능 파악 → 논리적 연결 추적 → 최적 배열 도출

### Discourse Structure
- **Pattern**: 주어진 도입 문단(박스) → 순서가 섞인 (A), (B), (C) 단락
- **Flow**: 고정된 시작(원칙/개념 제시) → 세 개의 단락을 논리적 순서로 배열

### Language Specifications
- **Passage Length**: 130-150 words (total across all paragraphs)
- **Sentence Complexity**: Moderate to complex, with explicit logical connectors (Avg. 2.0-2.2 clauses per sentence)
- **Vocabulary Level**: Academic and transitional vocabulary

**Required JSON Output Format:**
{
  "question": "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
  "intro_paragraph": "[Introductory paragraph in a box]",
  "passage_parts": {
    "(A)": "[Paragraph A content]",
    "(B)": "[Paragraph B content]",
    "(C)": "[Paragraph C content]"
  },
  "options": ["(A)-(C)-(B)", "(B)-(A)-(C)", "(B)-(C)-(A)", "(C)-(A)-(B)", "(C)-(B)-(A)"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the logical order]"
}
```

---

## RC37 - 읽기 37번 (글의 순서 배열)

```
Create a CSAT Reading Item 37 (Paragraph Ordering) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 논리적 글의 순서 파악 능력 측정
- **Processing Pattern**: 주어진 문단 분석 → 각 단락의 기능 파악 → 논리적 연결 추적 → 최적 배열 도출

### Discourse Structure
- **Pattern**: 주어진 도입 문단(박스) → 순서가 섞인 (A), (B), (C) 단락
- **Flow**: 고정된 시작(현상 제시) → 세 개의 단락을 논리적 순서(예: 원인→실험→결과)로 배열

### Language Specifications
- **Passage Length**: 130-150 words (total across all paragraphs)
- **Sentence Complexity**: Moderate to complex (Avg. 2.0-2.2 clauses per sentence)

**Required JSON Output Format:**
{
  "question": "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은? [3점]",
  "intro_paragraph": "[Introductory paragraph in a box]",
  "passage_parts": {
    "(A)": "[Paragraph A content]",
    "(B)": "[Paragraph B content]",
    "(C)": "[Paragraph C content]"
  },
  "options": ["(A)-(C)-(B)", "(B)-(A)-(C)", "(B)-(C)-(A)", "(C)-(A)-(B)", "(C)-(B)-(A)"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the logical order]"
}
```

---

## RC38 - 읽기 38번 (문장 위치 추론)

```
Create a CSAT Reading Item 38 (Sentence Insertion) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 주어진 문장의 적절한 삽입 위치 파악 능력 측정
- **Processing Pattern**: 주어진 문장 분석 → 글의 논리적 흐름 파악 → 각 삽입 위치별 적합성 검토 → 최적 위치 선택

### Discourse Structure
- **Pattern**: 주어진 문장(박스) → 5개의 삽입 위치가 표시된 본문

### Language Specifications
- **Passage Length**: 120-140 words
- **Sentence Complexity**: Moderate to complex (Avg. 2.0+ clauses per sentence)
- **Vocabulary Level**: Academic vocabulary with discourse markers

### Content Generation Guidelines
- The passage must include five insertion points marked exactly as **( ① )**, **( ② )**, **( ③ )**, **( ④ )**, **( ⑤ )**.
- The given sentence must fit naturally into only one of these points.

**Required JSON Output Format:**
{
  "question": "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?",
  "given_sentence": "[Independent sentence to be inserted]",
  "passage": "[Text with ①②③④⑤ insertion points in English]",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the logical insertion point]"
}
```

---

## RC39 - 읽기 39번 (문장 위치 추론)

```
Create a CSAT Reading Item 39 (Sentence Insertion) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 주어진 문장의 적절한 삽입 위치 파악 능력 측정

### Language Specifications
- **Passage Length**: 120-140 words
- **Sentence Complexity**: Moderate to complex (Avg. 2.0+ clauses per sentence)

### Content Generation Guidelines
- The passage must include five insertion points marked exactly as **( ① )**, **( ② )**, **( ③ )**, **( ④ )**, **( ⑤ )** (with parentheses and spacing).
- The given sentence must fit naturally into only one of these points.

**Required JSON Output Format:**
{
  "question": "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은? [3점]",
  "given_sentence": "[Independent sentence to be inserted]",
  "passage": "[Text with ①②③④⑤ insertion points in English]",
  "options": ["①", "②", "③", "④", "⑤"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the logical insertion point]"
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

### Language Specifications
- **Passage Length**: The passage must consist of **9–11 sentences**.
  - Each sentence should be **18–22 words long**.
  - Overall passage length: approximately **150–170 words**.

### Summary Template Structure
- One complete English sentence summarizing the passage
- (A), (B)는 <u>    (A)    </u>, <u>    (B)    </u>로 표기
- 두 개념의 **관계나 대비**가 반드시 드러나야 함
- Sentence length must be **25–35 words**

### Option Format
- All options must follow the format **"(A): word - (B): word"**.
- Each option must be a **single English word only**.
- (A) and (B) must share the same grammatical category.

**Required JSON Output Format:**
{
  "question": "다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은? [3점]",
  "passage": "[150-170 word academic passage, 9-11 sentences]",
  "summary_template": "[25-35 word summary with <u>    (A)    </u> and <u>    (B)    </u> blanks]",
  "options": [
    "(A): word - (B): word",
    "(A): word - (B): word",
    "(A): word - (B): word",
    "(A): word - (B): word",
    "(A): word - (B): word"
  ],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation]"
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

### Marker & Underline Rules (STRICT)
- You MUST insert **exactly five** markers with the pattern: `(a) <u>word</u>` ... `(e) <u>word</u>`
- Lowercase marker letters only: **(a)(b)(c)(d)(e)**.
- Each underline is **ONE** English word only.
- Exactly **ONE** of the five underlined words MUST be **contextually inappropriate**.

### Length & Language
- Passage: **English only**
- Questions & explanations: **Korean**

## QUESTION SPECIFICATIONS
### Q41 — Title Inference
- **Stem (Korean)**: "윗글의 제목으로 가장 적절한 것은?"
- **Options (English, 5지)**: 5 English title statements, **5–10 words** each.
- **Correct Answer Rule**: `"correct_answer"` must be a **string** in `"1"`–`"5"`.

### Q42 — Vocabulary Appropriateness
- **Stem (Korean)**: "밑줄 친 (a)~(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]"
- **Options (fixed)**: exactly `["(a)", "(b)", "(c)", "(d)", "(e)"]`.
- **Correct Answer Rule**: `"correct_answer"` must be a **string** in `"1"`–`"5"`.

## REQUIRED JSON OUTPUT FORMAT
{
  "set_instruction": "[41~42] 다음 글을 읽고, 물음에 답하시오.",
  "passage": "[Edited passage with (a) <u>...</u> ... (e) <u>...</u>]",
  "questions": [
    {
      "question_number": 41,
      "question": "윗글의 제목으로 가장 적절한 것은?",
      "options": ["Title 1", "Title 2", "Title 3", "Title 4", "Title 5"],
      "correct_answer": "1",
      "explanation": "[한국어 해설]"
    },
    {
      "question_number": 42,
      "question": "밑줄 친 (a)~(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]",
      "options": ["(a)", "(b)", "(c)", "(d)", "(e)"],
      "correct_answer": "1",
      "explanation": "[한국어 해설]"
    }
  ]
}
```

---

## RC43_45 - 읽기 43-45번 (장문 독해 - 복합 유형)

```
Create a CSAT Reading Item 43–45 (Long Reading Set) in perfect JSON format.

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- Core Skill: Identify paragraph order, referent resolution, and content correctness from a 4-paragraph long reading passage.
- Special Note for Item 44: Exactly one pronoun among (a)–(e) must refer to a different character (Person B), while the other four pronouns refer to Person A. Person A and Person B MUST be the same gender.

### Character Guidelines
- Use only these names:
  - Female set: Sarah, Chloe, Emma, Mia
  - Male set: Alex, Ben, Jack, Leo
- Choose one gender set only (all-female or all-male).

### Story Theme Guidelines
- Randomly select one theme: 'artistic struggle', 'scientific discovery', 'sports rivalry', 'a community project', 'a family secret'.

### Language Specifications
- Passage Length: 400–450 words total (each paragraph 95–115 words).
- Sentence Complexity: Moderate (~2 clauses per sentence).
- Vocabulary Level: CEFR B2 with 2–3 C1 words.

### FORMATTING RULES FOR Q44 UNDERLINES (STRICT)
- Insert exactly five underlined pronouns, labeled (a)~(e):
  - `(a) <u>she</u>` or `(a) <u>he</u>`
  - The label MUST come **before** the underlined pronoun.
- Placement:
  - (A): include exactly one `(a) <u>pronoun</u>`
  - (B): include exactly one `(b) <u>pronoun</u>`
  - (C): include exactly one `(c) <u>pronoun</u>`
  - (D): include exactly two `(d) <u>pronoun</u>` and `(e) <u>pronoun</u>`
- Allowed forms: strictly lowercase → `he`, `him`, `she`, `her`.
- Case Variety Rule: At least one objective case (him/her) among the five.
- Absolute Gender Consistency: All five pronouns must be either `he/him` OR `she/her`, never mixed.

### Reference Resolution Design (Q44)
- Person A introduced by name in Paragraph A.
- Exactly 4 pronouns → Person A; exactly 1 → Person B.

### Question Format
- Q43: Paragraph order.
- Q44: Reference resolution.
- Q45: Content accuracy.

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
      "explanation": "한국어 설명"
    },
    {
      "question_number": 44,
      "question": "밑줄 친 (a)~(e) 중에서 가리키는 대상이 나머지 넷과 다른 것은?",
      "options": ["(a)", "(b)", "(c)", "(d)", "(e)"],
      "correct_answer": 1,
      "explanation": "Must explicitly map (a)~(e) to character names."
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
      "explanation": "각 보기의 사실 여부를 확인"
    }
  ]
}
```

---

# 끝
