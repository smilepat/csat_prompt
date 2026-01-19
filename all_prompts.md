# CSAT English Item Generation Prompts

## BASE PROMPT

```
You are an expert CSAT English item writer for Korea's College Scholastic Ability Test.

Follow these permanent rules across ALL items unless later, item-specific instructions override them:
1) Item types: Listening / Reading only; adhere to official CSAT formats.
2) Audience: Korean high-school CSAT takers; align with the national curriculum and achievement standards.
3) Language-use rule:
   - Passages / transcripts (stimulus): English only.
   - Question stems and explanations: Korean only.
4) Output: Return a single, well-formed JSON object. No extra text, no commentary, no markdown.
5) Choices: Exactly 5 options. Provide one correct answer and four plausible distractors.
6) Answer key: "correct_answer" must be an integer 1–5 (not a string label).
7) Content quality:
   - Use CSAT-appropriate vocabulary and sentence structures.
   - Avoid culturally biased content, ambiguous keys, trivial clues, or option-length giveaways.
   - Ensure fairness and clarity for Korean EFL learners.

Text Abstractness (Kim, 2012):
- Select an appropriate level (1–9) based on target skill and difficulty.
  * Low (1–3): concrete, familiar contexts
  * Medium (4–6): moderately abstract
  * High (7–9): abstract, less familiar contexts

Syntactic Complexity (guidelines):
- Control average words per sentence, clauses per sentence, and subordination ratio to match CSAT level.
- Ensure grammatical accuracy and naturalness.

Vocabulary Profile (default = "CSAT"):
- "CSAT": 기본 고등학교 수준, 빈출 어휘 중심
- "CSAT+O3000": 고등학교 수준 + Oxford 3000 포함
- "AWL": 학술적 난이도, Academic Word List 중심
Also output:
- "vocabulary_difficulty": one of ["CSAT","CSAT+O3000","AWL"]
- "low_frequency_words": []  # Fill with AWL or O3000 words if required by the item.

JSON OUTPUT CONTRACT (strict):
Return exactly these keys. Do NOT add or omit keys. Do NOT include markdown, backticks, or commentary.

{
  "stimulus": "<English-only passage or transcript>",
  "question_stem": "<Korean-only question prompt>",
  "options": ["<choice 1>", "<choice 2>", "<choice 3>", "<choice 4>", "<choice 5>"],
  "correct_answer": 1,
  "explanation": "<Korean-only rationale explaining why the correct option is correct and why others are not>",
  "vocabulary_difficulty": "CSAT",
  "low_frequency_words": []
}

Constraints:
- stimulus: English only. No Korean. No glossaries inside stimulus.
- question_stem & explanation: Korean only.
- options: 5 distinct, concise choices without overlap or "all/none of the above".
- correct_answer: integer 1–5 (not a string). Must match the correct option index (1-based).
- Keep lengths CSAT-appropriate; avoid excessive verbosity.
- No images, tables, or external links unless an item-specific prompt requires structured descriptions.

Self-check BEFORE returning JSON:
- [ ] JSON parses with a standard parser.
- [ ] Keys exactly match the contract above.
- [ ] correct_answer is an integer in [1,5].
- [ ] stimulus contains ONLY English; question_stem/explanation contain ONLY Korean.
- [ ] options are 5, mutually exclusive, and plausible.
- [ ] The rationale (explanation) justifies both the correct answer and the incorrectness of distractors in Korean.

Conflict resolution:
- If any later instructions conflict with these, the later, item-specific instructions take priority for that item.
```

---

## LC01 - 듣기 1번 (목적 파악)

```
Create a CSAT Listening Item 1 (Purpose Identification) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Identifying the speaker's purpose in formal announcements
- **Cognitive Process**: Listen → Identify speaker's intent → Match with purpose options
- **Difficulty Level**: Basic comprehension with clear purpose indicators

### Discourse Type & Structure
- **Format**: Formal monologue (announcement, notice, or public address)
- **Structure Pattern**: Greeting → Identity/Role → Main announcement → Details → Closing
- **Content Flexibility**: Any institutional context (school, office, public facility, organization)
- **Speaker Role**: Official announcer, administrator, or authority figure

### Language Specifications
- **Transcript Length**: 60–80 words (≈30–40 seconds)
- **Sentence Complexity**: Simple to moderate (1–2 clauses per sentence)
- **Vocabulary Level**: High-frequency, concrete vocabulary
- **Speech Rate**: Standard conversational pace with clear articulation
- **Vocabulary Profile**:
  "vocabulary_difficulty": "CSAT",
  "low_frequency_words": []

### Question Format Requirements
- **Stem (Korean)**: "다음을 듣고, [남자/여자]가 하는 말의 목적으로 가장 적절한 것을 고르시오."
  - 성별 표시는 상황에 맞게 [남자] 또는 [여자] 중 하나로 결정하세요.
- **Options (Korean)**: 5 purpose statements ending with "~하려고"
  - 예: "~을(를) 안내하려고", "~을(를) 요청하려고", "~을(를) 알리려고", 등
- **Correct Answer**: Must directly correspond to the speaker's main intent
- **Distractors**: Related but secondary purposes, unmentioned purposes, or opposite purposes
  - 각 오답은 지문 일부 정보와 연결되지만 '주된 목적'은 아님을 드러내야 함
  - 의미 중복·포괄/배타 관계로 정답이 쉽게 노출되지 않도록 구성

### Content Generation Guidelines
- Generate realistic announcement scenarios (schedule changes, policy updates, event notifications)
- The main purpose must be identifiable with attentive listening (명시적 단서 + 맥락적 단서)
- Keep institutional contexts authentic to Korean high school learners' experiences
- Avoid culture-specific knowledge that disadvantages Korean EFL learners

### Language-Use Rule (override if base differs)
- transcript: **English only**
- question/explanation/options: **Korean only**

### Output Validation Rules
- "transcript" must be 60–80 English words (no Korean).
- "options" must be exactly 5 strings, each ending with "하려고".
- "correct_answer" must be an integer 1–5.
- "explanation" must justify why the correct option matches the main purpose and why others do not (in Korean).
- No markdown, no extra commentary — **return JSON only**.

**Required JSON Output Format:**
{
  "question": "다음을 듣고, [남자/여자]가 하는 말의 목적으로 가장 적절한 것을 고르시오.",
  "transcript": "[60-80 word formal announcement in English]",
  "options": ["목적1하려고", "목적2하려고", "목적3하려고", "목적4하려고", "목적5하려고"],
  "correct_answer": 1,
  "explanation": "[정답이 화자의 주된 목적과 일치함을 근거로 설명하고, 나머지 선택지가 부적절한 이유를 간단히 제시하세요.]",
  "vocabulary_difficulty": "CSAT",
  "low_frequency_words": []
}

Self-check before returning:
- [ ] JSON 파싱 가능 여부 확인
- [ ] "transcript" 60–80 words / English only
- [ ] options 5개, 모두 "~하려고"로 끝나는지
- [ ] correct_answer ∈ {1,2,3,4,5}
- [ ] question/explanation: Korean only
- [ ] Distractors가 '주된 목적'과 구분되는지
```

