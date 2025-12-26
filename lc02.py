# app/prompts/items/lc02.py

"""
LC02 — Listening 2: Opinion Identification

Notes
- BASE 공통 규칙(영어 대본 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 LC02 유형(대화문에서 특정 화자의 '의견' 파악)에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""
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
- [ ] Distractors가 대상 화자의 ‘일관된 의견’과 구분되는지
"""

SPEC = {
    "type": "listening_opinion",
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
        "word_count_transcript": [80, 100],
        "speaker_markers": ["M:", "W:"],
        "enforce_marker_per_line": True,
        "dialogue_alternation": True,
        "answer_indexing": "1-based"
    },
    "title": "듣기 2번 - 의견 파악"
}
