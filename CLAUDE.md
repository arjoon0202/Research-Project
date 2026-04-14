# CLAUDE CODE INSTRUCTIONS — Dissertation Humanisation

## OBJECTIVE

Rewrite the text content of `DISSERTATION_EDITED.docx` to eliminate AI-detection markers while preserving every citation, every factual claim, every analytical argument, and the document's formatting/structure. The rewritten text should read as if a human academic wrote it — specifically matching the stylistic fingerprint documented in `WRITING_STYLE_ANALYSIS.md`.

---

## HIGH-LEVEL WORKFLOW

```
1. SETUP
   ├── Read WRITING_STYLE_ANALYSIS.md (target writing style)
   ├── Read AI_DETECTION_REFERENCE.md (what to avoid)
   ├── Clone DISSERTATION_EDITED.docx → DISSERTATION_ORIGINAL_BACKUP.docx (never modify this)
   ├── Convert DISSERTATION_EDITED.docx → dissertation_original.md (reference text)
   ├── Convert the writing sample PDF → writing_sample.md (style reference only)
   └── Create a working copy: dissertation_working.md (this is what you edit)

2. REWRITE (Chapter by chapter, section by section)
   ├── Read original section from dissertation_original.md
   ├── Rewrite applying style rules + AI avoidance rules
   ├── Compare rewritten section against original for:
   │   ├── Citation accuracy (every citation preserved?)
   │   ├── Factual accuracy (same claims, same evidence?)
   │   ├── No content leakage from writing sample
   │   └── Meaning preservation (same argument?)
   └── Run adversarial AI detection check (Section 5 below)

3. ITERATE
   ├── If a segment fails adversarial check → revise that segment
   └── Repeat until all segments pass

4. REASSEMBLE
   ├── Patch rewritten text back into the .docx (XML-level edit)
   ├── Preserve ALL formatting: fonts, styles, headings, tables, bold/italic, page breaks
   └── Output: DISSERTATION_HUMANISED.docx
```

---

## CRITICAL CONSTRAINTS

### What You MUST Preserve (Non-Negotiable)

1. **Every in-text citation** — author names, years, page numbers. No citation may be deleted, altered, or fabricated.
2. **Every factual claim** — statistics, dates, policy provisions, names, figures. Cross-check against the original.
3. **Every table and its content** — comparison tables, thematic matrices. Only rewrite prose surrounding them; do not alter table cell text unless it contains flagged AI vocabulary.
4. **The argument structure** — the sequence of claims, evidence, and analysis in each section must be logically identical.
5. **Harvard referencing format** — maintain author-date style throughout.
6. **British English spelling** — organisation, behaviour, programme, centre, analyse, recognise, defence, labour, colour, judgement.
7. **Document formatting** — fonts, heading styles, table formatting, page layout, bold/italic. You are editing words, not formatting.
8. **The Reference List** — do not touch references at all.
9. **Preliminary pages** — abstract, TOC, acknowledgements, etc. Only rewrite the abstract text; preserve all other preliminary page content.

### What You MUST Change

1. AI-overused vocabulary (see AI_DETECTION_REFERENCE.md Section 4.1).
2. Uniform sentence lengths → varied sentence lengths.
3. Repetitive sentence openers → diverse openers.
4. Formulaic paragraph structures → varied structures.
5. AI-typical transitions ("Furthermore," "Moreover," "Additionally") → natural transitions.
6. Symmetrical paragraph lengths → varied paragraph lengths.
7. Meta-commentary patterns ("Applying the [framework] lens...") → let analysis speak directly.
8. Excessive hedging stacks → single qualifiers.
9. Rule-of-three patterns → vary list structures.

### What You MUST NOT Do

1. **Do not fabricate citations.** If a sentence cites Smith (2020), the rewritten sentence must cite Smith (2020).
2. **Do not change the meaning.** If the original says "the policy fails to specify training standards," the rewrite must say the same thing, just differently worded.
3. **Do not import content from the writing sample.** No paleolimnology, no Cladocera, no arsenic, no Yellowknife, no limnology concepts. Only stylistic patterns transfer.
4. **Do not relax the academic register.** The text must remain formally academic. No contractions, no fragments, no informal language.
5. **Do not add new analytical claims** not present in the original.
6. **Do not delete sections or paragraphs.** Rewrite them, don't remove them.
7. **Do not touch the .docx formatting/code.** Only modify text content within XML text runs.

