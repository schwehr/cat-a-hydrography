import numpy as np
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt

from b1_1c_nl_solutions.solvers import bisection, newton_raphson, secant

def plot_convergence():
    # Define the function and its derivative
    def func(x):
        return x**2 - 4
    def func_derivative(x):
        return 2*x
        
    # UI Elements
    method_selector = widgets.Dropdown(options=['Bisection', 'Newton-Raphson', 'Secant'], description='Method:')
    
    # Plotting function
    def plot(method):
        fig, ax = plt.subplots()
        x = np.linspace(0, 5, 100)
        ax.plot(x, func(x))
        ax.axhline(0, color='black', lw=0.5)

        if method == 'Bisection':
            # Bisection steps
            a, b = 0, 5
            for i in range(5):
                c = (a + b) / 2
                ax.plot(c, func(c), 'ro-')
                if func(a) * func(c) < 0:
                    b = c
                else:
                    a = c
        elif method == 'Newton-Raphson':
            # Newton-Raphson steps
            x_n = 5
            for i in range(3):
                ax.plot(x_n, func(x_n), 'go-')
                x_n = x_n - func(x_n)/func_derivative(x_n)
        elif method == 'Secant':
            # Secant steps
            x0, x1 = 4, 5
            for i in range(3):
                ax.plot(x1, func(x1), 'bo-')
                x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
                x0, x1 = x1, x2
                
        ax.set_title(f'{method} Convergence')
        plt.show()

    widgets.interactive(plot, method=method_selector)

if __name__ == '__main__':
    plot_convergence()
