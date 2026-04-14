# AI Detection Reference — How Turnitin and Grammarly Detect AI-Written Text

## Purpose

This document is a comprehensive reference for understanding how AI detectors work, what patterns they flag, and what specific linguistic markers distinguish AI-generated text from human-written text. Use this to guide adversarial self-checking when rewriting text to pass AI detection.

---

## 1. HOW TURNITIN'S AI DETECTION WORKS

### Architecture

Turnitin uses a **segment-based** approach, not whole-document analysis:

1. **Segmentation:** The document is broken into ~300-word segments.
2. **Per-segment analysis:** Each segment is analysed independently for perplexity, burstiness, word choice, and structural patterns.
3. **Classification:** Each segment is classified as "Human" or "AI."
4. **Score calculation:** The final AI percentage = (segments flagged as AI / total segments) × 100.
5. **Flagging:** Flagged segments are highlighted for instructor review.

### Key Implication

Because analysis is segment-based, a single AI-sounding paragraph in an otherwise human document will only flag that one segment (~10% of a 3,000-word paper). Conversely, if AI patterns are distributed evenly throughout, most segments will flag even if mixed with human text.

### What Turnitin Measures

Turnitin's model was trained on blended human and AI-generated text corpora. It evaluates:

- **Perplexity** (word-level predictability)
- **Burstiness** (variation in sentence length and structure across the document)
- **Word choice patterns** (vocabulary distribution)
- **Long-range statistical dependencies** beyond just perplexity/burstiness
- **Stylistic consistency** within and across segments

### Score Interpretation (Typical University Thresholds)

| Score | Interpretation | Typical Action |
|-------|---------------|----------------|
| 0% | No AI detected | None |
| 1–15% | Low probability | Noted on file |
| 16–30% | Moderate signals | Instructor reviews; student may be asked to explain |
| 31–50% | Significant signals | Academic integrity investigation likely |
| 51–80% | High probability | Formal investigation |
| 81–100% | Very high probability | Near-certain investigation |

### Turnitin's Known Limitations

- ~4% false positive rate on fully human-written text.
- ESL students face 6–8% false positive rates.
- Formal, structured academic writing naturally exhibits low perplexity/burstiness, overlapping with AI patterns.
- Technical and formulaic writing (lab reports, lit reviews) triggers more false positives.
- The 2026 model specifically targets "humaniser" tools designed to evade detection.
- Several major universities (Curtin, Vanderbilt, University of Cape Town, UC system, Johns Hopkins, U of Queensland) have disabled Turnitin's AI detection due to reliability concerns.

---

## 2. HOW GRAMMARLY'S AI DETECTION WORKS

Grammarly launched an AI detector (grammarly.com/ai-detector) and an AI humaniser (grammarly.com/ai-humanizer) in 2025.

### Key Facts

- Less accurate than Turnitin or GPTZero for AI detection.
- Higher false positive rate for formal/academic human writing (~34% vs ~15–18% for dedicated tools).
- Less reliable at detecting Claude-generated text compared to ChatGPT.
- Results can be inconsistent across multiple runs of the same text.
- Its own AI rewrite features ("improve it," "rewrite") can trigger AI detection on originally human-written text.

### Important Distinction for Students

- **Basic grammar corrections** (typos, commas, subject-verb agreement): Do NOT trigger AI detectors.
- **AI-powered rewrite features** (rewrite sentences, tone adjustments, "improve clarity"): CAN trigger AI detectors because these use generative AI to produce new text.

---

## 3. THE TWO CORE METRICS: PERPLEXITY AND BURSTINESS

### Perplexity

**Definition:** How predictable/surprising the text is — how well a language model can predict the next word given the preceding context.

- **Low perplexity** = highly predictable word choices → AI-like.
- **High perplexity** = surprising, less predictable word choices → human-like.

**Example:** "It's raining out, so take your ___"
- "umbrella" = low perplexity (predictable)
- "monkey" = high perplexity (surprising)

**Why AI text has low perplexity:** LLMs select statistically probable next tokens. They converge on "safe," common word choices. Humans make idiosyncratic, context-dependent, sometimes surprising word choices.

### Burstiness

**Definition:** How much variation exists in sentence length, structure, and local style across the document.

- **Low burstiness** = uniform sentence lengths and structures → AI-like.
- **High burstiness** = varied sentence lengths (mixing short punchy sentences with long complex ones) → human-like.

**Why AI text has low burstiness:** LLMs apply the same token-selection rules uniformly, producing consistent rhythm. Humans naturally vary their pace — they write short declarative sentences, then long subordinate-clause-heavy ones, then medium ones, in unpredictable patterns.

### Key Insight

