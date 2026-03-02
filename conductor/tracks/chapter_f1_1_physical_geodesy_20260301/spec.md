# Specification: Chapter F1.1 Physical Geodesy

## Overview
This track involves creating Chapter F1.1, "Physical Geodesy," for the TeachBook template, covering gravity fields, height systems, and geopotential modeling as required by the IHO Cat A hydrographer certification (S-5A_Ed1.0.2). 

## Instructional Approach
- **Tone:** Academic and Action-Oriented.
- **Pedagogy:** Problem-Based Learning. The chapter should utilize problem scenarios to introduce theoretical concepts.
- **Focus:** A balanced mix of geodetic theory and practical computations.

## Functional Requirements
The chapter must cover the following topics in order, aligning with S-5A Ed1.0.2:

1.  **F1.1a Gravity field of the Earth**
    *   (i) Equipotential surfaces
    *   (ii) Gravity and gravity anomalies
2.  **F1.1b Global geopotential models**
    *   (i) Spherical harmonics
3.  **F1.1c Height systems**
    *   (i) Dynamic, orthometric, and normal heights
4.  **F1.1d Deflection of the vertical**
    *   (i) Deflection of the vertical and its components

## Interactivity & UX
- **Problem Scenarios:** Introduce concepts (e.g., transforming coordinates, identifying the correct height system for water flow) using real-world hydrographic scenarios.
- **Python Snippets:** Provide functional Python code for geodetic calculations (e.g., calculating theoretical gravity, converting between height systems mathematically if applicable, modeling spherical harmonic expansions conceptually).
- **SQLite/DuckDB:** (Optional) If large dataset examples are used for gravity anomalies, incorporate them, per the updated Tech Stack.

## Non-Functional Requirements
- **References:** Utilize inline definitions (linking to Wikipedia/Wiktionary), GCMD Keyword Viewer links, and external primary geodetic reference documents (e.g., NGS, IHO publications).
- **Licensing:** Text and generated data must be CC-0. Code must be Apache-2.0.
- **Environment:** Assume students use Ubuntu Linux with possible remote Windows access. 

## Acceptance Criteria
- Chapter F1.1 is complete, covering all specified S-5A topics.
- Content relies on a Problem-Based Learning structure.
- Python snippets are provided and unit-tested where feasible.
- Terminology is properly linked to external definitions and primary sources.