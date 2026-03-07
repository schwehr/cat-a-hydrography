# Specification: Chapter B1.1b - Linear Algebra

## 1. Overview
Create Chapter B1.1b on "Linear Algebra" for the Cat A hydrographer certification TeachBook. The chapter will translate theoretical mathematical concepts into practical geomatics and hydrographic surveying applications using Problem-Based Learning (PBL). The content will be delivered via Jupyter Notebooks and will leverage material from `deepresearch/b1.1b-linear-algebra-in-geodesy.md`, supplemented to cover all topics outlined in `third_party/S-5A_Ed1.0.2.md`.

## 2. Functional Requirements
* **Topic Coverage:** Strictly follow the topics and order from IHO S-5A Section B1.1b:
  * (i) Vector and affine spaces, vector and inner products, norms.
  * (ii) Linear operators, matrix representation, composition, transpose.
  * (iii) Translations, rotations, and further spatial transformations.
* **Content Integration:** Incorporate and expand upon the provided `deepresearch/b1.1b-linear-algebra-in-geodesy.md` document to ensure correctness and completeness.
* **Python Implementations:** Provide concrete code examples for all mathematical operations using `NumPy` (matrices/arrays), `SciPy` (advanced solvers), and `SymPy` (symbolic derivations).
* **Interactivity:** Develop interactive visual demonstrations using `ipywidgets` to help students dynamically explore concepts such as translations, rotations, and eigenvalues/eigenvectors.
* **Problem-Based Learning Data:** Use a hybrid data strategy:
  * *Synthetic Data:* For introducing foundational matrix operations and basic concepts.
  * *Real-world Data:* For advanced exercises (e.g., GNSS, IMU, MBES georeferencing and spatial transformations).
* **Glossary & References:** Include a glossary for all new acronyms and terms. Link terms to primary references, Wikipedia/Wiktionary, and the NASA GCMD Keyword Viewer.

## 3. Non-Functional Requirements
* **Licensing:** All text and generated synthetic data must be strictly CC-0. All Python code snippets and unit tests must be Apache-2.0. Explicitly reference SPDX identifiers.
* **Open Source:** Strictly use open-source tools. Do not use any AGPL or similarly restrictively licensed software.
* **Environment:** Ensure compatibility with Ubuntu Linux and Jupyter Book/Sphinx build systems.
* **Testing:** Provide automated unit tests for all Python code examples to ensure mathematical correctness.

## 4. Acceptance Criteria
* [ ] The chapter successfully builds within the Jupyter Book environment without errors.
* [ ] All S-5A B1.1b topics (vector/affine spaces, inner products, linear operators, translations, rotations) are covered in the correct order.
* [ ] Python examples are present, using NumPy, SciPy, and SymPy as appropriate, and include passing unit tests.
* [ ] At least two interactive `ipywidgets` are included (e.g., visualizing a 2D/3D rotation or translation).
* [ ] PBL exercises utilize both synthetic and real-world hydrographic/geodetic data.
* [ ] Glossary is fully populated with required external links (NASA GCMD, Wikipedia).
* [ ] Licensing headers (CC-0 for text/data, Apache-2.0 for code) are correctly applied.