**Low perplexity + low burstiness together** is the strongest AI signal. Academic writing naturally tends toward lower perplexity (formal vocabulary, discipline-specific terms) but human academic writing still shows higher burstiness than AI academic writing.

---

## 4. SPECIFIC AI WRITING PATTERNS TO ELIMINATE

### 4.1 Overused AI Vocabulary

The following words have been statistically identified as dramatically overused in AI-generated text relative to human baselines. Eliminating or drastically reducing these is essential.

**Highest-signal words (25x+ increase since 2022):**
- delve, delves, delving
- showcasing, showcases
- underscores, underscoring

**High-signal words (5–10x increase):**
- comprehensive, crucial, pivotal, nuanced, multifaceted
- landscape, tapestry, realm, interplay
- robust, seamless, vibrant, dynamic
- illuminate, elucidate, underscore
- navigate, embark, foster, harness
- intricate, intricacies, meticulous, meticulously
- paramount, testament, groundbreaking
- leverage, synergy, holistic

**Moderate-signal words (overused but not exclusively AI):**
- moreover, furthermore, additionally (as paragraph starters)
- facilitate, enhance, bolster
- explore, exploration
- framework, architecture (when overused)
- operationalise (when overused)
- noteworthy, notably

**Transition words/phrases overused by AI:**
- "Furthermore," / "Moreover," / "Additionally," as sentence/paragraph openers
- "In summary" / "In conclusion" / "In essence"
- "It is important to note" / "It should be noted"
- "In today's ever-evolving world/landscape"
- "It is worth emphasising/highlighting"
- "This underscores the importance of"

### 4.2 Structural Patterns That Signal AI

**The Rule of Three:**
AI overuses tripartite lists: "adjective, adjective, and adjective" or "phrase, phrase, and phrase." Humans do this sometimes but AI does it systematically and repetitively.

**Symmetrical paragraph structure:**
Every paragraph follows the same pattern (topic sentence → evidence → evaluation → link). Human paragraphs vary in structure.

**Uniform paragraph length:**
AI tends to produce paragraphs of very similar word counts (e.g., all 120–150 words). Humans write paragraphs of varied lengths.

**Section summaries:**
AI frequently concludes paragraphs/sections with explicit summary sentences beginning "In summary" or "Overall." This is uncommon in natural academic prose.

**Announcing and summarising:**
AI both announces what a section will do AND summarises what it has done. Human writers usually do one or the other.

**Formulaic meta-commentary:**
- "Applying the [framework] lens..."
- "Through the lens of [theory]..."
- "This analysis reveals that..."
- "[Theory] provides a useful framework for understanding..."

**Excessive hedging stacks:**
AI piles qualifiers: "While it is important to acknowledge the potential limitations, the evidence suggests that..." Humans hedge more selectively.

**Balanced "on one hand / on the other hand" structures:**
AI systematically presents both sides in every paragraph. Humans sometimes commit to a position without immediate qualification.

### 4.3 Sentence-Level Patterns

**Uniform sentence length:**
AI sentences cluster around 20–25 words. Human sentences range from 5 to 45+ words within a single paragraph.

**Predictable sentence openers:**
AI cycles through: "The...", "This...", "These...", "However,...", "Furthermore,...", "Additionally,..." Human writers use more varied openers including dependent clauses, prepositional phrases, participial phrases, and occasional single-word or two-word openers.

**Nominalisation overuse:**
AI favours abstract nominalisations over concrete verbs. "The implementation of the policy" instead of "implementing the policy" or "when the government implemented the policy."

**Passive voice consistency:**
AI uses passive voice at a consistent rate throughout. Humans shift between active and passive depending on emphasis needs.

**Excessive use of "This" as sentence opener:**
AI frequently begins consecutive sentences with "This [noun]..." or "This [verb]s..." creating a monotonous referential chain.

### 4.4 Document-Level Patterns

**Statistical regression to the mean:**
AI smooths over specific, unusual facts and replaces them with generic, positive descriptions. The content becomes simultaneously less specific and more exaggerated — "shouting louder and louder that a portrait shows a uniquely important person, while the portrait itself is fading from a sharp photograph into a blurry, generic sketch."

**Absence of genuine authorial voice:**
AI text lacks idiosyncratic choices that mark individual writers — unusual collocations, discipline-specific shorthand, minor grammatical preferences, favourite sentence structures.

**Over-cohesion:**
AI text is too cohesive — every paragraph connects smoothly to the next with explicit transitions. Human academic writing sometimes has rougher transitions, abrupt topic shifts, or implicit connections that require reader inference.

**Sentiment consistency:**
AI maintains a uniform positive/neutral evaluative tone. Human academic writing shifts in evaluative stance — sometimes critical, sometimes approving, sometimes uncertain — within a single section.

---

## 5. WHAT MAKES TEXT READ AS HUMAN

