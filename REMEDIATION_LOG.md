# REMEDIATION LOG — Targeted Fixes from Adversarial Audit

**Date:** April 14, 2026  
**Input:** DISSERTATION_HUMANISED.docx  
**Output:** DISSERTATION_REMEDIATED.docx  

---

## FIX 1: Em Dash Removal

**Before:** 37 em dashes  
**After:** 0 em dashes  
**Target:** ≤ 4  
**Result:** PASS

### Replacements Made (37 total)

| Location | Original Pattern | Replacement |
|----------|-----------------|-------------|
| Abstract (para 122) | `) — most obviously` | `) , most obviously` (comma) |
| Abstract (para 123) | `developments — including...regions —` | Commas (paired parenthetical) |
| §1.1 (para 131) | `settings — a practice` | Comma |
| §1.1 (para 133) | `limitations — making` | Comma |
| §1.1 (para 134) | `cultures — a concern` | Comma |
| §2.2.1 (para 178) | `attitudes — including` | Comma |
| §2.2.3 (para 182) | `factors — both` | Comma |
| §2.2.4 (para 184) | `inconsistent — affirming` | Colon |
| §2.4.1 (para 199) | `inclusion — as opposed...integration —` | Commas (restructured) |
| §2.4.4 (para 201) | `effects — pointing` | Comma |
| §2.5 (para 211) | `literature — particularly` | Comma |
| §2.5 (para 211) | `(2010) —` | Comma |
| §3.2 (para 221) | `process — ...synthesis —` | Parentheses |
| §3.5 (para 230) | `documents — particularly...Policy —` | Commas |
| §4.2 (para 253) | `concepts — ...Learning —` | Parentheses |
| §4.3 (para 259) | Two paired parentheticals (4 dashes) | Parentheses |
| §4.3 (para 262) | `enacted — in some` | Comma |
| §4.4.3 (para 276) | `2004 — four` | Comma |
| §4.4.5 (para 283) | Paired parenthetical (2 dashes) | Parentheses |
| §4.5 (para 287) | `emerge — particularly` | Comma |
| §4.6 (para 291) | Paired parenthetical (2 dashes) | Commas |
| §5.3 (para 302) | `emerge — most` | Comma |
| §5.3 (para 305) | Paired parenthetical (2 dashes) | Parentheses |
| §5.4 (para 310) | Paired parenthetical (2 dashes) | Commas |
| §5.7 (para 325) | `first step — not because` | Period + new sentence |

---

## FIX 2: Sentence Opener Diversification

**Sections fixed:** 28  
**Sections passing (≤2 per opener word):** 28/28  
**Result:** PASS

### Per-Section Changes

| Section | Opener Word | Before | After | Technique |
|---------|------------|--------|-------|-----------|
| §1.1 | "The" | 7 | 2 | Prepositional fronting, participial fronting, passive reframe |
| §1.8 | "Chapter" | 5 | 2 | Object fronting, prepositional phrase, adverbial opener |
| §2.2.4 | "The" | 3 | 2 | Passive reframe |
| §2.3 | "A" | 3 | 2 | Ordinal opener ("Second,") |
| §2.4.1 | "The" | 3 | 2 | Prepositional fronting |
| §2.4.2 | "The" | 3 | 2 | Prepositional fronting |
| §2.4.2 | "When" | 3 | 2 | "Where" substitution |
| §2.4.4 | "The" | 5 | 2 | Adverbial, prepositional, participial fronting |
| §2.4.4 | "In" | 3 | 2 | "During" substitution |
| §2.4.5 | "The" | 3 | 2 | "Among" opener |
| §3.2 | "The" | 8 | 2 | Adverbial, passive, participial, prepositional |
| §3.2 | "This" | 3 | 2 | "Such" substitution |
| §3.3 | "The" | 4 | 2 | Prepositional fronting, participial |
| §3.4 | "The" | 6 | 2 | Passive, prepositional, participial, quantified |
| §3.4 | "Research" | 4 | 2 | "For Research Question..." prepositional |
| §3.5 | "The" | 7 | 2 | Object fronting, participial, passive, adverbial |
| §4.2 | "The" | 5 | 2 | Prepositional, restructured |
| §4.2 | "At" | 3 | 2 | Restructured to declarative |
| §4.3 | "The" | 5 | 2 | Adverbial, citation-led, restructured |
| §4.3 | "In" | 3 | 2 | Citation-led ("Lipsky's framework suggests...") |
| §4.4.3 | "The" | 6 | 2 | Object fronting, prepositional, passive |
| §4.4.5 | "The" | 6 | 2 | Passive, citation-led, restructured, evaluative |
| §4.5 | "The" | 9 | 2 | Adverbial, passive, restructured |
| §4.5 | "Evidence" | 3 | 2 | Passive reframe |
| §4.5 | "Working" | 3 | 2 | Shortened to "Proposition" |
| §4.6 | "The" | 3 | 2 | Subject swap ("Chapter 5 takes up...") |
| §5.2 | "The" | 6 | 2 | Participial, adverbial, passive, restructured |
| §5.2 | "Chapter" | 4 | 2 | Passive, restructured |
| §5.3 | "The" | 10 | 2 | Participial, passive, evaluative, restructured |
| §5.4 | "The" | 9 | 2 | Passive, participial, restructured |
| §5.4 | "Recommendation" | 5 | 2 | "Second,", "Third,", "Fourth," openers |
| §5.4 | "This" | 3 | 2 | "Such" substitution |
| §5.7 | "The" | 4 | 2 | Adverbial ("Perhaps"), restructured |

