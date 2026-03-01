# Track Specification: Chapter F1.4 Levelling

## Overview
This track involves writing Chapter F1.4 on "Levelling" for the TeachBook template, which supports the IHO Cat A hydrographer certification. The chapter will synthesize material from the `S-5A_Ed1.0.2.md` syllabus and the provided `deepresearch/f1.4-levelling.md` content.

## Instructional Approach
- **Tone:** A blend of Academic and Action-Oriented.
- **Goal:** A balanced mix of theoretical understanding of levelling principles and practical, action-oriented execution.
- **Strategy:** Problem-Based Learning, beginning with authentic challenges (e.g., setting up a level) to guide the theoretical exploration.

## Functional Requirements
The chapter MUST cover the following topics in order, as dictated by `third_party/S-5A_Ed1.0.2.md`:

1.  **F1.4a Levelling instruments**
    *   (i) Levelling instruments
    *   (ii) Total stations
    *   (iii) Effects of curvature and refraction
    *   (iv) Reduction of levels and correction to the relevant height datum
    *   (v) Calibration requirements and documentation
    *   *Objective:* Explain the principles of operation of instruments used in determination of height differences.
2.  **F1.4b Height reduction**
    *   *Objective:* Conduct surveys in accordance with standards.

## Interactivity & UX
- Include **Python Snippets** to demonstrate practical calculations (e.g., for reducing levels or calculating curvature/refraction corrections).
- Introduce topics using **Problem-Based Scenarios** to ground the theory in real-world hydrographic tasks.
- Provide alternative data processing examples using SQLite and DuckDB where appropriate for datasets.

## Non-Functional Requirements
- **Licensing:** Text and generated data must be CC-0. Code must be Apache-2.0.
- **Reference System:** Include inline links to primary sources (like Wikipedia/Wiktionary) for unfamiliar terms. Use the GCMD Keyword Viewer (https://gcmd.earthdata.nasa.gov/KeywordViewer/scheme/all) for standardized terminology.
- **Dependencies:** Assume students are on Ubuntu Linux but may access MS Windows remotely. Prefer open-source software (no AGPL).

## Acceptance Criteria
- Chapter F1.4 is fully written and covers all topics listed in S-5A Ed1.0.2.
- The content utilizes a Problem-Based Learning approach.
- Python code snippets are provided, functional, and well-commented.
- Terminology is properly linked to inline definitions and GCMD keywords.
- Unit tests are provided for the Python code examples where possible.