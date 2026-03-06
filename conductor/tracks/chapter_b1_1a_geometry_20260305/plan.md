# Implementation Plan: Chapter B1.1a - Geometry

## Phase 1: Setup and Structuring [checkpoint: 79ad502]
- [x] Task: Create the new chapter file
    - [x] Determine the exact path in the book's repository structure for Chapter B1.1a.
    - [x] Create the Markdown file (`.md`) with the correct MyST headers and CC-0/Apache-2.0 license tags.
- [x] Task: Establish the chapter outline
    - [x] Add main headings corresponding to the syllabus topics: Conic Sections, Geometry of the Ellipse/Ellipsoid, and Parametric Equations.
    - [x] Import foundational text from the `deepresearch/b1.1a-geometry-report-conic-sections-and-parametric-equations.md` report.
- [x] Task: Conductor - User Manual Verification 'Setup and Structuring' (Protocol in workflow.md)

## Phase 2: Core Content and Theory Implementation [checkpoint: 79ad502]
- [x] Task: Write Conic Sections content
    - [x] Detail the mathematical definitions of the circle, ellipse, parabola, and hyperbola.
    - [x] Explain eccentricity and projective geometry with appropriate references.
- [x] Task: Write Ellipse and Ellipsoid geometry content
    - [x] Connect the theoretical ellipse to the reference ellipsoid used in hydrographic surveying.
    - [x] Provide the standard geometric formulas.
- [x] Task: Write Parametric Equations content
    - [x] Explain 2D parametric equations for curves.
    - [x] Explain 3D parametric representations of spatial surfaces.
- [x] Task: Implement Glossary and References
    - [x] Identify key terminology (e.g., eccentricity, directrix, oblate spheroid) and add definitions.
    - [x] Link terms to the NASA GCMD Keyword Viewer, Wikipedia, or primary references.
- [x] Task: Conductor - User Manual Verification 'Core Content and Theory Implementation' (Protocol in workflow.md)

## Phase 3: Interactive Python and TDD Integration [checkpoint: 32a6c30]
- [x] Task: Write unit tests for Geometry calculations (Red Phase)
    - [x] Create a Python test file (e.g., `test_b1_1a_geometry.py`) for the calculations to be introduced.
    - [x] Write tests validating the calculation of eccentricity, flattening, and parametric coordinate generation.
    - [x] Ensure tests fail as expected.
- [x] Task: Implement Geometry calculation functions (Green Phase)
    - [x] Write the Python functions in the chapter's code blocks (or an imported module) to satisfy the unit tests.
    - [x] Verify that all tests pass and coverage is >80%.
- [x] Task: Integrate `ipywidgets` visualizations
    - [x] Develop interactive sliders to demonstrate how changing eccentricity affects the conic section shape.
    - [x] Ensure the widgets render correctly within the Jupyter Book environment.
- [x] Task: Conductor - User Manual Verification 'Interactive Python and TDD Integration' (Protocol in workflow.md)

## Phase 4: Final Review and Build
- [x] Task: Complete full local build
    - [x] Run the Jupyter Book/Sphinx build command (e.g., `jupyter-book build .`).
    - [x] Verify there are no warnings or missing references.
- [x] Task: Code style and linting verification
    - [x] Run the project's linters (e.g., `flake8`, `black`) on the embedded or attached Python code.
    - [x] Ensure adherence to the CC-0 and Apache-2.0 licenses.
- [x] Task: Conductor - User Manual Verification 'Final Review and Build' (Protocol in workflow.md)