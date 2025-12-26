# app/prompts/items/lc06.py

"""
LC06 — Listening 6: Payment Amount (강화 최종판 + CRITICAL MATH RULE)
- 정신적 계산(정수) / 최종 금액 미제시 / 마지막 두 턴 무숫자
- 실제 수능 스타일: 110–130 words, 7–9 turns, 거래 맥락 풍부화
- 정률 할인(%) 사용 시 반드시 정수 결과가 되도록 설계 (반올림 절대 금지, 불일치 시 내부 재생성)
- BASE 공통 규칙(영어 대본 / 한국어 발문·해설 / JSON만 출력 등)은 base.py에서 주입됩니다.
"""

PROMPT = r"""
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
  - EN: "That’ll be", "It comes to", "The total is", "Altogether", "You’ll pay", "Let me calculate"
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
"""

SPEC = {
    "type": "listening_payment_amount",
    "components": [
        "question",
        "transcript",
        "options",
        "correct_answer",
        "explanation",
        "vocabulary_difficulty",
        "low_frequency_words"
    ],
    "processing_hints": {
        "word_count_transcript": [110, 130],
        "speaker_markers": ["M:", "W:"],
        "enforce_marker_per_line": True,
        "min_turns": 7,
        "max_turns": 9,
        "integers_only": True,
        "discount_mode": ["flat", "percent", "none_allowed"],
        "allowed_percentages": [10, 20, 25, 50],
        "percent_result_must_be_integer": True,
        "regenerate_if_percent_not_integer": True,
        "repeat_key_numbers_at_most_once": True,
        "forbidden_regex": [
            r"(?i)\b(that('|’)ll be|it comes to|total is|altogether|let me calculate|you('|\s)?ll pay|how much (will it be|is it))\b",
            r"[$€£₩]\s*\d",
            r"\b(총액|합계|금액|모두 합하면|합치면)\b.*\d",
            r"\b(얼마(예요|인가요))\b"
        ],
        "last_two_turns_digit_free": True,
        "last_two_turns_forbidden_words_regex": r"(?i)\b(one|two|three|four|five|six|seven|eight|nine|ten|hundred|thousand|dollar(s)?|won)\b|[0-9]|[$€£₩]",
        "option_currency_from_transcript": True,
        "option_format_regex_usd": r"^\$\d{1,3}(,\d{3})*$|^\$\d+$",
        "option_format_regex_krw": r"^\d{1,3}(,\d{3})*원$",
        "option_spacing_min": 2,
        "answer_indexing": "1-based"
    },
    "special_features": [
        "multi-step integer calculation",
        "no explicit total in transcript",
        "last-two-turns digit-free",
        "no numeric answer leakage",
        "optional explicit no-discount trap",
        "test-taker must compute",
        "length-validated regeneration",
        "percent-discount integer guarantee"
    ],
    "title": "듣기 6번 - 지불 금액(강화 최종판 + CRITICAL MATH RULE)"
}
TEMPLATE = PROMPT
def template(): return PROMPT