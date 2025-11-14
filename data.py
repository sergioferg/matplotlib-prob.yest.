import numpy as np

x_1 = np.linspace(0, 5)  # Sample data.
y_1 = x_1**2
y_2 = np.exp(x_1)
x_3 = np.linspace(0.01, 5)
y_3 = np.log(x_3)

def get_data():
    return dict(x_1=x_1, y_1=y_1, y_2=y_2, x_3=x_3, y_3=y_3)