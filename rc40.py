# app/prompts/items/rc40.py

"""
RC40 — Reading 40: Summary Completion

Note:
- BASE 공통 규칙(영어 본문 / 한국어 발문·해설, JSON만 출력 등)은 base.py에서 주입됩니다.
- 이 파일은 RC40 유형에 특화된 요구사항만 담습니다.
- item-specific 지시가 BASE와 충돌 시, item-specific(본 프롬프트)가 우선합니다.
"""

PROMPT = r"""Create a CSAT Reading Item 40 (Summary Completion) following these specifications:

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
- **Passage Length**:  
  - The passage must consist of **9–11 sentences**.  
  - Each sentence should be **information-dense and 18–22 words long**.  
  - The overall passage length should therefore be approximately **150–170 words**.  
  - Avoid producing fewer than 9 sentences or more than 11 sentences.
- **Sentence Complexity**: 복잡하고 정보 밀도가 높을 것
- **Vocabulary Level**: 학술적이고 추상적인 어휘 포함
- **Reading Level**: 고난도 종합 추론 요구

### Vocabulary Profile
"vocabulary_difficulty": "AWL"

### Question Format Requirements
- **Stem**: "다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은? [3점]"
- **Summary**: 영어 한 문장, (A)와 (B) 두 빈칸 포함

### Summary Template Structure
- One complete English sentence summarizing the passage
- (A), (B)는 <u>    (A)    </u>, <u>    (B)    </u>로 표기
- 두 개념의 **관계나 대비**가 반드시 드러나야 함 (단순 열거 금지)
- (A) and (B) must represent the two core concepts that organize the entire passage.
- The blanks (A) and (B) must be placed in positions where they share the same grammatical category 
  (e.g., both nouns, both verbs, both adjectives).
- **Avoid noun-only templates whenever possible.**
- At least half of all generated items must use **verb-verb** or **adjective-adjective** structures.  

- **STRICT LENGTH & COMPLEXITY REQUIREMENTS**
  - The summary template must always contain **at least three clauses** (one main clause + two subordinate clauses).  
  - The template must include **at least two different subordinating connectors** (e.g., although, because, while, if, what, when, even though, unless).  
  - Templates using only a **relative clause ("which …") + main clause** are invalid.  
  - Templates using only a **not only–but also** pattern are invalid.  
    - If "not only–but also" is used, it must be embedded within a longer multi-clause sentence that also contains an additional subordinate clause (e.g., conditional, concessive, or noun clause).  
  - Sentence length must be **25–35 words** and span **two or more lines** when written.  
  - Templates must rotate across **relative, conditional, concessive, and noun clauses**, and at least one **non-relative clause** must appear in every item.  

- Example acceptable structures (must vary):
  - **Conditional + Concessive + Result** → "If sustainable living <u>  (A)  </u> waste, although many resist the effort, it ultimately <u>  (B)  </u> responsibility across communities."  
  - **Noun Clause + Main + Relative** → "What students <u>  (A)  </u> in their early years often <u>  (B)  </u> their success, which later determines opportunities."  
  - **Mixed (3-Clause)** → "Although recycling <u>  (A)  </u> participation, what governments fail to do often <u>  (B)  </u> the programs' effectiveness, because enforcement remains inconsistent."  
  - **Embedded not only–but also + Subordinate** → "Although seasonal observation not only <u>  (A)  </u> understanding but also <u>  (B)  </u> responsibility, it becomes meaningful because ecosystems reveal both resilience and vulnerability."  

### Option Format
- All options must follow the format **"(A): word - (B): word"**.
- Each option must be a **single English word only** (no multi-word phrases).
- (A) and (B) must share the same grammatical category, consistent with the Summary Template.
- Do NOT generate only nouns. Ensure that at least one item uses verb-verb options and another uses adjective-adjective options.
- Permitted categories: 
  - Verb - Verb (e.g., "reduces / preserves")  
  - Adjective - Adjective (e.g., "flexible / effective")  
  - Verb - Noun or Adjective - Noun (allowed only if the Template requires it)  
  - Noun - Noun (allowed, but should be the minority)  
- Distractors must be partially plausible but ultimately fail to capture the passage's overall meaning.
- At least one distractor should have (A) correct but (B) incorrect, and another should have (B) correct but (A) incorrect.

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
"""

SPEC = {
    "type": "reading_summary_completion",
    "components": [
        "question",
        "passage",
        "summary_template",
        "options",
        "correct_answer",
        "explanation"
    ],
    "processing_hints": {
        "passage_sentences": [9, 11],
        "passage_words_per_sentence": [18, 22],
        "summary_format": "dual_blanks_ab_with_contrast_or_relation",
        "answer_indexing": "1-based"
    },
    "title": "읽기 40번 - 요약문 완성"
}
