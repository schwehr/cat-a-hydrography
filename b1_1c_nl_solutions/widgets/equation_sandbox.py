import numpy as np
import ipywidgets as widgets
from IPython.display import display
from b1_1c_nl_solutions.solvers import newton_raphson

def equation_sandbox():
    # UI Elements
    equation_text = widgets.Text(value='x**2 - 4', description='f(x):')
    derivative_text = widgets.Text(value='2*x', description="f'(x):")
    x0_input = widgets.FloatText(value=5.0, description='x0:')
    solve_button = widgets.Button(description='Solve')
    output_area = widgets.Output()

    def solve_equation(b):
        with output_area:
            output_area.clear_output()
            try:
                # Use eval to parse the user's function strings.
                # WARNING: In a real-world application, eval can be dangerous.
                # Here, it is used for educational purposes in a controlled environment.
                func = lambda x: eval(equation_text.value, {"x": x, "np": np})
                func_prime = lambda x: eval(derivative_text.value, {"x": x, "np": np})
                
                root = newton_raphson(func, func_prime, x0_input.value)
                print(f"Root found at: {root}")
            except Exception as e:
                print(f"Error: {e}")

    solve_button.on_click(solve_equation)
    display(equation_text, derivative_text, x0_input, solve_button, output_area)

if __name__ == '__main__':
    equation_sandbox()
