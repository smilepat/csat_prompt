PROMPT = r"""
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

Common Belief–Rebuttal: Introduce a common belief → Rebuttal → Author’s true argument (main point).

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

❌ Do NOT prefix with “①”, “②”, “③”, “④”, “⑤”, “1.”, “-”, bullets, or parentheses.

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
"""

SPEC = {
"type": "standard",
"components": ["question", "passage", "options", "correct_answer", "explanation"],
"processing_hints": {
"passage": "main_point_explanation"
},
"title": "읽기 22번 - 요지 파악"
}