---

## LC02 - 듣기 2번 (의견 파악)

```
Create a CSAT Listening Item 2 (Opinion Identification) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Identifying a speaker's opinion in conversational dialogue
- **Cognitive Process**: Track dialogue → Identify target speaker → Extract consistent viewpoint
- **Difficulty Level**: Basic comprehension with clear opinion markers

### Discourse Type & Structure
- **Format**: Two-person dialogue with alternating speakers using explicit labels: `M:` and `W:`
- **Structure Pattern**: Topic introduction → Opinion expression → Supporting reasons → Conclusion
- **Content Flexibility**: Everyday topics requiring personal opinions or recommendations
- **Interaction Type**: Advice-giving, preference sharing, light persuasion

### Language Specifications
- **Transcript Length**: 80–100 words (≈40–50 seconds)
- **Sentence Complexity**: Simple sentences with basic connectors (because, so, but, I think, in my view, we should, etc.)
- **Vocabulary Level**: Everyday conversational vocabulary
- **Speech Rate**: Natural conversational pace with clear speaker distinction
- **Vocabulary Profile**:
  "vocabulary_difficulty": "CSAT",
  "low_frequency_words": []

### Question Format Requirements
- **Stem (Korean)**: "대화를 듣고, [남자/여자]의 의견으로 가장 적절한 것을 고르시오."
  - 상황에 맞게 대상 화자를 [남자] 또는 [여자] 중 하나로 결정하세요.
- **Options (Korean)**: 5 opinion statements (declarative or prescriptive)
  - 종결: "~이다", "~해야 한다" 등 자연스러운 평서/당위 표현 사용
- **Correct Answer**: Must reflect the target speaker's consistent viewpoint across the dialogue
- **Distractors**:
  - 다른 화자의 의견, 일부 정보만 반영한 부분 의견, 언급되지 않은 견해, 반대 의견
  - 의미 중복/포괄 관계를 피하고, 정보 단서(예: 수치·시간)만으로 정답이 드러나지 않도록 구성

### Content Generation Guidelines
- 활동, 선택, 권고와 관련된 자연스러운 일상 대화 상황을 설정하세요.
- 한 화자가 일관된 의견을 명시적으로 표현하고, 간단한 근거를 1–2개 제시하게 하세요.
- 한국 고등학생에게 익숙한 맥락(학교/동아리/가정/지역 커뮤니티 등)을 사용하세요.
- 문화특정 배경지식이 필요하지 않도록 공정성을 확보하세요.
- 발화 라벨은 줄마다 반드시 `M:` 또는 `W:`로 시작하게 하세요. (혼용/누락 금지)

### Language-Use Rule (override if base differs)
- transcript: **English only**
- question/explanation/options: **Korean only**

### Output Validation Rules
- "transcript" must be 80–100 English words and lines must alternate starting with `M:` / `W:` labels.
- "options" must be exactly 5 Korean statements (mix of declarative/prescriptive ok).
- "correct_answer" must be an integer 1–5.
- "explanation" (Korean) must:
  - 대화에서 대상 화자의 의견 표지가 나타나는 문장을 근거로 제시
  - 오답이 왜 대상 화자의 의견이 아닌지(상대 화자 견해/부분 정보/미언급/반대) 간단히 명시
- No markdown, no extra commentary — **return JSON only**.

**Required JSON Output Format:**
{
  "question": "대화를 듣고, [남자/여자]의 의견으로 가장 적절한 것을 고르시오.",
  "transcript": "M: ...\nW: ...\nM: ...\nW: ...",
  "options": ["의견1이다", "의견2해야 한다", "의견3이다", "의견4해야 한다", "의견5이다"],
  "correct_answer": 1,
  "explanation": "[대상 화자의 의견 근거와 오답 배제 사유를 한국어로 간결히 제시하세요.]",
  "vocabulary_difficulty": "CSAT",
  "low_frequency_words": []
}

Self-check before returning:
- [ ] JSON 파싱 가능 여부 확인
- [ ] "transcript" 80–100 words / English only / 각 줄 `M:` 또는 `W:`로 시작 / 교대 발화가 자연스러운지
- [ ] options 5개, 한국어 자연스러운 평서/당위 종결
- [ ] correct_answer ∈ {1,2,3,4,5} (1-based indexing)
- [ ] question/explanation: Korean only
- [ ] Distractors가 대상 화자의 '일관된 의견'과 구분되는지
```

---

## LC06 - 듣기 6번 (지불 금액)

