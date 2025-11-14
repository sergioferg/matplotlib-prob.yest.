import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0, 5, 10)  # Sample data.
y_1 = x_1**2

fig_1 = plt.figure(figsize=(5,4))
axes_1 = fig_1.add_axes([0.1,0.1,0.9,0.9])
axes_1.set_xlabel('days')
axes_1.set_ylabel('days²')
axes_1.set_title('days chart')
axes_1.plot(x_1,y_1,label='x/x²')
axes_1.plot(y_1,x_1,label='x²/x')
axes_1.legend(loc=0)
# fig_1.tight_layout()

axes_2 = fig_1.add_axes([0.4,0.4,0.35,0.3])
axes_2.set_title('days chart 2')
axes_2.plot(x_1,y_1,label='x/x²')

axes_2.text(0,10, 'message')


plt.savefig("plot2.png", bbox_inches='tight')       