### 5.1 Vocabulary Variation

- Use common, concrete words instead of ornate synonyms.
- Alternate between formal and slightly less formal register (within academic bounds).
- Use discipline-specific jargon naturally, not performed.
- Avoid stacking evaluative adjectives.

### 5.2 Sentence Variation (Burstiness)

- Mix sentence lengths deliberately: some under 10 words, some over 35.
- Use different sentence types: declarative, conditional, rhetorical questions, concessive.
- Start sentences with different structures: dependent clauses, prepositional phrases, subjects, adverbs, participial phrases.
- Occasionally use fragments for emphasis (sparingly in academic writing — use short declarative sentences instead).

### 5.3 Paragraph Variation

- Vary paragraph lengths: some 2–3 sentences, some 5–7 sentences.
- Don't follow the same internal structure in every paragraph.
- Begin some paragraphs with evidence, some with claims, some with concessions, some with questions.

### 5.4 Authorial Voice Markers

- Include occasional evaluative commentary that reflects genuine analytical engagement.
- Use concrete, specific language over abstract generalisations.
- Allow some findings to stand before qualifying them (not every positive immediately qualified).
- Include minor stylistic idiosyncrasies consistent with the author's established voice.
- Reference specific details from the primary source material rather than generic descriptions.

### 5.5 Imperfection Signals

These are NOT about deliberately introducing errors, but about allowing natural human writing patterns:

- Slightly uneven paragraph lengths.
- Transitions that work but aren't perfectly smooth.
- Occasional short sentences that just state a fact plainly.
- Vocabulary preferences (humans have favourite words they return to — this is different from AI repetition because the word choice is idiosyncratic).

---

## 6. ADVERSARIAL SELF-CHECK PROTOCOL

When reviewing rewritten text for AI detection risk, check each ~300-word segment for:

1. **Vocabulary scan:** Count flagged AI words from Section 4.1. Target: fewer than 2 per segment.
2. **Sentence length variance:** Calculate the standard deviation of sentence lengths. Target: SD > 8 words.
3. **Sentence opener diversity:** List the first 3 words of each sentence. Target: no more than 2 sentences starting with the same word in a segment.
4. **Paragraph length variance:** Measure paragraph word counts. Target: at least 30% variation between shortest and longest.
5. **Transition diversity:** Check paragraph-opening transitions. Target: no "Furthermore/Moreover/Additionally" as paragraph openers within the same segment.
6. **Rule-of-three check:** Count tripartite list structures. Target: no more than 1 per segment.
7. **Meta-commentary check:** Flag any sentences that announce what the analysis will show or summarise what it has shown. Target: eliminate or minimise.
8. **Specificity check:** Each analytical paragraph should contain at least one concrete, specific reference to the primary source material (page numbers, specific provisions, exact wording).
9. **Evaluative variation:** Check that evaluative stance varies within sections — not uniformly positive or uniformly critical.
10. **Cohesion naturalness:** Ensure transitions between paragraphs aren't all explicit. Some implicit connections are fine.

---

## 7. KEY RESEARCH FINDINGS

- PNAS study (Reinhart et al., 2025): LLMs show systematic grammatical and rhetorical differences from humans across all 66 Biber features. Instruction-tuned models show larger differences than base models. LLMs struggle to match human stylistic variation.
- PubMed analysis of 14 million abstracts: Words like "delves" increased 25x since 2022. "Showcasing" and "underscores" increased 9x. ~15% of papers from non-English-speaking countries estimated to be AI-processed.
- Nature study (O'Sullivan, 2025): AI systems produce "tightly grouped clusters" reflecting uniform patterns. Human texts show far greater variation and individuality.
- Pangram Labs: Perplexity/burstiness-based detectors have higher false positive rates for ESL students and high-achieving students writing formally — because academic writing rewards the same traits detectors flag as AI.

---

## 8. SPECIAL CONSIDERATIONS FOR THIS DISSERTATION

This dissertation is:
- **Formal academic writing** (inherently lower perplexity) — must compensate with high burstiness.
- **Education policy analysis** — uses specialised vocabulary that overlaps with AI-common words (framework, implementation, policy, inclusive).
- **Document analysis methodology** — naturally involves structured, systematic language.
- **British English** — Turnitin handles British English but some detection models are US-English-biased.

**Strategy:** The primary defence against AI detection for this text is:
1. High burstiness (varied sentence lengths and structures).
2. Concrete specificity (references to specific policy provisions, page numbers, exact wordings).
3. Genuine analytical voice (evaluative shifts, honest acknowledgements of ambiguity).
4. Vocabulary diversification (rotating synonyms, avoiding AI-overused words).
5. Structural unpredictability (varied paragraph lengths and internal structures).