```
Create a **CSAT Listening Item 6 (Payment Amount)** with **high realism and strong guardrails** using the following specifications.

## ITEM CHARACTERISTICS & METHOD

### Assessment Objective
- **Core Skill**: Compute the payable amount via mental arithmetic.
- **Cognitive Process**: Extract unit prices & quantities (integers) → Apply ≤1 discount/condition → Multiply → Sum → (Test-taker computes privately)

### Dialogue Type & Structure
- **Format**: Transactional dialogue; each line MUST start with `M:` or `W:`
- **Turns**: 7–9 turns total
- **Suggested Structure**:
  1) Context/need (venue, event, shop, etc.)
  2) Unit price(s) stated (integers only; USD `$` or KRW `원`, consistent)
  3) Quantity decision
  4) Discount/condition mentioned (flat, percentage, or explicitly not applicable)
  5) Clerk summarizes items (repeat numbers ONCE only, but **never state total or multiply in speech**)
  6) Customer confirms
  7) (Optional small talk / seat/time preference)
  8) Clerk closing with **payment action phrase only**
  9) Customer polite reply (no numbers) → END

### CRITICAL ANTI-LEAK GUARDRAILS
- The **final payment amount must NEVER appear** in the transcript.
- Forbid explicit totalizing phrases:
  - EN: "That'll be", "It comes to", "The total is", "Altogether", "You'll pay", "Let me calculate"
  - KO: "총액/합계/금액은", "합쳐서/모두 합하면", "계산해 드리면", "…원입니다/입니다", "얼마예요?/얼마인가요?"
- The **last TWO turns** must contain **zero** digits, currency symbols, or number words.
- Customer must NOT ask "How much will it be?"
- Clerk must NOT verbalize calculations; only provide unit prices, conditions, and action phrase.

### CRITICAL MATH RULE
- Every intermediate and final calculation must yield an **INTEGER**.
- Unit prices must always be multiples of 10 (e.g., $10, $20, $30 … or 10원, 20원, 30원 …).
- Only the following discount rates are allowed: 10%, 20%, 25%, 50%.
- Divisibility conditions for integer results:
  - 10% off → Pre-discount total must be a **multiple of 10**.
  - 20% off → Pre-discount total must be a **multiple of 5** (automatically satisfied if all prices are multiples of 10).
  - 25% off → Pre-discount total must be a **multiple of 4** (easily satisfied if total is a multiple of 20).
  - 50% off → Always results in an integer.
- If the chosen total does not satisfy these divisibility conditions, you must **discard and regenerate internally with different unit prices or quantities until it does**.
- No rounding or decimal/fraction results are permitted anywhere.
- Final discounted price ∈ ℤ (integer set).

### Language Specifications
- **Transcript Length**: **110–130 English words**
  - If output is shorter than 100 words, regenerate internally until it satisfies the range.
- **Sentence Complexity**: Moderate
- **Vocabulary**: Everyday commercial/service

### Question & Options (Korean)
- **Stem**: "대화를 듣고, [남자/여자]가 지불할 금액을 고르시오."
- **Currency Consistency**: Options MUST match transcript currency (all `$` or all `원`).
- **Options**: 5 distinct integers, close in value.
  - Spacing: each differs ≥2 (same unit scale).
- **Correct Answer**: not in transcript; index = 1–5.

### Output Contract (JSON ONLY)
{
  "question": "대화를 듣고, [남자/여자]가 지불할 금액을 고르시오.",
  "transcript": "[110–130 word dialogue in English; M:/W: per line; unit prices & quantities; one discount mode (flat / integer-safe percent / explicit no-discount); NO final total; last two turns contain NO numerals/currency/number words.]",
  "options": ["<same-currency amount 1>", "<same-currency amount 2>", "<same-currency amount 3>", "<same-currency amount 4>", "<same-currency amount 5>"],
  "correct_answer": 1,
  "explanation": "[계산 과정을 한국어로 단계별로만 설명, 최종 금액 숫자 제시 금지, 마지막은 '따라서 정답은 ○번이다']",
  "vocabulary_difficulty": "CSAT",
  "low_frequency_words": []
}

### Construction Checklist
- [ ] Transcript length = 110–130 words; regenerate if <100
- [ ] Transcript 7–9 turns; each line starts with `M:` or `W:`
- [ ] No final total or explicit multiplication spoken
- [ ] Last two turns free of digits/currency/number words
- [ ] **CRITICAL MATH RULE satisfied**: all totals and discounts yield integers, no rounding
- [ ] Exactly one discount mode (flat, integer-safe percent, or explicit no-discount)
- [ ] Options: 5, same currency as transcript, distinct, spacing ≥2
- [ ] Explanation: Korean only, step-by-step reasoning, no final number, ends with "따라서 정답은 ○번이다"
```

---

## LC07 - 듣기 7번 (이유 파악)

```
Create a CSAT Listening Item 7 (Reason Identification) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Identifying specific reasons for inability to participate in events
- **Cognitive Process**: Track invitation → Identify refusal → Extract actual reason from multiple possibilities
- **Difficulty Level**: Intermediate comprehension requiring reason discrimination

### Discourse Type & Structure
- **Format**: Two-person dialogue about event participation
- **Structure Pattern**: Invitation/suggestion → Interest but inability → Reason exploration → Actual reason revelation
- **Content Flexibility**: Any social event or activity invitation scenario
- **Interaction Type**: Social invitation and polite refusal with explanation

### Language Specifications
- **Transcript Length**: 90-110 words (approximately 45-55 seconds)
- **Sentence Complexity**: Moderate with causal expressions and explanations
- **Vocabulary Level**: Social and explanatory vocabulary
- **Speech Rate**: Natural conversational pace with clear reason indicators

### Vocabulary Profile
"vocabulary_difficulty": "CSAT",
"low_frequency_words": []

### Question Format Requirements
- **Stem**: "대화를 듣고, [남자/여자]가 [이벤트]에 갈 수 <u>없는</u> 이유를 고르시오."
- **Options**: 5 Korean reason statements using causal expressions
- **Correct Answer**: Must be the actual reason explicitly stated by the speaker
- **Distractors**: Suggested but rejected reasons, related but incorrect reasons, opposite situations

### Content Generation Guidelines
- Create realistic social invitation scenarios
- Include multiple potential reasons but make one clearly correct
- Ensure the actual reason is explicitly stated, not just implied
- Use contexts relevant to Korean student social life

**Required JSON Output Format:**
{
  "question": "대화를 듣고, [남자/여자]가 [이벤트]에 갈 수 <u>없는</u> 이유를 고르시오.",
  "transcript": "[90-110 word invitation dialogue with M:/W: indicators]",
  "options": ["이유1때문에", "이유2해야 해서", "이유3때문에", "이유4해야 해서", "이유5때문에"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the reason]"
}
```

---

