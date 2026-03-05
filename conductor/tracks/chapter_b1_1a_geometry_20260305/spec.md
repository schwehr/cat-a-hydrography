# Specification: Chapter B1.1a - Geometry

## Overview
Create a new chapter covering section B1.1a on Geometry for the IHO Cat A hydrographer certification TeachBook. The chapter will focus on Conic Sections, the geometry of the ellipse and ellipsoid, and parametric equations of curves and surfaces, based on the `S-5A_Ed1.0.2.md` syllabus.

## Scope
- Extract relevant syllabus topics from `third_party/S-5A_Ed1.0.2.md`.
- Incorporate and expand upon the foundational mathematical theory provided in `deepresearch/b1.1a-geometry-report-conic-sections-and-parametric-equations.md`.
- The chapter will be formatted as a MyST Markdown file (`.md`) suitable for Jupyter Book rendering.

## Functional Requirements
- **Content:**
  - Define and explore Conic Sections (circle, ellipse, parabola, hyperbola) with a focus on eccentricity and projective geometry.
  - Detail the geometry of the ellipse and reference ellipsoid, crucial for hydrographic positioning.
  - Explain parametric equations of curves and surfaces in 2D and 3D space.
- **Tone & Depth:**
  - Maintain a balanced approach, combining theoretical rigor (mathematical proofs and derivations) with practical Problem-Based Learning (PBL) applications.
- **Interactive & Programmatic Elements:**
  - Include executable Python code snippets to calculate ellipse parameters and plot parametric equations.
  - Integrate `ipywidgets` to create interactive sliders and visualizations (e.g., demonstrating how changing eccentricity alters a conic section).
  - Provide unit tests for the Python calculations to adhere to the project's high code coverage guidelines.
- **Project Guidelines Adherence:**
  - Ensure all answers/claims have proper references.
  - Use open-source software/libraries (e.g., `pyproj`, `matplotlib`, `numpy`). No AGPL software.
  - Include a glossary of terms for students unfamiliar with the field, linking to primary references or the NASA GCMD Keyword Viewer.
  - Content must be CC-0 licensed, and code must be Apache-2.0 licensed.

## Non-Functional Requirements
- **Accessibility:** Must be readable and fully functional on Ubuntu Linux environments (the target student OS).
- **Format:** Must compile successfully with Sphinx/Jupyter Book.

## Out of Scope
- Topics outside of B1.1a (e.g., Linear Algebra B1.1b and Numerical Methods B1.1c).
- Advanced geodetic datum transformations not directly related to basic ellipsoid geometry.

## Acceptance Criteria
- [ ] A new `.md` file for Chapter B1.1a is created in the appropriate book directory.
- [ ] The chapter successfully builds via Jupyter Book without warnings or errors.
- [ ] Python code blocks execute successfully and are covered by unit tests.
- [ ] `ipywidgets` visualizations render and function correctly.
- [ ] All terminology is clearly defined and referenced.