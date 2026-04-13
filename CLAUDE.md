# CLAUDE.md — Dissertation Correction Task

## CARDINAL RULE

**DO NOT FABRICATE.** Never invent, guess, or assume any factual detail — page numbers, publication years, journal names, volume numbers, page ranges, author names, or quoted text. If you cannot verify a detail from the files in this repository, flag it with a `[HUMAN CHECK REQUIRED]` comment rather than guessing. A wrong citation is worse than a flagged one.

## PROJECT CONTEXT

You are correcting a master's dissertation (M.Ed., Liverpool John Moores University) after external reviews identified citation, reference, and formatting issues. The dissertation is a qualitative desktop analysis of Guyana's Draft Inclusion Policy for Special Educational Needs.

The file `VERIFIED_REVIEW_FINDINGS.md` contains every confirmed issue to fix. It was produced by cross-checking two independent reviews against the primary sources. Only verified issues are included — false findings from the reviews have already been filtered out.

## FILES IN THIS REPOSITORY

1. `DISSERTATION_PHASE5_COMPLETE.docx` — The dissertation to correct. This is a Word document. Use python-docx or the unpack/edit XML/repack approach (scripts at `/mnt/skills/public/docx/scripts/office/`) to edit it.
2. `Inclusion_Policy_for_Guyana.docx` — The primary policy document under analysis. Use this to verify page references. Do NOT modify this file.
3. `VERIFIED_REVIEW_FINDINGS.md` — The verified list of issues to fix. Read this file IN FULL before making any changes.
4. `Additional_Annotated_Bibliography_Supplementary_Sources.md` — Verified source details for supplementary references. Use to check bibliographic details. Do NOT modify.
5. `Annotated_Bibliography_Inclusive_Education_Guyana_v2.docx` — Original annotated bibliography with verified facts. Use for reference. Do NOT modify.

## OUTPUT

Save the corrected dissertation to the same directory as the original, named `DISSERTATION_FINAL_CORRECTED.docx`. Do not overwrite the original.

---

## EXECUTION PLAN

Work through the following phases in order. Complete each phase fully before moving to the next. After each phase, print a summary of exactly what was changed.

---

### PHASE A: Read and Understand

1. Read `VERIFIED_REVIEW_FINDINGS.md` completely.
2. Read the Draft Inclusion Policy (`Inclusion_Policy_for_Guyana.docx`) and confirm the table of contents page-to-section mapping.
3. Unpack the dissertation docx and familiarise yourself with the XML structure.
4. Print: "Phase A complete. Ready to proceed."

Do NOT make any changes in this phase.

---

### PHASE B: Page Reference Corrections

This is the highest-priority fix.

1. Find every instance in the dissertation where the Draft Inclusion Policy (Ministry of Education Guyana, 2010) is cited with a page number.
2. For each citation, determine which SECTION of the policy the quoted/cited content falls in.
3. Cross-check the section against the policy's table of contents to verify the page number.
4. Apply corrections per the verified findings:
   - Content currently cited as p. 18 that belongs in Section 3 (starts p. 19) must be changed. Provisions at the start of Section 3 → p. 19. Provisions near the end of Section 3 (monitoring, parliamentary reporting, the passage just before "The Enactment of the Policy" at p. 21) → p. 20.
   - Do NOT change page references that are already verified correct (p. 14, p. 10, p. 12, p. 13, pp. 22-24, p. 24, p. 27, p. 32, p. 33).
5. Also fix the same page references in Appendix A.
6. Print a table listing every policy page reference in the document, its quoted text, and whether it was changed or left as-is.

---

### PHASE C: Source Attribution Fix