## LC08 - 듣기 8번 (언급되지 않은 것)

```
Create a CSAT Listening Item 8 (Not Mentioned) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Identifying information not mentioned in event-related dialogue
- **Cognitive Process**: Track mentioned information → Compare with options → Identify omissions
- **Difficulty Level**: Intermediate information tracking with systematic checking

### Discourse Type & Structure
- **Format**: Two-person dialogue about event information
- **Structure Pattern**: Event discovery → Information gathering → Detail confirmation → Additional inquiries
- **Content Flexibility**: Any event, program, or activity with multiple informational aspects
- **Interaction Type**: Information exchange and inquiry

### Language Specifications
- **Transcript Length**: 90-110 words (approximately 45-55 seconds)
- **Sentence Complexity**: Moderate with information-dense content
- **Vocabulary Level**: Informational and descriptive vocabulary
- **Speech Rate**: Natural pace with clear information delivery

### Vocabulary Profile
"vocabulary_difficulty": "CSAT",
"low_frequency_words": []

### Question Format Requirements
- **Stem**: "대화를 듣고, [Event/Program/Activity in English]에 관해 언급되지 <u>않은</u> 것을 고르시오."
- **Options**: 5 Korean information categories related to the topic
- **Correct Answer**: Must be the information category not mentioned in the dialogue
- **Distractors**: Information categories explicitly mentioned in the dialogue

### Content Generation Guidelines
- Create information-rich dialogues about events or programs
- Ensure 4 information categories are clearly mentioned and 1 is omitted
- Include realistic event contexts with typical information needs
- Use systematic information patterns familiar to Korean students

**Required JSON Output Format:**
{
  "question": "대화를 듣고, [Event/Program/Activity in English]에 관해 언급되지 <u>않은</u> 것을 고르시오.",
  "transcript": "[90-110 word information dialogue with M:/W: indicators]",
  "options": ["정보항목1", "정보항목2", "정보항목3", "정보항목4", "정보항목5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of what was not mentioned]"
}
```

---

## LC09 - 듣기 9번 (내용 불일치)

```
Create a CSAT Listening Item 9 (Content Mismatch) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Identifying factual inconsistencies between monologue content and options
- **Cognitive Process**: Process announcement information → Compare with factual statements → Identify contradictions
- **Difficulty Level**: Intermediate factual verification with detailed information

### Discourse Type & Structure
- **Format**: Formal announcement monologue
- **Structure Pattern**: Introduction → Event details → Schedule information → Procedures → Additional information
- **Content Flexibility**: Any formal event or program announcement
- **Speaker Role**: Official announcer or event organizer

### Language Specifications
- **Transcript Length**: 110-130 words (approximately 55-65 seconds)
- **Sentence Complexity**: Moderate with detailed factual information
- **Vocabulary Level**: Formal and informational vocabulary
- **Speech Rate**: Clear, measured pace appropriate for announcements

### Vocabulary Profile
"vocabulary_difficulty": "CSAT",
"low_frequency_words": []

### Event Name Extraction Rules (CRITICAL)
- **From the transcript, extract the official event/program name (e.g., "Ecosystem Exploration Day").
- **Preserve the exact English name and capitalization as spoken; do not translate it.
- **If multiple names appear, choose the main event being announced (first full proper name in the introduction).
- **If no explicit event name is given, construct a concise, specific proper name from context (e.g., "School Wetlands Field Trip").

### Question Format Requirements
- **Stem**: "[이벤트]에 관한 다음 내용을 듣고, 일치하지 <u>않는</u> 것을 고르시오."
- **Format**: "「{event_name}」에 관한 다음 내용을 듣고, 일치하지 <u>않는</u> 것을 고르시오."
- **Do NOT output placeholders like "[이벤트]". If the event name cannot be extracted, synthesize a plausible proper name from the transcript and use it instead.
- **Options**: 5 Korean factual statements about the announced content
- **Correct Answer**: Must be the statement that contradicts the announcement
- **Distractors**: Statements that accurately reflect the announcement content

### Content Generation Guidelines
- Create detailed event announcements with specific factual information
- Ensure 4 statements match the content exactly and 1 contradicts it
- Include realistic institutional or public event contexts
- Use precise factual language and clear information structure

### Self-Check Before Output (MANDATORY)
- The question must contain 「 and 」 with the actual event name, not any placeholders.
- correct_answer must be a number 1–5.
- The transcript must be English only; the question/explanation must be Korean.
- If the question contains [ or ], regenerate the question to use the required format.

**Required JSON Output Format:**
{
  "question": "「{event_name}」에 관한 다음 내용을 듣고, 일치하지 <u>않는</u> 것을 고르시오.",
  "transcript": "[110-130 word formal announcement in English]",
  "options": ["사실1", "사실2", "사실3", "사실4", "사실5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the contradiction]"
}
```

---

## LC10 - 듣기 10번 (표 정보 확인)

```
Create a CSAT Listening Item 10 (Chart Information) following these specifications:

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
```

---

## LC11 - 듣기 11번 (짧은 대화 응답)

```
Create a CSAT Listening Item 11 (Short Response Inference) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Inferring appropriate responses to final statements in short dialogues
- **Cognitive Process**: Follow dialogue context → Analyze final statement → Select logical response
- **Difficulty Level**: Advanced contextual inference requiring pragmatic understanding

### Discourse Type & Structure
- **Format**: Brief two-person dialogue (2-3 exchanges)
- **Structure Pattern**: Situation setup → Problem/request → Final statement requiring response
- **Content Flexibility**: Any everyday situation requiring immediate, contextually appropriate responses
- **Interaction Type**: Problem-solving, request-response, or social interaction

### Language Specifications
- **Transcript Length**: 60-80 words (approximately 30-40 seconds)
- **Sentence Complexity**: Simple to moderate with clear contextual cues
- **Vocabulary Level**: Everyday conversational vocabulary
- **Speech Rate**: Natural conversational pace

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: permit", "예: schedule"]

### Formatting Instructions for Transcript
- 대화문은 M: (남자 화자), W: (여자 화자) 표기를 사용한다.
- 남자가 먼저 말하고, 여자가 마지막에 말하며, 그 마지막 발화가 문제에서 응답해야 하는 대상이 된다.
- 대화는 2~3턴으로 구성하되, 마지막 발화는 반드시 여자의 대사로 끝난다.

### Question Format Requirements
- **Stem**: "대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오. [3점]"
- **Options**: 5 English response options
- **Correct Answer**: Must be the most contextually appropriate and natural response
- **Distractors**: Contextually inappropriate, logically inconsistent, or socially awkward responses

### Content Generation Guidelines
- Create realistic everyday scenarios requiring immediate responses
- Ensure the final statement clearly sets up the need for a specific type of response
- Include contexts familiar to Korean students (daily life, services, social situations)
- Use natural conversational patterns and appropriate social registers

**Required JSON Output Format:**
{
  "question": "대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오. [3점]",
  "transcript": "[60-80 word short dialogue with M:/W: indicators]",
  "options": ["Response 1", "Response 2", "Response 3", "Response 4", "Response 5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of why the response is appropriate]"
}
```

