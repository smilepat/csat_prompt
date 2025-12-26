# lc16_17.py

ITEM_ID = "LC16_17"
TITLE = "듣기 16-17번 - 장문 듣기 (세트형)"

CONTENT = """Create a CSAT Listening Item 16-17 (Long Listening Set) following these specifications.

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
"""

SPEC = {
    "type": "set",
    "set_size": 2,
    "start_number": 16,
    "components": [
        "transcript",
        "questions",
        "vocabulary_difficulty",
        "low_frequency_words"
    ],
    "processing_hints": {
        "must_concretize_speaker_placeholder": True,
        "must_concretize_category_placeholder": True,
        "enforce_word_count_min": 180,
        "enforce_word_count_max": 220
    },
}

PROMPT = {
    ITEM_ID: {
        "title": TITLE,
        "content": CONTENT,
        "spec": SPEC,
    }
}


def get_prompt() -> dict:
    """Return a mapping compatible with a PromptManager registry."""
    return PROMPT
