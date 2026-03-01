# Implementation Plan: Chapter F1.4 Levelling

## Phase 1: Structure and Core Instrumentation
- [ ] Task: Create initial markdown file `book/f1.4-levelling.md` with headers matching the S-5A syllabus sections.
- [ ] Task: Integrate introductory content and the "Problem-Based Scenario" setting up the chapter.
- [ ] Task: Draft section on "Levelling instruments" and "Total stations" using `deepresearch/f1.4-levelling.md` as a source.
- [ ] Task: Add relevant CC-0 references and inline links (Wikipedia/GCMD) to the drafted sections.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Structure and Core Instrumentation' (Protocol in workflow.md)

## Phase 2: Refraction, Curvature, and Reduction
- [ ] Task: Write Tests: Create `tests/test_f1_4_calculations.py` for Python calculation snippets relating to curvature, refraction, and level reduction.
- [ ] Task: Implement Feature: Draft section on "Effects of curvature and refraction".
- [ ] Task: Implement Feature: Write and embed Python snippets in `book/f1.4-levelling.md` for curvature/refraction calculations ensuring they pass the unit tests.
- [ ] Task: Implement Feature: Draft section on "Reduction of levels and correction to the relevant height datum".
- [ ] Task: Implement Feature: Write and embed Python snippets for level reduction calculations, ensuring they pass the tests.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Refraction, Curvature, and Reduction' (Protocol in workflow.md)

## Phase 3: Calibration and Data Management
- [ ] Task: Write Tests: Create `tests/test_f1_4_database.py` to test dataset processing with SQLite/DuckDB.
- [ ] Task: Implement Feature: Draft section on "Calibration requirements and documentation".
- [ ] Task: Implement Feature: Add data processing examples for level reduction using SQLite and DuckDB, ensuring they pass the database tests.
- [ ] Task: Implement Feature: Draft section on "Height reduction (F1.4b)" emphasizing conducting surveys in accordance with standards.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Calibration and Data Management' (Protocol in workflow.md)

## Phase 4: Review and Finalization
- [ ] Task: Review the entire chapter for the "Academic and Action-Oriented" tone.
- [ ] Task: Verify that all terminology is correctly linked (GCMD Viewer, Wikipedia).
- [ ] Task: Add `book/f1.4-levelling.md` to `book/_toc.yml` to ensure it is published.
- [ ] Task: Conductor - User Manual Verification 'Phase 4: Review and Finalization' (Protocol in workflow.md)