---

## LC12 - 듣기 12번 (짧은 대화 응답)

```
Create a CSAT Listening Item 12 (Short Response Inference) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Inferring appropriate responses to final statements in short dialogues
- **Cognitive Process**: Follow dialogue context → Analyze final statement → Select logical response
- **Difficulty Level**: Intermediate contextual inference with clear response patterns

### Discourse Type & Structure
- **Format**: Brief two-person dialogue (2-3 exchanges)
- **Structure Pattern**: Proposal → Concern expression → Reassurance → Response needed
- **Content Flexibility**: Any situation involving initial hesitation followed by reassurance
- **Interaction Type**: Invitation acceptance after concern resolution

### Language Specifications
- **Transcript Length**: 50-70 words (approximately 25-35 seconds)
- **Sentence Complexity**: Simple with clear reassurance patterns
- **Vocabulary Level**: Basic conversational vocabulary
- **Speech Rate**: Natural conversational pace

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: permit", "예: schedule"]

### Question Format Requirements
- **Stem**: "대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오."
- **Options**: 5 English response options
- **Correct Answer**: Must show acceptance after reassurance, as the man's response to the final W: line
- **Distractors**: Continued hesitation, irrelevant responses, inappropriate reactions

### Transcript Formatting Instructions
- 대화문은 W: (여자 화자), M: (남자 화자) 표기를 사용한다.
- 여자가 먼저 말하고, 남자가 마지막에 말하며, 그 마지막 발화가 문제에서 응답해야 하는 대상이 된다.
- 대화는 2~3턴으로 구성하되, 마지막 발화는 반드시 남자의 대사로 끝난다.
- 대화문 표기는 W: (여자), M: (남자)를 사용한다.
- 여자가 먼저 말하고, 마지막 발화도 반드시 여자의 대사(W:)로 끝난다.
- 남자의 응답은 transcript에 포함하지 않으며, 보기가 남자의 응답 후보가 된다.
- (검증) transcript의 마지막 줄은 반드시 `W:`로 시작해야 한다.

### Content Generation Guidelines
- Create scenarios where initial concerns are addressed and resolved
- Ensure the final statement provides clear reassurance
- Include contexts involving activities, programs, or invitations
- Use clear concern-resolution patterns

**Required JSON Output Format:**
{
  "question": "대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오.",
  "transcript": "[50-70 word dialogue with W:/M: indicators; ends with a W: line; the man's response is NOT included]",
  "options": ["Response 1", "Response 2", "Response 3", "Response 4", "Response 5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the response logic]"
}
```

---

## LC13 - 듣기 13번 (긴 대화 응답)

```
Create a CSAT Listening Item 13 (Long Response Inference) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Inferring appropriate responses in extended dialogue contexts
- **Cognitive Process**: Track extended conversation → Understand contribution context → Select appreciative response
- **Difficulty Level**: Intermediate contextual inference with extended dialogue tracking

### Discourse Type & Structure
- **Format**: Extended two-person dialogue
- **Turn Pattern**: Exactly **9 turns total** → M: 5 times, W: 4 times
- **Structure Pattern**: Contact → Proposal → Interest → Contribution offer → Acceptance → Response needed
- **Content Flexibility**: Any collaborative or charitable activity scenario
- **Interaction Type**: Voluntary contribution and appreciation

### Language Specifications
- **Transcript Length**: 100-120 words (approximately 50-60 seconds)
- **Sentence Complexity**: Simple with clear contribution patterns
- **Vocabulary Level**: Basic conversational and activity-related vocabulary
- **Speech Rate**: Natural conversational pace

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: permit", "예: schedule"]

### Question Format Requirements
- **Stem**: "대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오."
- **Options**: 5 English response options
- **Correct Answer**: Must express appreciation and encouragement for the contribution, as the woman's response to the final M: line
- **Distractors**: Inappropriate reactions, misunderstanding responses, irrelevant comments

### Transcript Formatting Instructions
- 대화문은 반드시 **M과 W의 발화가 교대로 교환**되어야 한다.
- 총 **9턴**: 남자(M) 5회, 여자(W) 4회.
- 마지막 발화는 반드시 **M:으로 끝나야** 하며, 여자의 최종 응답은 transcript에 포함하지 않는다.
- 전체 길이는 100~120 단어(약 50~60초)로 유지한다.

### Content Generation Guidelines
- Create scenarios involving voluntary contributions or collaborative efforts
- Ensure the final statement confirms positive contribution
- Include contexts involving community activities, charitable work, or group projects
- Use clear appreciation and encouragement patterns

**Required JSON Output Format:**
{
  "question": "대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오.",
  "transcript": "[100-120 word extended dialogue with exactly 9 turns (M:5, W:4), ending with M:]",
  "options": ["(Woman's response) 1", "(Woman's response) 2", "(Woman's response) 3", "(Woman's response) 4", "(Woman's response) 5"],
  "correct_answer": [1-5],
  "explanation": "[남자의 마지막 발화에 대해 여자가 감사와 격려를 표현하는 응답이 왜 적절한지 한국어로 설명]"
}
```

---

## LC14 - 듣기 14번 (긴 대화 응답)