---

## DETAILED REWRITING RULES

### Rule 1: Sentence Length Variation

For each paragraph, ensure:
- At least one sentence under 15 words.
- At least one sentence over 30 words.
- The standard deviation of sentence word counts should exceed 8.

**Before (AI-like):**
"The policy establishes a framework for inclusive education. This framework identifies thirteen dimensions of institutional capacity. These dimensions address teacher training, curriculum adaptation, and resource allocation. However, the policy does not specify measurable standards for any of these dimensions."

**After (human-like):**
"Thirteen dimensions of institutional capacity are identified in the policy. These range from teacher training to curriculum adaptation to resource allocation — yet for none of them does the policy specify a measurable standard. The framework exists on paper, but its provisions lack the operational detail that would make compliance verifiable."

### Rule 2: Sentence Opener Diversity

Within any 5-sentence span, no more than 2 sentences should start with the same word. Rotate among:
- Subject-first ("The policy...")
- Prepositional phrase ("In Section 4.3 of the policy,...")
- Adverbial ("Significantly, the policy...")
- Citation-led ("Matland (1995) argues that...")
- Concessive ("Although the policy acknowledges...")
- Conditional ("If implementation were to proceed as designed,...")
- Participial ("Drawing on Lipsky's (1980) framework,...")
- Short declarative ("This omission is telling.")

### Rule 3: Vocabulary Substitution

Replace AI-overused words with plainer alternatives:

| AI Word | Alternatives |
|---------|-------------|
| delve/delves | examine, investigate, look closely at, consider, probe |
| comprehensive | thorough, full, complete, wide-ranging, extensive |
| crucial | important, essential, central, key, critical |
| pivotal | important, central, key, decisive |
| nuanced (adj) | subtle, qualified, complex, differentiated |
| multifaceted | complex, varied, having several dimensions |
| robust | strong, solid, well-developed, substantial |
| landscape (metaphor) | context, environment, field, situation, conditions |
| framework (if overused) | structure, model, approach, system, scheme |
| operationalise (if overused) | implement, put into practice, enact, give effect to, carry out |
| architecture (metaphor) | structure, system, design, arrangement |
| illuminate | show, reveal, clarify, make clear, bring to light |
| underscore | emphasise, highlight, stress, point to, show |
| navigate | manage, handle, work through, address, deal with |
| foster | encourage, support, promote, cultivate |
| Furthermore/Moreover | [omit and use implicit connection, or use "However," "In contrast," "At the same time," "Yet," "Equally,"] |
| Additionally | [omit, or use "Beyond this," "Separately," "A further point is that"] |
| It is important to note | [just state the point directly] |
| It should be noted | [just state the point directly] |
| facilitate | support, enable, help, allow, make possible |
| enhance | improve, strengthen, increase, develop |

### Rule 4: Paragraph Structure Variation

Ensure no three consecutive paragraphs follow the same internal structure. Mix:
- Evidence-first paragraphs (start with a finding, then interpret).
- Claim-first paragraphs (start with an analytical claim, then support with evidence).
- Concession-first paragraphs (start by acknowledging a counterpoint, then develop).
- Question-driven paragraphs (pose a question, then address it).
- Short, punchy paragraphs (2–3 sentences making a single tight point).

### Rule 5: Transition Naturalisation

- Remove or replace "Furthermore," "Moreover," "Additionally," "In addition," as paragraph openers.
- Allow some paragraph transitions to be implicit (the reader infers the connection).
- When explicit transitions are needed, prefer: "However," "In contrast," "Yet," "At the same time," "A separate concern is," "Equally," "The same pattern appears in," "Against this background,".

### Rule 6: Meta-Commentary Reduction

Remove or rewrite sentences that announce what the analysis is doing:
- "Applying the social model lens established in Chapter 2 (Section 2.3)..." → Just apply the lens by using its concepts directly.
- "This section will examine..." → Delete and start examining.
- "As discussed in Section 2.4..." → Only cross-reference if genuinely necessary; otherwise, just make the point.

### Rule 7: Semicolon Integration

