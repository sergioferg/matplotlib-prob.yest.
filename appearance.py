import matplotlib.pyplot as plt
import numpy as np
from data import get_data

data = get_data()

fig_3 = plt.figure(figsize=(6, 4))
axes_3 = fig_3.add_axes([0, 0, 1, 1])
axes_3.set_title('hello')
axes_3.plot(data['x_1'], data['y_1'])

plt.savefig('plot4.png')