```
Create a CSAT Listening Item 14 (Long Response Inference) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Inferring appropriate responses in complex extended dialogues
- **Cognitive Process**: Track complex conversation → Understand scheduling context → Select appropriate response
- **Difficulty Level**: Advanced contextual inference with complex dialogue tracking

### Discourse Type & Structure
- **Format**: Extended two-person dialogue
- **Scenario Type**: Professional **telephone conversation**
- **Turn Pattern**: Exactly **9 turns total** → W: 5 times, M: 4 times
- **Structure Pattern**: Request → Acceptance → Scheduling conflict → Coordination → Promise → Response needed
- **Interaction Type**: Professional scheduling and commitment

### Language Specifications
- **Transcript Length**: 120-140 words (approximately 60-70 seconds)
- **Sentence Complexity**: Moderate with professional language patterns
- **Vocabulary Level**: Professional and scheduling vocabulary
- **Speech Rate**: Natural professional conversation pace

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: permit", "예: schedule"]

### Question Format Requirements
- **Stem**: "대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오. [3점]"
- **Options**: 5 English response options
- **Correct Answer**: Must express hope and positive expectation for the promised response, as the man's response to the final W: line
- **Distractors**: Impatient responses, misunderstanding, inappropriate timing, irrelevant comments

### Transcript Formatting Instructions
- 대화문은 반드시 **M과 W의 발화가 교대로 교환**되어야 한다.
- 총 **9턴**: 여자(W) 5회, 남자(M) 4회.
- 마지막 발화는 반드시 **W:**로 끝나야 하며, 그 발화는 후속 응답(콜백/이메일 약속 등)을 명확히 약속한다.
- 남자의 최종 응답은 transcript에 포함하지 않고, 선택지에 제시한다.
- 전체 길이는 120~140 단어(약 60~70초)로 유지한다.
- 상황은 반드시 **전화 통화**여야 하며, 첫 발화는 전화 인사 또는 자기소개로 시작한다.

### Content Generation Guidelines
- Create professional consultation or expert invitation scenarios
- Ensure the final statement makes a clear promise for future response
- Include contexts involving professional services, expert advice, or formal requests
- Use appropriate professional language and scheduling patterns

**Required JSON Output Format:**
{
  "question": "대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오. [3점]",
  "transcript": "[120-140 word professional telephone dialogue with exactly 9 turns (W:5, M:4), ending with a W: line that promises a follow-up; the man's response is NOT included]",
  "options": ["(Man's response) 1", "(Man's response) 2", "(Man's response) 3", "(Man's response) 4", "(Man's response) 5"],
  "correct_answer": [1-5],
  "explanation": "[여자의 마지막 약속 발화에 대해 남자가 희망/긍정적 기대를 공손하게 표현하는 응답이 왜 적절한지 한국어로 설명]"
}
```

---

## LC15 - 듣기 15번 (상황에 맞는 말)

```
Create a CSAT Listening Item 15 (Situational Response) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Selecting appropriate utterances for complex situational contexts
- **Cognitive Process**: Analyze complex situation → Understand speaker motivation → Select optimal expression
- **Difficulty Level**: Advanced situational inference requiring deep contextual understanding

### Discourse Type & Structure
- **Format**: Situational description monologue
- **Structure Pattern**: Background → Initial plan → Complication → Experience factor → Advice motivation → Utterance selection
- **Content Flexibility**: Any advice-giving situation based on experience and expertise
- **Speaker Role**: Experienced advisor offering guidance based on personal knowledge

### Language Specifications
- **Transcript Length**: 140-160 words (approximately 70-80 seconds)
- **Sentence Complexity**: Complex with sophisticated situational development
- **Vocabulary Level**: Sophisticated situational and advisory vocabulary
- **Speech Rate**: Measured pace appropriate for complex situation description

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: permit", "예: schedule"]

### Question Format Requirements
- **Stem**: "다음 상황 설명을 듣고, [화자]가 [상대방]에게 할 말로 가장 적절한 것을 고르시오. [3점]"
- **Options**: 5 English utterance options
- **Correct Answer**: Must be the most contextually appropriate and helpful utterance
- **Distractors**: Partially appropriate, contextually mismatched, or inappropriately toned utterances

### Transcript Formatting Instructions
- transcript의 마지막 문장은 반드시 다음 영어 문장으로 끝난다(철자·구두점·대괄호 그대로 사용):
   "In this situation, what would [화자] most likely to say to [상대방]?"
- 위 마지막 문장도 Transcript Length(140–160 words)에 포함된다

### Content Generation Guidelines
- Create complex scenarios requiring experience-based advice
- Ensure the speaker has clear motivation and expertise to offer guidance
- Include realistic contexts where advice-giving is natural and helpful
- Use sophisticated language appropriate for complex situational analysis

**Required JSON Output Format:**
{
  "question": "다음 상황 설명을 듣고, [화자]가 [상대방]에게 할 말로 가장 적절한 것을 고르시오. [3점]",
  "transcript": "[140-160 word situational description in English; ends with the exact line: \"In this situation, what would [화자] most likely to say to [상대방]?\" ]",
  "options": ["Utterance 1", "Utterance 2", "Utterance 3", "Utterance 4", "Utterance 5"],
  "correct_answer": [1-5],
  "explanation": "[Korean explanation of the situational appropriateness]"
}
```

---

## LC16_17 - 듣기 16-17번 (장문 듣기 세트형)

