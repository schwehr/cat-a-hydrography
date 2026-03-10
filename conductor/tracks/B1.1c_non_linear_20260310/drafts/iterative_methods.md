# Section B1.2c.1: Iterative Methods

An iterative method is a mathematical procedure that generates a sequence of improving approximate solutions for a class of problems. For a non-linear equation of the form $f(x) = 0$, an iterative method begins with an initial guess (or estimates) and applies a systematic algorithmic update to converge toward the true root (solution), $\alpha$.

In scientific computing and geomatics, the choice of iterative method depends on the behavior of the function, the availability of its derivative, and the required speed of convergence.

### The Newton-Raphson Method
The Newton-Raphson method is the undisputed standard for solving non-linear equations in geodesy and hydrography due to its rapid convergence rate. It utilizes the first derivative (the gradient) of the function to project a tangent line toward the x-axis, providing the next approximation.

Given an initial guess $x_0$, the recursive update formula is:
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

*   **Convergence:** When the initial guess is sufficiently close to the true root, the Newton-Raphson method exhibits **quadratic convergence**. This means the number of correct decimal places approximately doubles with each iteration.
*   **Vulnerability:** The method will fail (divide by zero) if the derivative $f'(x_n)$ evaluates to zero. It may also diverge wildly if the function has local minima/maxima near the root or if the initial guess is too far from the true solution.

### The Secant Method
In many geospatial algorithms, calculating the exact analytical derivative $f'(x)$ is computationally expensive or mathematically impossible. The Secant method serves as a robust alternative. Instead of using a tangent line, it draws a secant line through the two most recent approximations to estimate the derivative.

The update formula requires two initial guesses, $x_0$ and $x_1$:
$$x_{n+1} = x_n - f(x_n)\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$$

*   **Convergence:** The Secant method exhibits *superlinear* convergence. It is slightly slower than Newton-Raphson but mathematically highly efficient because it bypasses the need to evaluate a derivative function.

### The Bisection Method (Bracketing)
The Bisection method is a "brute-force" algorithm based on the Intermediate Value Theorem. If a continuous function $f(x)$ has opposite signs at the endpoints of an interval $[a, b]$ (i.e., $f(a) \cdot f(b) < 0$), a root must exist within that interval.

The algorithm calculates the midpoint $c = \frac{a+b}{2}$. It then evaluates $f(c)$ and replaces either $a$ or $b$ with $c$ to narrow the bracket containing the root.
*   **Convergence:** The Bisection method has **linear convergence**. While it is computationally slow compared to Newton-Raphson, it is universally stable and *guaranteed* to converge as long as the initial bracket contains a root. It is often used to get a sufficiently close estimate before switching to Newton-Raphson for rapid finalization.
