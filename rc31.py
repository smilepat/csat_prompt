# app/prompts/items/rc31.py

"""
RC31 — Reading 31: Blank Inference (Word/Phrase)

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC31 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 31 (Blank Inference - Word/Phrase) following these specifications:

## ITEM CHARACTERISTICS & METHODOLOGY

### Assessment Objective
- **Core Skill**: 문맥을 통한 핵심 어휘/구 추론 능력 측정
- **Processing Pattern**: 문맥 분석 → 논리적 관계(인과, 대조 등) 파악 → 빈칸의 기능 확인 → 적절한 어휘/구 추론
- **Evaluation Focus**: 글의 논리적 흐름을 완성하는 핵심 개념어의 정확한 추론 능력

### Discourse Structure
- **Pattern**: 주제 제시 → 배경 설명 → 핵심 논점 → **빈칸 위치** → 구체적 사례/상술 → 결론
- **Flow**: 개념 도입 → 맥락 설정 → 중심 아이디어 → **추론 지점** → 예시/근거 → 종합
- **Key Positioning**: 빈칸은 텍스트의 핵심 개념을 요약하거나 논리적 연결을 담당하는 위치에 배치

### Language Specifications
- **Passage Length**: 130–150 words
- **Sentence Complexity**: Complex, with dense logical relationships (e.g., cause-effect, contrast) to support inference. (Avg. 2.1–2.3 clauses per sentence)
- **Vocabulary Level**: Advanced academic and abstract vocabulary.
- **Reading Level**: High academic complexity, focused on logical inference.

### Vocabulary Profile
"vocabulary_difficulty": "CSAT+O3000",
"low_frequency_words": ["예: statistic", "예: percentage"]  // 예시 단어, 반드시 사용해야 하는 것은 아님

### Question Format Requirements
- **Stem**: "다음 글의 빈칸에 들어갈 말로 가장 적절한 것은?"
- **Options**: 5개 선택지, 모두 빈칸에 들어갈 수 있는 영어 단어 또는 짧은 구
- **Correct Answer**: 문맥의 논리적 흐름에 완벽히 부합하는 핵심 어휘/구
- **Distractors**: 부분적으로 관련되거나, 반의어이거나, 논리적으로 부적절한 어휘/구들

### Content Generation Guidelines
- Any argumentative or explanatory topic requiring logical reasoning
- Any concept with cause-effect relationships or logical progressions
- Any subject requiring inference and logical connection
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
"""

SPEC = {
    "type": "reading_blank_word_phrase",
    "components": [
        "question",
        "passage",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "word_count_passage": [130, 150],
        "passage_format": "blank_filling",
        "answer_indexing": "1-based"
    },
    "title": "읽기 31번 - 빈칸 추론 (단어/구)"
}
