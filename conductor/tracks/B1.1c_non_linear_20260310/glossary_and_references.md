# Glossary & References: Numerical Solutions of Non-Linear Equations

## Glossary
- **Bisection Method:** A root-finding algorithm that repeatedly bisects an interval and then selects a subinterval in which a root must lie for further processing. [Wikipedia](https://en.wikipedia.org/wiki/Bisection_method)
- **Conditioning (Root):** A measure of how sensitive the solution (root) of a non-linear equation is to small changes in the function values or initial parameters. Highly dependent on the derivative $f'(\alpha)$ at the root.
- **ECEF (Earth-Centered, Earth-Fixed):** A Cartesian coordinate system defined with its origin at the center of mass of the Earth. [Wiktionary](https://en.wiktionary.org/wiki/ECEF)
- **Forward Error:** The absolute difference between the exact analytical solution and the computed numerical approximation.
- **Backward Error (Residual):** The magnitude of the function evaluated at the approximated root, i.e., $|f(x_{approx})|$.
- **Newton-Raphson Method:** An iterative root-finding algorithm that produces successively better approximations to the roots of a real-valued function using its first derivative. [Wikipedia](https://en.wikipedia.org/wiki/Newton%27s_method)
- **Round-off Error:** Error introduced in calculations because computers represent continuous real numbers using discrete, finite-precision floating-point formats (e.g., IEEE 754).
- **Secant Method:** A root-finding algorithm that uses a succession of roots of secant lines to better approximate a root of a function, avoiding the need to compute derivatives analytically. [Wikipedia](https://en.wikipedia.org/wiki/Secant_method)
- **Truncation Error:** The error made by truncating an infinite sum or an infinite iterative sequence and approximating it with a finite number of steps.

## Primary References
- IHO S-5A Standards of Competence for Category "A" Hydrographic Surveyors (Ed 1.0.2). [IHO Publication](https://iho.int/iho_pubs/standard/S-5/S-5A_Ed1.0.2.pdf)
- Numerical Analysis textbooks regarding IEEE 754 floating-point standard and root finding stability (e.g., *Numerical Linear Algebra* by Trefethen and Bau).
- GCMD Earth Science Keywords (for standardized geospatial terminology). [NASA GCMD](https://gcmd.earthdata.nasa.gov/KeywordViewer/scheme/all)