---

## FIX 3: Rule-of-Three Reduction

**Sections fixed:** 17+  
**Sections passing (≤1 tripartite per 300-word segment):** 28/28  
**Result:** PASS

### Strategies Applied

| Strategy | Count | Example |
|----------|-------|---------|
| Two-part + "as well as" | 15 | "X and Y, as well as Z" |
| Two-part + "compounded by" | 4 | "X and Y, compounded by Z" |
| Two-part + "alongside" | 5 | "X and Y alongside Z" |
| Two-part + "together with" | 6 | "X and Y, together with Z" |
| Two-part + subordinate clause | 4 | "X and Y, while Z" |
| Two-part + "followed by" | 2 | "X and Y followed by Z" |
| Restructured prose | 5 | Various restructurings |

### Sections with Changes

- §1.1: 5 triples restructured
- §1.7: 5 triples restructured
- §1.8: 3 triples restructured
- §2.2.4: 1 triple restructured
- §2.3: 3 triples restructured
- §2.4.2: 2 triples restructured
- §2.4.5: 5 triples restructured
- §3.2: 5 triples restructured
- §3.3: 1 triple restructured
- §3.9: 4 triples restructured
- §4.3: 2 triples restructured
- §4.4.4: 2 triples restructured
- §4.5: 2 triples restructured
- §5.2: 3 triples restructured
- §5.3: 1 triple restructured
- §5.4: 10 triples restructured
- §5.7: 4 triples restructured

---

## FIX 4: Spelling Corrections

| Location | Before | After |
|----------|--------|-------|
| §1.7 (para 169) | judgments | judgements |
| §3.9 (para 238) | judgments | judgements |

**Verification:** 0 occurrences of "judgments" remaining in body text.  
**Note:** "Organization" (×2 in References), "Center" (×1 in References), and "conceptualized" (×1 in References) left unchanged as they are proper nouns or published titles.

---

## VERIFICATION RESULTS

| Check | Target | Result | Status |
|-------|--------|--------|--------|
| A. Em Dash Count | ≤ 4 | 0 | PASS |
| B. Sentence Opener Diversity | ≤ 2 per word per section | 28/28 sections pass | PASS |
| C. Rule-of-Three Count | ≤ 1 per 300-word segment | 28/28 sections pass | PASS |
| D. Citation Preservation | 0 differences | 39/39 citations preserved | PASS |
| E. Meaning Preservation | Spot-checked | No meaning changes introduced | PASS |
| F. British English ("judgments") | 0 in body text | 0 | PASS |

---

## SUMMARY

All four targeted fixes have been applied:

1. **Em dashes:** Reduced from 37 to 0 (target ≤4). Each replaced with commas, parentheses, colons, semicolons, or sentence breaks as appropriate to context.
2. **Sentence openers:** All 28 flagged sections now have no word appearing more than twice as a sentence opener. Techniques used: syntactic rotation (fronting prepositional phrases, participial phrases, subordinate clauses), passive reframing, and adverbial/evaluative openers.
3. **Rule-of-three:** All 28 flagged sections now have ≤1 tripartite list per 300-word segment. Excess triples converted to two-part structures with connectives ("as well as", "alongside", "together with", "compounded by").
4. **Spelling:** "judgments" corrected to "judgements" in §1.7 and §3.9.

No citations were altered, added, or removed. No analytical claims were changed. No new vocabulary from AI-flagged lists was introduced. British English maintained throughout body text.
