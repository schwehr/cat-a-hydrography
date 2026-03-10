import numpy as np
import ipywidgets as widgets
from IPython.display import display

from b1_1c_nl_solutions.precision import demonstrate_catastrophic_cancellation

def rounding_error_explorer():
    # UI Elements
    x_slider = widgets.FloatLogSlider(
        value=1e-8,
        base=10,
        min=-16,
        max=-1,
        step=0.2,
        description='x value'
    )
    
    # Plotting function
    def explore(x):
        naive, robust = demonstrate_catastrophic_cancellation(x)
        print(f"Naive result:  {naive}")
        print(f"Robust result: {robust}")
        print(f"Absolute Error: {abs(naive - robust)}")
        if robust != 0:
            print(f"Relative Error: {abs(naive - robust)/robust:.2%}")

    widgets.interactive(explore, x=x_slider)

if __name__ == '__main__':
    rounding_error_explorer()