```
Create a CSAT Listening Item 16-17 (Long Listening Set) following these specifications.

## ITEM CHARACTERISTICS
- Extended academic/informational monologue
- 180–220 words in English (must count words; outside this range = INVALID)
- Clear structure: Introduction → Topic statement → 4–5 enumerated items → Explanation → Conclusion
- Speaker: Expert/lecturer/presenter

## PLACEHOLDER REPLACEMENT (HARD CONSTRAINTS)
- [화자] MUST be replaced in the final JSON with exactly ONE of: "화자", "남자", "여자".
  - If monologue with no gender cues → "화자".
  - If dialogue with M:/W: markers → use "남자" or "여자".
- [항목 유형] MUST be replaced with an ACTUAL category label that matches the enumerated items in the transcript.
  - Examples: "문학 장르", "언어적 표현", "문화적 관습", "의사소통 방식".
  - The chosen label must exactly describe the enumerated list in the transcript.
- Do NOT leave [화자] or [항목 유형] in the output. If placeholders remain, regenerate.

## QUESTION FORMAT (HARD CONSTRAINTS)
- Two questions only: question_number 16 and 17.
- Q16: "[화자/남자/여자]가 하는 말의 주제로 가장 적절한 것은?"
  - Options: 5 ENGLISH topic statements.
  - correct_answer: integer (1–5).
  - explanation: Korean.
- Q17: "언급된 [구체적 항목 유형]이 <u>아닌</u> 것은?"
  - Transcript must enumerate 4–5 items; options must list those items (English) + one distractor.
  - correct_answer: integer (1–5).
  - explanation: Korean.

## VOCABULARY METADATA (HARD CONSTRAINTS)
- At top-level, always output:
  "vocabulary_difficulty": "CSAT+O3000"
  "low_frequency_words": [at least 2 uncommon academic words from transcript]
- These keys are mandatory. If missing → regenerate.

## OUTPUT FORMAT (STRICT JSON ONLY)
Return ONLY:
{
  "set_instruction": "[16~17] 다음을 듣고, 물음에 답하시오.",
  "transcript": "[180–220 word English monologue]",
  "questions": [
    {
      "question_number": 16,
      "question": "[화자/남자/여자]가 하는 말의 주제로 가장 적절한 것은?",
      "options": ["topic1", "topic2", "topic3", "topic4", "topic5"],
      "correct_answer": 1,
      "explanation": "[한국어 해설]"
    },
    {
      "question_number": 17,
      "question": "언급된 [구체적 항목 유형]이 <u>아닌</u> 것은?",
      "options": ["item1", "item2", "item3", "item4", "item5"],
      "correct_answer": 3,
      "explanation": "[한국어 해설]"
    }
  ],
  "vocabulary_difficulty": "CSAT+O3000",
  "low_frequency_words": ["academic_word1", "academic_word2"]
}

## VALIDATION REMINDERS
- Word count strictly 180–220.
- No placeholders remain.
- question_number field required.
- correct_answer must be integer 1–5.
- vocab metadata required.
```

---

## RC18 - 읽기 18번 (목적 파악)

```
Create a CSAT Reading Item 18 (Purpose Identification) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: Identifying the primary communicative purpose of a formal notice or announcement
- **Cognitive Process**: Analyze background situation → Trace cause and anticipated outcomes → Infer the writer's main intent → Match with the most accurate purpose option
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
- No informal greetings (e.g., "Hello," "Hi,").

### Language Specifications
- **Passage Length**: 120–150 words (English only)
- **Register**: Formal, institutional tone
- **Sentence Style**: Compound–complex preferred; align with syntactic targets
- **Key Language Features**:
  - Causal markers: "due to", "as a result", "because of"
  - Anticipatory phrasing: "many looked forward to", "we had planned to"
  - Intent verbs (appear late): "announce", "inform", "notify", "postpone", "cancel"
  - Closure tone: "we regret…", "we appreciate your understanding", "thank you for your cooperation"
- **Vocabulary Profile**:
  "vocabulary_difficulty": "CSAT+O3000",
  "low_frequency_words": ["sponsor", "exhibit", "festival"]

### Question Format Requirements
- **Stem (Korean)**: "다음 글의 목적으로 가장 적절한 것은?"
- **Options (Korean, 5지)**:
  - Action-based 목적 표현, 모두 "~하려고"로 끝남
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
- [ ] Distractors가 '주된 목적'과 구분되는지
```

---

## RC19 - 읽기 19번 (심경 변화)

```
Create a CSAT Reading Item 19 (Emotional Change) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY
### Assessment Objective
- **Core Skill**: Tracking emotional progression in narrative texts
- **Cognitive Process**: Identify initial state → Track transition points → Determine final state via inference
- **Difficulty Level**: Intermediate emotional analysis requiring inference skills

### Text Type & Structure
- **Format**: Personal narrative or short story with a clear emotional arc
- **Structure Pattern**: Initial situation → Expectation/hope → Complication → Behavioral/physiological response → Resolution cue
- **Narrative Type**: First-person or close third-person focalization

### Language Specifications
- **Passage Length**: 100–130 words (English only)
- **Sentence Complexity**: Moderate; narrative, vivid but concise
- **Vocabulary Level**: Concrete, descriptive, inference-friendly
- **Reading Level**: Accessible narrative style for Korean HS learners

### CRITICAL ANTI-LEAKAGE RULES (HARD CONSTRAINTS)
1. ❌ **Direct emotion vocabulary is strictly forbidden.**
   - Do NOT use any emotional adjectives, verbs, adverbs, or nouns (e.g., happy, sad, nervous, anxious, proud, relief, hesitate, unsure, frustrated, disappointed, confident, excited, indifferent, etc.).
   - Do NOT use synonyms, antonyms, or morphological variants of the option adjectives.
   - Do NOT use explicit emotional actions (e.g., smile, frown, cry, cheer, sigh).
   - If such words appear, regenerate internally and remove them.

2. ❌ **Option words must NOT appear in the passage.**
   - The exact adjectives used in the options (e.g., "anxious", "relieved") and their synonyms/variants must not appear in the passage text.
   - The passage must only convey emotions indirectly through behaviors, contexts, or physiological cues.

3. ✅ Emotions must be inferred ONLY via:
   - Neutral physical behaviors (e.g., tapping a pen, pausing before speaking, tightening shoulders).
   - Contextual actions (e.g., rewriting a draft, rechecking a clock, rearranging notes).
   - Subtle physiological changes (e.g., heartbeat speeding, breathing slowing, posture shifting).
   - Dialogues/inner thoughts that imply feelings without naming them.

4. **Self-check before finalizing**:
   - Scan and REMOVE any direct emotion terms, synonyms, or overlaps with option adjectives.

### Options Language Rule
- Options must be exactly 5 strings, each in the format: `"adjective_A → adjective_B"`.
- Both adjective_A and adjective_B must be **English adjectives**.
- None of the option adjectives may appear in the passage text.

### Question Format
- **Stem (Korean)**: "다음 글에 드러난 [인물]의 심경 변화로 가장 적절한 것은?"
- **Options**: 5 English patterns (adj1 → adj2).
- **Correct Answer**: 1-based index (1–5).
- **Explanation (Korean)**: Must justify the emotional inference **only from indirect contextual cues** and explain why distractors fail.

### Output Validation Rules
- Passage: 100–130 English words, no emotion vocabulary, no overlap with options.
- Options: exactly 5 strings, format "adj → adj".
- Correct Answer: integer 1–5.
- Explanation: Korean only, grounded in contextual cues.
- No extra fields, no markdown.

**Required JSON Output Format:**
{
  "question": "다음 글에 드러난 [character_name]의 심경 변화로 가장 적절한 것은?",
  "passage": "[100–130 word narrative with indirect emotional progression, no emotion words, no option overlap]",
  "options": ["adjective1 → adjective2", "adjective3 → adjective4", "adjective5 → adjective6", "adjective7 → adjective8", "adjective9 → adjective10"],
  "correct_answer": 1,
  "explanation": "[Korean explanation using only indirect contextual evidence]",
  "vocabulary_difficulty": "CSAT+O3000",
  "low_frequency_words": ["sponsor", "exhibit", "festival"]
}
```