The target author uses semicolons to join related independent clauses. Introduce this pattern where natural:
- "The policy identifies training as a priority; it does not, however, prescribe what that training should contain."
- "Six categories of disability are recognised in the policy text; intellectual disability and autism spectrum conditions are conspicuously absent."

---

## ADVERSARIAL AI DETECTION SELF-CHECK

After rewriting each section (~300 words at a time, matching Turnitin's segmentation), perform this check:

### Check 1: Flagged Vocabulary Count
Scan the segment for words from the AI_DETECTION_REFERENCE.md Section 4.1 lists. Target: ≤2 per 300-word segment.

### Check 2: Sentence Length Standard Deviation
Calculate sentence word counts in the segment. Compute SD. Target: SD > 8.

### Check 3: Sentence Opener Diversity
List the first word of each sentence. Target: No word appears as a sentence opener more than twice in a segment.

### Check 4: Paragraph Length Variance
If the segment contains multiple paragraphs, calculate word counts. Target: ≥30% variance between shortest and longest.

### Check 5: Transition Word Pattern
Check for "Furthermore," "Moreover," "Additionally," "In addition" as paragraph openers. Target: 0 in any segment.

### Check 6: Rule-of-Three Count
Count tripartite list structures ("X, Y, and Z" or "X, Y, Z"). Target: ≤1 per segment. If more, restructure some into prose.

### Check 7: Meta-Commentary Check
Flag any sentence that announces what the text is about to do or summarises what it has done. Target: 0 per segment (or at most 1 in genuinely transitional locations).

### Check 8: Meaning Preservation
Compare each rewritten paragraph against the original. Verify:
- Same citations present.
- Same factual claims made.
- Same analytical conclusion reached.
- No new claims introduced.
- No claims deleted.

### Check 9: Content Leakage Check
Scan rewritten text for any words/concepts from the writing sample's subject matter: Cladocera, arsenic, paleolimnology, subfossil, Yellowknife, subarctic, sediment cores, Daphnia, Bosmina, limnology, bioassay, ecotoxicology. Target: 0 occurrences.

### Check 10: British English Verification
Scan for American spellings. Target: 0 American spellings.

---

## SECTION-BY-SECTION PROCESSING ORDER

Process the dissertation in this order:

1. **Chapter 4** (Results & Discussion) — highest priority; most AI-detection risk due to extensive analytical prose.
2. **Chapter 2** (Literature Review) — second priority; dense referencing and formal analytical prose.
3. **Chapter 5** (Conclusions & Recommendations) — third priority.
4. **Chapter 1** (Introduction) — fourth priority.
5. **Chapter 3** (Methodology) — lowest priority; technical/procedural writing is more forgivable.
6. **Abstract** — last; rewrite after all chapters are finalised.

---

## TECHNICAL INSTRUCTIONS FOR .DOCX EDITING

### Converting .docx to .md for Editing

Use python-docx or pandoc to extract text content:

```bash
pandoc DISSERTATION_EDITED.docx -t markdown -o dissertation_original.md
```

### Patching Text Back into .docx

Use the unpack/pack scripts from `/mnt/skills/public/docx/scripts/office/` for XML-level work. The approach:

1. Unpack the .docx to XML.
2. Identify text runs (`<w:t>` elements) in the XML.
3. Replace the text content within existing runs — do NOT create new runs, delete runs, or modify run properties (which contain formatting).
4. Repack the .docx.

**Critical:** Save all paragraph references BEFORE making any changes to avoid index-shifting from insertions. Work through the document sequentially, updating text within existing XML structures.

### Alternative Approach

If XML-level editing is too fragile, you can:
1. Use python-docx to iterate through paragraphs.
2. For each paragraph, replace the text content while preserving the paragraph's style and run formatting.
3. Be careful with runs that contain mixed formatting (e.g., italic within a paragraph) — preserve run boundaries.

---

## OUTPUT

Final deliverable: `DISSERTATION_HUMANISED.docx` in `/mnt/user-data/outputs/`

Also output: `HUMANISATION_REPORT.md` documenting:
- Per-section adversarial check results (pass/fail per check per segment).
- Summary of vocabulary substitutions made.
- Any segments that required multiple iterations.
- Final estimated AI detection risk assessment.
- CODEX will review your ouput.
