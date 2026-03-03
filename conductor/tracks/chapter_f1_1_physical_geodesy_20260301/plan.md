# Implementation Plan: Chapter F1.1 Physical Geodesy

## Phase 1: Gravity and Geopotential Models [checkpoint: fa7bfa5]
- [x] Task: Create initial markdown file `book/f1.1-physical-geodesy.md` with headers matching the S-5A syllabus sections. ab4b224
- [x] Task: Write the introductory "Problem-Based Scenario" focusing on how gravity impacts hydrographic measurements (e.g., determining mean sea level).
- [x] Task: Draft section on "F1.1a Gravity field of the Earth" covering equipotential surfaces, gravity, and gravity anomalies. Use `deepresearch/f1.1-physical-geodesy.md` as source material.
- [x] Task: Write Tests: Create `tests/test_f1_1_gravity.py` for Python snippets calculating theoretical normal gravity (e.g., Somigliana equation).
- [x] Task: Implement Feature: Embed the theoretical normal gravity Python snippets in the gravity anomalies section.
- [x] Task: Draft section on "F1.1b Global geopotential models" focusing on spherical harmonics.
- [x] Task: Conductor - User Manual Verification 'Phase 1: Gravity and Geopotential Models' (Protocol in workflow.md) fa7bfa5

## Phase 2: Height Systems and Deflection [checkpoint: 1b91cdc]
- [x] Task: Draft section on "F1.1c Height systems" detailing dynamic, orthometric, and normal heights. 120ba48
- [x] Task: Implement Feature: Add Python snippets explaining the mathematical differences between orthometric and dynamic heights (conceptual conversions based on different gravity denominators). 120ba48
- [x] Task: Write Tests: Add tests for height system conversion snippets to `tests/test_f1_1_gravity.py`. 120ba48
- [x] Task: Draft section on "F1.1d Deflection of the vertical" explaining its components and impact on hydrographic sensors. 120ba48
- [x] Task: Conductor - User Manual Verification 'Phase 2: Height Systems and Deflection' (Protocol in workflow.md) 1b91cdc

## Phase 3: Review and Finalization
- [ ] Task: Add relevant CC-0 references and inline links (Wikipedia/Wiktionary/GCMD Viewer/NGS) throughout the drafted chapter.
- [ ] Task: Add an SQLite/DuckDB example showing how one might query a database of gravity anomalies or height conversions across a survey line.
- [ ] Task: Review the entire chapter to ensure the "Academic and Action-Oriented" tone is consistent.
- [ ] Task: Add `book/f1.1-physical-geodesy.md` to `book/_toc.yml` under the Tutorials section.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Review and Finalization' (Protocol in workflow.md)