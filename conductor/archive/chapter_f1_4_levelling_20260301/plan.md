# Implementation Plan: Chapter F1.4 Levelling

## Phase 1: Structure and Core Instrumentation [checkpoint: 01c60ea]
- [x] Task: Create initial markdown file `book/f1.4-levelling.md` with headers matching the S-5A syllabus sections. 39a9f7c
- [x] Task: Integrate introductory content and the "Problem-Based Scenario" setting up the chapter. 15e4467
- [x] Task: Draft section on "Levelling instruments" and "Total stations" using `deepresearch/f1.4-levelling.md` as a source.
- [x] Task: Add relevant CC-0 references and inline links (Wikipedia/GCMD) to the drafted sections. 75ba4b8
- [x] Task: Conductor - User Manual Verification 'Phase 1: Structure and Core Instrumentation' (Protocol in workflow.md) 01c60ea

## Phase 2: Refraction, Curvature, and Reduction [checkpoint: 3c8be72]
- [x] Task: Write Tests: Create `tests/test_f1_4_calculations.py` for Python calculation snippets relating to curvature, refraction, and level reduction. e065365
- [x] Task: Implement Feature: Draft section on "Effects of curvature and refraction". a8680c7
- [x] Task: Implement Feature: Write and embed Python snippets in `book/f1.4-levelling.md` for curvature/refraction calculations ensuring they pass the unit tests. a8680c7
- [x] Task: Implement Feature: Draft section on "Reduction of levels and correction to the relevant height datum". a8680c7
- [x] Task: Implement Feature: Write and embed Python snippets for level reduction calculations, ensuring they pass the tests. a8680c7
- [x] Task: Conductor - User Manual Verification 'Phase 2: Refraction, Curvature, and Reduction' (Protocol in workflow.md) 3c8be72

## Phase 3: Calibration and Data Management [checkpoint: 1f9af91]
- [x] Task: Write Tests: Create `tests/test_f1_4_database.py` to test dataset processing with SQLite/DuckDB. ef2e8ee
- [x] Task: Implement Feature: Draft section on "Calibration requirements and documentation". ccd5348
- [x] Task: Implement Feature: Add data processing examples for level reduction using SQLite and DuckDB, ensuring they pass the database tests. ccd5348
- [x] Task: Implement Feature: Draft section on "Height reduction (F1.4b)" emphasizing conducting surveys in accordance with standards. ccd5348
- [x] Task: Conductor - User Manual Verification 'Phase 3: Calibration and Data Management' (Protocol in workflow.md) 1f9af91

## Phase 4: Review and Finalization [checkpoint: a6c201d]
- [x] Task: Review the entire chapter for the "Academic and Action-Oriented" tone. e97a2cc
- [x] Task: Verify that all terminology is correctly linked (GCMD Viewer, Wikipedia). e97a2cc
- [x] Task: Add `book/f1.4-levelling.md` to `book/_toc.yml` to ensure it is published. e97a2cc
- [x] Task: Conductor - User Manual Verification 'Phase 4: Review and Finalization' (Protocol in workflow.md) a6c201d