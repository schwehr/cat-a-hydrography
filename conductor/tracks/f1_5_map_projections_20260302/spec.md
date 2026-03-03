# Specification: Chapter F1.5 - Map Projections

## Overview
This track involves writing Chapter F1.5 on map projections for the interactive Jupyter TeachBook, targeting IHO Cat A hydrographer certification. The chapter will use `third_party/S-5A_Ed1.0.2.md` to define the list of topics and their order of presentation. Existing material from `deepresearch/f1.5-map-projections.md` will serve as the baseline draft, which will be expanded, refined, and heavily supplemented to meet all project requirements.

## Functional Requirements
*   **Content Alignment:** Must strictly follow the topic list and order specified in `third_party/S-5A_Ed1.0.2.md` for section F1.5.
*   **Baseline Integration:** Utilize `deepresearch/f1.5-map-projections.md` as the structural foundation, adding necessary original content, definitions, and examples to ensure correctness and completeness.
*   **Interactive Python Elements:**
    *   Include code examples demonstrating area and shape distortions (e.g., Tissot's indicatrix).
    *   Provide examples utilizing standard Python geospatial libraries like `pyproj` or `cartopy`.
    *   Integrate interactive widgets allowing students to dynamically change projection parameters.
*   **Assessments & Problem-Based Learning (PBL):**
    *   Include a practical Python programming task involving coordinate transformations.
    *   Present a real-world case study analyzing the impact of incorrect projection choices in hydrography.
    *   Include a theoretical quiz (multiple-choice or short-answer) to reinforce understanding.
*   **Open Source Focus:** All code examples and solutions must utilize open-source software. Do not use AGPL-licensed software.

## Non-Functional Requirements
*   **References & Glossary:** All answers and explanations must include references. Assume the reader does not know acronyms and terms; provide a glossary and links to primary references (e.g., Wikipedia/Wiktionary, NASA GCMD).
*   **Licensing:** Text and generated data must be under the Creative Commons CC-0 license. Code snippets must be under the Apache-2.0 license.
*   **Testing:** Provide unit tests for all Python code examples where possible.
*   **Target Environment:** Students are assumed to be using Ubuntu Linux (or MS Windows on a remote VM).

## Acceptance Criteria
*   [ ] Chapter F1.5 is fully written and accessible within the Jupyter Book structure.
*   [ ] All topics from `third_party/S-5A_Ed1.0.2.md` under F1.5 are covered in the correct order.
*   [ ] The baseline material from `deepresearch/f1.5-map-projections.md` is successfully integrated and expanded upon.
*   [ ] The chapter contains interactive widgets, distortion demonstrations, and `pyproj`/`cartopy` examples.
*   [ ] The chapter concludes with a programming task, a case study, and a theoretical quiz.
*   [ ] All text is CC-0, code is Apache-2.0, and proper references/glossary terms are included.
*   [ ] Unit tests for the provided Python code examples are present and passing.

## Out of Scope
*   Covering topics outside of section F1.5 as defined in `third_party/S-5A_Ed1.0.2.md`.
*   Providing support or examples for proprietary/commercial GIS software.
