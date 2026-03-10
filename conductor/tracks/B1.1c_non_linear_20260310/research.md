# Mathematical Parameters for ECEF to Geodetic

## Overview
Converting Earth-Centered, Earth-Fixed (ECEF) coordinates to Geodetic coordinates (Latitude $\phi$, Longitude $\lambda$, Height $h$) is a classic non-linear problem in hydrography and geodesy.

## Reference Ellipsoid (WGS84)
- Semi-major axis ($a$): 6378137.0 m
- Flattening ($f$): 1 / 298.257223563
- First eccentricity squared ($e^2$): $2f - f^2 \approx 0.00669437999014$

## Iterative Formulation
Given ECEF coordinates $(X, Y, Z)$:
1. Calculate longitude (direct):
   $\lambda = \text{atan2}(Y, X)$

2. Let $p = \sqrt{X^2 + Y^2}$

3. The equation for latitude is non-linear because both $N$ (prime vertical radius of curvature) and $h$ depend on $\phi$:
   $N(\phi) = \frac{a}{\sqrt{1 - e^2 \sin^2 \phi}}$
   $h = \frac{p}{\cos \phi} - N(\phi)$
   $\tan \phi = \frac{Z}{p} \left( 1 - e^2 \frac{N(\phi)}{N(\phi) + h} \right)^{-1}$

4. **Iterative Solution (Newton-Raphson or Successive Substitution):**
   - Initial guess: $\phi_0 = \text{atan2}\left(Z, p(1 - e^2)\right)$
   - Iterate $\phi_{i+1} = \text{atan2}\left( Z + e^2 N(\phi_i) \sin \phi_i, p \right)$
   - Iterate until $|\phi_{i+1} - \phi_i| < \epsilon$ (e.g., $\epsilon = 1 \times 10^{-12}$ radians).
