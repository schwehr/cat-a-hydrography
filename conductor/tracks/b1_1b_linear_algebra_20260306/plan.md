# Implementation Plan: Chapter B1.1b - Linear Algebra

## Phase 1: Setup and Documentation Skeleton [checkpoint: e20b0ee]
- [x] Task: Initialize Chapter Structure 6bc3267
    - [x] Create the primary Jupyter Notebook (`b1.1b_linear_algebra.ipynb` or Markdown equivalent depending on Jupyter Book config).
    - [x] Add explicit CC-0 licensing header for text/data and Apache-2.0 header for code blocks (using SPDX identifiers).
    - [x] Create the glossary section skeleton and link to primary references, Wikipedia/Wiktionary, and NASA GCMD Keyword Viewer.
- [x] Task: Import Initial Content 6bc3267
    - [x] Import and format the existing content from `deepresearch/b1.1b-linear-algebra-in-geodesy.md`.
- [x] Task: Conductor - User Manual Verification 'Setup and Documentation Skeleton' e20b0ee (Protocol in workflow.md)

## Phase 2: Topic (i) - Vector/Affine Spaces, Inner Products, Norms [checkpoint: edf935e]
- [x] Task: Implement Mathematical Foundations
    - [x] Write failing unit tests for vector space operations, inner products, and norms (Red Phase).
    - [x] Write Python code snippets using `SymPy` to show theoretical vector/affine spaces and `NumPy` for numerical inner products and norms (Green Phase).
    - [x] Refactor and ensure coverage > 80%.
- [x] Task: Draft Educational Content
    - [x] Integrate the math snippets into the notebook.
    - [x] Write explanatory text for Topic (i) emphasizing geodetic applications (synthetic data focus).
    - [x] Update glossary with relevant terms (e.g., Vector Space, Affine Space, Norm).
- [x] Task: Conductor - User Manual Verification 'Topic (i) - Vector/Affine Spaces, Inner Products, Norms' edf935e (Protocol in workflow.md)

## Phase 3: Topic (ii) - Linear Operators, Matrix Representation [checkpoint: 3fb30f5]
- [x] Task: Implement Matrix Operations
    - [x] Write failing unit tests for matrix representations, compositions (multiplication), and transposes (Red Phase).
    - [x] Write Python code snippets using `NumPy` and `SciPy` for linear operators (Green Phase).
    - [x] Refactor and ensure coverage > 80%.
- [x] Task: Draft Educational Content
    - [x] Integrate the matrix operation snippets into the notebook.
    - [x] Write explanatory text for Topic (ii).
    - [x] Update glossary with relevant terms (e.g., Linear Operator, Transpose, Matrix).
- [x] Task: Conductor - User Manual Verification 'Topic (ii) - Linear Operators, Matrix Representation' 3fb30f5 (Protocol in workflow.md)

## Phase 4: Topic (iii) - Translations, Rotations, Spatial Transformations [checkpoint: 2ae2107]
- [~] Task: Implement Spatial Transformations - [ ] Task: Implement Spatial Transformations & Interactivity Interactivity
    - [x] Write failing unit tests for 2D and 3D translation and rotation matrices (Red Phase).
    - [x] Write Python code for translations and rotations (Green Phase).
    - [x] Develop interactive `ipywidgets` to visually demonstrate rotations (e.g., pitch, roll, yaw) and translations.
    - [x] Refactor and ensure coverage > 80%.
- [x] Task: Develop Real-World PBL Exercises
    - [x] Create a Problem-Based Learning exercise applying linear algebra to GNSS/IMU or MBES georeferencing using real-world data constraints.
- [x] Task: Draft Educational Content
    - [x] Integrate transformation code, widgets, and the PBL exercise into the notebook.
    - [x] Write explanatory text for Topic (iii).
    - [x] Update glossary with relevant terms (e.g., Translation, Rotation Matrix, Euler Angles).
- [x] Task: Conductor - User Manual Verification 'Topic (iii) - Translations, Rotations, Spatial Transformations' 2ae2107 (Protocol in workflow.md)

## Phase 5: Final Review and Build Verification
- [ ] Task: Verify Project Integration
    - [ ] Run the complete test suite for the chapter and verify >80% coverage.
    - [ ] Build the Jupyter Book locally to ensure no syntax or formatting errors in the Sphinx build process.
    - [ ] Perform a final review of the glossary to ensure all links (NASA GCMD, Wikipedia) are functional.
- [ ] Task: Conductor - User Manual Verification 'Final Review and Build Verification' (Protocol in workflow.md)