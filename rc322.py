"""
Create a CSAT Reading Item 32 (Blank Inference - Phrase/Clause) following these specifications.

### 1. OPTION TYPE (MANDATORY)
All five options MUST be **abstract conceptual clauses or abstract conceptual phrases**, not actions.

Allowed:
- abstract noun phrase (conceptual)
- that-clause expressing a principle (NOT a fact or example)
- conceptual to-infinitive clause (NOT purpose)
- participial conceptual clause (being shaped by ~ / having been shaped by ~)
- passive conceptual clause (are sustained by ~ / are structured by ~)

Prohibited:
- simple action verb phrases (e.g., “people choose to ~”, “they fail to ~”)
- policy recommendations (e.g., “society should ban ~”)
- normative instructions (e.g., “we must promote ~”)
- examples or concrete statements
- sentence fragments (e.g., “short-term benefits”)
- clauses describing individual behavior
- clauses describing events in time (e.g., “historical conflicts have occurred”)

**Every option MUST operate at an abstract, system-level conceptual scale.**

---

### 2. REQUIRED GRAMMATICAL VARIETY (STRONG CONSTRAINT)
Across the 5 options, you MUST include EXACTLY:

- **1 passive conceptual clause**
- **1 present-perfect conceptual clause**
- **1 conceptual to-infinitive clause**
- Remaining 2 options MUST be either:
  - abstract noun phrases, OR
  - conceptual that-clauses

Example of correct coverage (for internal reference):
- (to-inf) “to acknowledge the interdependence of institutional norms”
- (present perfect) “has been shaped by enduring structural constraints”
- (passive) “are sustained by mutually reinforcing civic principles”
- (noun phrase) “the contingent nature of democratic legitimacy”
- (that-clause) “that enduring pluralism relies on negotiated boundaries”

---

### 3. LENGTH CONSTRAINT (MANDATORY)
Each option MUST be **9–15 words**.

Prohibited:
- ≤ 7 words (too short)
- ≥ 17 words (too long)

---

### 4. GRAMMATICAL COMPATIBILITY (ABSOLUTE REQUIREMENT)
The option MUST be grammatically compatible with the blank sentence.

Examples:
- If the blank follows **that**, option MUST be a clause that can follow “that”.
- If the blank follows **because**, option MUST be a full clause.
- If the blank is inside a **passive slot**, option MUST be a complement compatible with passive.
- If the blank requires a **finite clause**, options may NOT be noun phrases.

**If ANY option is incompatible with the blank sentence’s grammatical frame, REGENERATE ALL OPTIONS.**

---

### 5. SEMANTIC SCOPE & RELEVANCE (MANDATORY)
All options MUST:

- be at the same abstractness level as the passage
- express structural, systemic, or conceptual relationships
- avoid repeating passage wording
- differ logically (scope misalignment, nuance shifts) but be conceptually relevant
- avoid contradictions unless intended as a distractor
- avoid overly narrow or concrete claims

---

### 6. DISTRACTOR QUALITY RULES
A distractor is valid only if it is:

- relevant but logically insufficient, OR
- conceptually plausible but misaligned, OR
- overly generalized or overly narrow, OR
- missing critical nuance, OR
- incorrect at the macro-argument level

Distractors MUST:
- still be grammatical
- still be conceptual
- NOT be factually absurd
- NOT be fragmentary

---

### 7. HARD VALIDATION BEFORE OUTPUT
Before producing the JSON, you MUST verify:

1. **Each option satisfies the required grammatical type.**
2. **Options include exactly one passive, one present-perfect, one conceptual to-inf.**
3. **All options are 9–15 words in length.**
4. **All options are abstract conceptual clauses/phrases.**
5. **NO option is action-based or behavioral.**
6. **Every option fits grammatically into the blank sentence.**
7. **Correct option is the ONLY one that completes the conceptual argument.**

If ANY requirement fails, REGENERATE ALL OPTIONS.


============================================================
## 8. REQUIRED JSON OUTPUT FORMAT
============================================================

{
  \"question\": \"다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?\",
  \"passage\": \"[130–150 word academic passage with one embedded blank]\",

  \"options\": [
    \"abstract conceptual phrase/clause option\",
    \"abstract conceptual phrase/clause option\",
    \"abstract conceptual phrase/clause option\",
    \"abstract conceptual phrase/clause option\",
    \"abstract conceptual phrase/clause option\"
  ],

  \"answer\": 2,

  \"explanation\": \"[한국어 해설: 정답 근거 및 오답 배제 이유]\",

  \"metadata\": {
    \"item_number\": 32,
    \"item_type\": \"Reading\",
    \"skill_focus\": \"Inference (Phrase/Clause)\",
    \"difficulty\": \"High\",
    \"abstractness_level\": 8,
    \"syntactic_complexity\": {
      \"avg_words_per_sentence\": 19.0,
      \"avg_clauses_per_sentence\": 2.2,
      \"subordination_ratio\": 0.4
    },
    \"vocabulary_difficulty\": \"CSAT+AWL\",
    \"passage_word_count\": 140,
    \"TYPE_SPECIFIC_METADATA\": \"focus: conceptual logical transition\",
    \"low_frequency_words\": []
  }
}
"""