---

## RC20 - 읽기 20번 (주장 파악)

```
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
- **Correct Answer**: Captures the author's **main** argument/recommendation (central claim)
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
```

---

## RC21 - 읽기 21번 (함축 의미 추론)

```
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
```

---

## RC22 - 읽기 22번 (요지 파악)

```
Create a CSAT Reading Item 22 (Main Point Identification) following these specifications.

ITEM CHARACTERISTICS & METHODOLOGY

Assessment Objective

Core Skill: The ability to identify the central argument of an explanatory text and synthesize key information to extract the main message.

Cognitive Process: Analyze the logical flow of the entire passage and derive the main point by integrating all information, not just from a single section.

Difficulty Target: 중상 (예상 정답률 70–80%, 변별도 0.2–0.3)

Abstractness & Complexity Controls

Abstractness Level (1–9): 5

Syntactic Complexity Targets (optional):

avg_words_per_sentence: 20.7

avg_clauses_per_sentence: 2.7

subordination_ratio: 0.5

Vocabulary Profile (optional): Academic and explanatory vocabulary

Text Type & Structure

Format: Explanatory or expository text

Structure Pattern: Randomly select one of the three:

Common Belief–Rebuttal: Introduce a common belief → Rebuttal → Author's true argument (main point).

Problem–Solution: Present a phenomenon or problem → Analyze causes → Offer and explain a solution (main point).

Argumentative Progression: Pose a question/phenomenon → Provide evidence/examples → Synthesize into a conclusion (main point).

Type-Specific Policy: The main point must not be identifiable from the first sentence alone; require integrated comprehension.

Language Specifications

Passage Length: 140–170 words (English only)

Sentence Style: Academic cohesion; complexity aligned to the above targets

Question & Options: Korean

Explanation: Korean, concise

Vocabulary Profile

"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: sponsor", "예: exhibit", "예: festival"] // examples; not mandatory to use

Question Format Requirements

Stem (Korean): "다음 글의 요지로 가장 적절한 것은?"

Options (Korean, 5지):

Write 5 Korean statements WITHOUT any leading numbering or markers.

❌ Do NOT prefix with "①", "②", "③", "④", "⑤", "1.", "-", bullets, or parentheses.

Distractors must include:

The common belief (if present at the beginning)

Partial/subordinate points mentioned in the passage

Related but non-central statements

A statement opposite to the main point

Correct Answer: Exactly one, matching the central message of the passage

Explanation (Korean)

Must include:

정답 근거: 본문 전개 + 유형별 핵심 근거

오답 배제: 각 선택지가 틀린 이유 간략히 (1–2문장씩)

OUTPUT (validator-compatible; JSON only)

Return ONLY valid JSON. Use the exact keys below.
correct_answer는 반드시 문자열 "1"~"5" 중 하나.
No extra keys beyond the schema.

{
"question": "다음 글의 요지로 가장 적절한 것은?",
"passage": "[140–170 word academic passage in English]",
"options": [
"Option sentence 1",
"Option sentence 2",
"Option sentence 3",
"Option sentence 4",
"Option sentence 5"
],
"correct_answer": "1",
"explanation": "정답 근거 및 오답 배제 이유를 한국어로 간결히 작성"
}

Hard Constraints (Self-Check)

Passage word count 140–170 (English only).
```

---

## RC24 - 읽기 24번 (제목 추론)

```
Create a CSAT Reading Item 24 (Title Inference) following these specifications.

## ITEM CHARACTERISTICS & METHODOLOGY
### Assessment Objective
- **Core Skill**: Inferring the most appropriate **title** that captures and synthesizes the passage's central idea.
- **Cognitive Process**: Identify contrast or development → Integrate all information → Express synthesis as an abstract title.
- **Difficulty Target**: 중상 (예상 정답률·변별도는 시스템 가이드에 준함)

### Text Type & Structure
- **Format**: Complex expository or analytical text (topics may include science, society, culture, technology, or philosophy).
- **Choose ONE structure pattern** and maintain it throughout:
  1) **Contrast–Synthesis**: Present a common assumption → show contrasting evidence → conclude with a synthesized insight.
  2) **Problem–Solution**: Present a realistic issue → explain an effective solution → synthesize the implication.
  3) **Historical–Analytical**: Connect a present phenomenon with historical context → analyze continuity and innovation → synthesize a balanced conclusion.
- **Opening Section (HARD)**: Must include a clear contrast between common belief and actual fact, using patterns like:
  - "It is natural to assume … However, …"
  - "People often believe … yet …"
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
2. Contains a clear contrast trigger near the beginning ("It is natural to assume … However …" or equivalent).
3. Includes at least one contrast cue ("however", "yet", "while", "whereas") and one synthesis cue ("therefore", "thus", "overall", "in sum", "taken together") near the conclusion.
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
```

---

(계속되는 프롬프트는 파일 크기 제한으로 인해 다음 파일에 작성됩니다)
