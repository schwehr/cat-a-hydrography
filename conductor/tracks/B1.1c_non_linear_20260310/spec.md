# Specification: B1.1c Numerical Solutions of Non-Linear Equations

## Overview
This track involves authoring Chapter B1.1c for the TeachBook, covering the "Numerical solutions of non-linear equations" module as defined by the IHO S-5A Standards of Competence for Category "A" Hydrographic Surveyors. The content will blend academic rigor with practical Python-based implementations and applied hydrographic scenarios.

## Functional Requirements
- **Theoretical Content:**
  - Detailed explanation of **Iterative Methods**: Newton-Raphson, Secant, and Bisection methods.
  - Comprehensive analysis of **Rounding and Numerical Errors**: Floating-point precision (IEEE 754), truncation error, round-off error, forward/backward error, and root conditioning.
  - Adherence to the structure and topic order of `third_party/S-5A_Ed1.0.2.md`.
- **Python Implementations:**
  - Standard implementations for Newton-Raphson, Secant, and Bisection algorithms.
  - Demonstrations of floating-point precision issues and rounding errors using NumPy.
  - A hydrographic case study (e.g., ECEF to Geodetic coordinate conversion or ray-tracing for acoustic refraction).
- **Interactive Features (ipywidgets):**
  - **Convergence Visualization:** Animated/interactive plots showing algorithm progression.
  - **Rounding Error Explorer:** Tool to adjust precision and observe impact on results.
  - **Equation Sandbox:** Input field for custom non-linear equations to test solvers.
- **Ecosystem Integration:**
  - Reference commercial alternatives: MATLAB, CARIS HIPS/SIPS, Trimble Business Center, and ArcGIS Pro.
  - Provide a glossary of terms and links to primary references (Wikipedia, EarthData, etc.).
  - All content must include verifiable citations.

## Non-Functional Requirements
- **Platform Compatibility:** Functional on Ubuntu Linux and accessible via MS Windows remote VM.
- **Licensing:** Text/data under CC-0; Code under Apache-2.0.
- **Style:** Professional, senior-engineer tone.

## Acceptance Criteria
- Chapter B1.1c is successfully integrated into the TeachBook structure.
- All Python examples include unit tests with >80% coverage.
- Interactive widgets are fully functional within the Jupyter environment.
- No use of AGPL-licensed software.
- Correctness and completeness verified against IHO S-5A requirements.

## Out of Scope
- Solving linear systems (covered in B1.1c-linear-systems).
- Advanced multivariate non-linear optimization (unless specifically needed for the case study).
