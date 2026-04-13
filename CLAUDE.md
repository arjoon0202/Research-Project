# CLAUDE.md — Dissertation Correction Task

## CARDINAL RULE

**DO NOT FABRICATE.** Never invent, guess, or assume any factual detail — page numbers, publication years, journal names, volume numbers, page ranges, author names, or quoted text. If you cannot verify a detail from the files in this repository, flag it with `[HUMAN CHECK REQUIRED]` rather than guessing. A wrong citation is worse than a flagged one.

## PROJECT CONTEXT

You are performing a forensic editorial audit of a master's dissertation (M.Ed., Liverpool John Moores University) after external reviews identified issues. The major content corrections (page references, source attribution, TOC headings) have already been applied. Your job is the systematic sweep: cross-reference audit, missing preliminary pages, generic reference cleanup, and consistency checks.

## FILES

1. `DISSERTATION_PHASE5_CORRECTED.docx` — The corrected dissertation. **Use this as your working file.**
2. `Inclusion_Policy_for_Guyana.docx` — The primary policy document. Use to verify page references. Do NOT modify.
3. `VERIFIED_REVIEW_FINDINGS.md` — The verified issues list. Read in full before starting.
4. `Additional_Annotated_Bibliography_Supplementary_Sources.md` — Verified source details. Do NOT modify.
5. `Annotated_Bibliography_Inclusive_Education_Guyana_v2.docx` — Original annotated bibliography. Do NOT modify.

## CORRECTIONS ALREADY APPLIED

The following have been fixed. Do NOT redo them:

1. All p. 18 page references → corrected to p. 19 (curriculum) or p. 20 (monitoring/reporting)
2. IDB/World Bank misattribution → restructured in Sections 1.2 and 5.4
3. Armstrong reference → body text now identifies it as a book chapter contribution
4. TOC headings → "Hypotheses" changed to "Working Hypotheses" in 1.5 and 4.5
5. "and and" typo → fixed in Section 4.4.1
6. Redundant repeated citations → consolidated in Section 4.4.1

## OUTPUT

Save the final document as `DISSERTATION_FINAL.docx` in the same directory. Do not overwrite the input file.

---

## PHASE A: Read and Understand

1. Read `VERIFIED_REVIEW_FINDINGS.md` completely.
2. Unpack the corrected dissertation and familiarise yourself with the structure.
3. Print: "Phase A complete."

Do NOT make changes in this phase.

---

## PHASE B: Page Reference Verification

Verify, do not redo. The p. 18 corrections are already applied.

1. Find every instance where the Draft Inclusion Policy (Ministry of Education Guyana, 2010) is cited with a page number.
2. Confirm no p. 18 policy references remain (page ranges in the reference list like pp. 186–209 are fine).
3. Confirm all other page references are plausible per the policy's TOC:
   - p. 10 = Guyana perspective / p. 12 = specialist schools / p. 13 = coordination deficit / p. 14 = The Inclusion Policy / p. 19 = Section 3 / p. 20 = end of Section 3 / p. 21+ = Enactment / pp. 22-24 = Training / p. 24 = IEPs / p. 27 = ACEO / p. 32 = School structures / p. 33 = Special schools
4. Print the verification table.

---

## PHASE C: Add List of Tables

The dissertation contains Tables 4.01 and 4.02 but no List of Tables in the preliminary pages. Add one.

1. Insert a "LIST OF TABLES" section after the Table of Contents and before the Abstract.
2. It should list:
   - Table 4.01: Alignment of the Draft Inclusion Policy with International Frameworks
   - Table 4.02: Operationalisation of Policy-Specified Institutional Mechanisms
3. Use the same formatting style as the existing Table of Contents.
4. Print what was added.

---

## PHASE D: Generic Reference Improvements

1. The reference list entry "Ministry of Education Guyana (n.d.) Inclusive education initiatives in Guyana [Online]. Available at: https://education.gov.gy" is a bare homepage URL. Check the annotated bibliography files for a more specific URL. If found, update. If not, insert `[HUMAN CHECK: replace with specific document URL]`.
2. The reference list entry "World Bank (2024) Disability inclusion in Guyana: Country profile [Online]. Available at: https://www.worldbank.org/en/topic/disability" is a general topic page. Check the annotated bibliography files for a more specific URL. If found, update. If not, insert `[HUMAN CHECK: replace with specific country profile URL]`.
3. Print what was changed.

---

## PHASE E: Cross-Reference Audit

This is forensic. Report only — do NOT make changes unless a clear fix is obvious (like a misspelled author name).

1. Extract every in-text citation (author, year) from the dissertation body (Abstract through Chapter 5).
2. Extract every entry from the reference list.
3. Report:
   - Any in-text citation NOT in the reference list.
   - Any reference list entry NOT cited in the body text.
   - Any discrepancies in author names, dates, or spelling between citations and reference list.
4. Print the full audit results.

---

## PHASE F: Minor Fixes

1. If no existing note explains the SEN/SEND terminological shift, add a brief parenthetical at the first point where both terms appear. Example: "(The Draft Inclusion Policy uses 'SEN'; recent Guyanese institutional developments, including the CPCE programme, use the expanded term 'SEND.' Both appear in this study according to their original context.)"
2. Scan for any American English spellings introduced during editing (organization, behavior, analyze, etc.) and correct to British English.
3. Print what was changed.

---

## PHASE G: Pack and Verify

1. Repack the document as `DISSERTATION_FINAL.docx`.
2. Report: body word count (Chapters 1–5), em dash count, reference count.
3. Print: "Phase G complete. Final document saved."

---

## THINGS YOU MUST NOT DO

- Do NOT add Matland (1995) to the reference list — it is already there.
- Do NOT change any page references that are already correct.
- Do NOT rewrite prose for style unless specifically instructed.
- Do NOT guess page numbers — use `[VERIFY PAGE]` if uncertain.
- Do NOT modify the source files (policy document, annotated bibliographies).
- Do NOT fabricate any bibliographic detail.
