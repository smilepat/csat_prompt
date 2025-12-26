# app/prompts/items/rc19.py

"""
RC19 — Reading 19: Emotional Change (심경 변화)

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC19 유형(심경 변화)에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""
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
"""

SPEC = {
    "type": "reading_emotional_change",
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
        "word_count_passage": [100, 130],
        "options_pattern": r"^[A-Za-z\-]+(?:\s[A-Za-z\-]+)*\s→\s[A-Za-z\-]+(?:\s[A-Za-z\-]+)*$",
        "answer_indexing": "1-based",
        "ban_emotion_terms": True,
        "ban_synonyms_of_options": True,
        "ban_direct_emotion_actions": True,
        "ban_option_overlap_in_passage": True
    },
    "special_features": ["emotional_change", "strict_no_overlap"],
    "title": "읽기 19번 - 심경 변화"
}
