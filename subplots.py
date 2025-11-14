import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0, 5)  # Sample data.
y_1 = x_1**2
y_2 = np.exp(x_1)
x_3 = np.linspace(0.01, 5)
y_3 = np.log(x_3)

fig_2, axes_2 = plt.subplots(figsize=(8,4), nrows=1, ncols=3)
plt.tight_layout()
axes_2[1].set_title('plot 2')
axes_2[1].set_xlabel('x')
axes_2[1].set_ylabel('x²')
axes_2[1].plot(x_1, y_1, 'm')

axes_2[0].set_title('plot 1')
axes_2[0].set_xlabel('x')
axes_2[0].set_ylabel('e^x')
axes_2[0].plot(x_1, y_2, color='burlywood')

axes_2[2].set_title('plot 3')
axes_2[2].set_xlabel('x')
axes_2[2].set_ylabel('logn(x)')
axes_2[2].plot(x_1, y_3, 'k')

plt.savefig('plot3.png', bbox_inches='tight')