1. **IDB/World Bank (Section 1.2):** The sentence "the Inter-American Development Bank estimates disability prevalence in Guyana at 13.6 per cent, consistent with the WHO global estimate of approximately 15 per cent (World Bank, 2024)" misattributes the IDB estimate to the World Bank. Fix by restructuring the sentence so the claim is attributed to the World Bank's reporting of international estimates, without naming the IDB as a separate source that isn't in the reference list. For example: "Contemporary estimates suggest the true figure is substantially higher; international assessments reported by the World Bank (2024) place disability prevalence in Guyana at approximately 13.6 per cent, consistent with the WHO global estimate of approximately 15 per cent."
2. **IDB/World Bank (Section 5.4, Recommendation 4):** Apply the same fix to the sentence "IDB estimates suggest a figure closer to 13.6% for Guyana, consistent with the WHO global estimate of approximately 15% (World Bank, 2024)." Restructure to: "international estimates place disability prevalence closer to 13.6 per cent, consistent with the WHO global estimate of approximately 15 per cent (World Bank, 2024)."
3. **Armstrong (Section 2.4.5):** Where Armstrong, Armstrong and Spandagou (2005) is first cited, add qualifying language indicating it is a book chapter. For example, change "documented that across the Eastern Caribbean" to "noted, in their contribution to Mitchell's edited volume on inclusive education, that across the Eastern Caribbean" or similar phrasing that signals it is a chapter, not a standalone study.
4. Print exactly what was changed for each fix.

---

### PHASE D: Table of Contents and Preliminary Pages

1. In the Table of Contents, change "1.5 Hypotheses" to "1.5 Working Hypotheses".
2. Verify that all other TOC entries match the actual body headings. If any mismatch is found, correct the TOC to match the body.
3. Add a "LIST OF TABLES" section to the preliminary pages, after the Table of Contents and before the Abstract. It should list:
   - Table 4.01: Alignment of the Draft Inclusion Policy with International Frameworks
   - Table 4.02: Operationalisation of Policy-Specified Institutional Mechanisms
   Include page numbers if they can be determined; otherwise use placeholder page numbers that match the chapter structure.
4. Print what was changed.

---

### PHASE E: Generic Reference Improvements

1. In the reference list, the entry for "Ministry of Education Guyana (n.d.)" points to a bare homepage URL. If you can identify a more specific URL for the SEND/inclusive education content from the annotated bibliography files, update it. If not, add a note: `[HUMAN CHECK REQUIRED: replace with specific document URL]`.
2. In the reference list, the entry for "World Bank (2024)" points to a generic disability topic page. If you can identify a more specific Guyana country profile URL from the annotated bibliography files, update it. If not, add a note: `[HUMAN CHECK REQUIRED: replace with specific country profile URL]`.
3. Print what was changed.

---

### PHASE F: Cross-Reference Audit

This is a forensic check. Do NOT make changes — only report findings.

1. Extract every in-text citation (author, year) from the body of the dissertation (Chapters 1–5 and Abstract).
2. Extract every entry from the reference list.
3. Report:
   - Any in-text citation that does NOT appear in the reference list.
   - Any reference list entry that is NOT cited anywhere in the body text.
   - Any discrepancies in author names, dates, or spelling between in-text citations and reference list entries.
4. Print the full audit results.

---

### PHASE G: Minor Fixes

1. **SEN/SEND note:** If there is no existing acknowledgement of the SEN→SEND terminological shift, add a brief parenthetical note at the first point where both terms appear (likely Chapter 1 or the Definitions section). Something like: "(The policy uses the term 'SEN'; recent Guyanese institutional developments, including the CPCE programme, use the expanded term 'SEND.' Both terms are used in this study according to their original context.)"
2. **British English check:** Scan for any American English spellings that may have been introduced during editing (organization, behavior, analyze, etc.). Correct to British English.
3. Print what was changed.

---

### PHASE H: Final Verification

1. Repack the document.
2. Run a final word count on Chapters 1–5 body text. Report the count.
3. Count remaining em dashes. Report the count.
4. Count total references in the reference list. Report the count.
5. Print: "Phase H complete. Final document saved as DISSERTATION_FINAL_CORRECTED.docx."

---

## THINGS YOU MUST NOT DO

- Do NOT add Matland (1995) to the reference list — it is already there. One review incorrectly claimed it was missing.
- Do NOT award the preliminary pages 5/5 — the list of tables IS missing and needs to be added.
- Do NOT claim the TOC "perfectly mirrors" the body — it does not (Hypotheses vs Working Hypotheses).
- Do NOT change any content that is factually correct.
- Do NOT rewrite prose for style unless specifically instructed. The prose corrections are lower priority than the citation fixes.
- Do NOT guess page numbers. If you cannot determine the correct page from the policy document, use `[VERIFY PAGE]` as a placeholder.
- Do NOT modify the primary source files (policy document, annotated bibliographies).
