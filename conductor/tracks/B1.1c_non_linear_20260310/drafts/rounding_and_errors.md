# Section B1.2c.2: Rounding and Numerical Errors

The transition from continuous analytical mathematics to applied numerical methods introduces profound operational complexities. Analytical algebra assumes infinite precision, whereas scientific computing relies exclusively on discrete, finite-precision floating-point arithmetic.

To safely apply non-linear numerical solvers, a hydrographer must understand the sources of computational error, how they propagate, and how to analyze the reliability of an output.

### Truncation Error vs. Round-off Error
Errors in numerical non-linear solvers are broadly categorized into two distinct types:
*   **Truncation Error (Method Error):** This error arises directly from the mathematical approximation. For example, iterative methods theoretically require an infinite number of steps to reach the exact true solution. By stopping the algorithm after $N$ iterations (based on our stopping criteria), we inherently "truncate" the process, leaving a small remaining mathematical error.
*   **Round-off Error:** This error is dictated by hardware limitations. Because all digital computers utilize floating-point representations (typically IEEE 754 64-bit double precision), irrational numbers and repeating decimals cannot be perfectly stored. The truncation of infinite real numbers into finite binary strings creates microscopic discrepancies during every arithmetic operation. In iterative algorithms, where the output of one step becomes the input of the next, round-off errors can accumulate destructively.

### Forward Error, Backward Error, and Residuals
When auditing the numerical fidelity of an iterative solver, the analysis relies on the concepts of forward and backward error. Let $\alpha$ represent the exact, theoretically true root, and let $x_{approx}$ represent our computed numerical approximation.

*   **Forward Error:** Measures the absolute distance between our approximation and the truth: $|x_{approx} - \alpha|$. In practical geomatics, the forward error is inherently unknowable because the "true" physical coordinate is exactly what we are trying to find.
*   **Backward Error (The Residual):** Because forward error is hidden, we substitute our approximation back into the original function to generate a residual: $R = |f(x_{approx})|$. The residual mathematically quantifies how well the computed approximation satisfies the equation.

### The Conditioning of a Root
A highly dangerous misconception in scientific computing is the assumption that achieving a very small residual (backward error) guarantees a highly accurate solution (small forward error).

In linear systems, this relationship is governed by the *Condition Number* of the matrix. For non-linear equations, the conditioning of a root depends entirely on the derivative of the function at the root, $f'(\alpha)$.

The relationship between forward error and backward error is bounded by:
$$ 	ext{Forward Error} \approx \frac{	ext{Backward Error}}{|f'(x_{approx})|} $$
$$ |x_{approx} - \alpha| \approx \frac{|f(x_{approx})|}{|f'(x_{approx})|} $$

**Practical Implications:**
*   **Well-Conditioned Root:** If the tangent line is steep ($|f'(x)|$ is large), the root is well-conditioned. A small residual reliably guarantees a small forward error. The iterative solver is safe and accurate.
*   **Ill-Conditioned Root:** If the tangent line is nearly horizontal ($|f'(x)|$ is very close to zero), the root is pathologically ill-conditioned. In this scenario, dividing a microscopic residual by a microscopic derivative can result in a massive forward error. The computed answer may reside dangerously far from the true physical solution, despite the computer reporting that $f(x) \approx 0$.
