import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
import numpy as np
from data import get_data

data = get_data()

fig_3 = plt.figure(figsize=(6, 4))
axes_3 = fig_3.add_axes([0, 0, 1, 1])

# Default colors (b: blue, g: green, r: red, c: cyan, m: magenta,
# y: yellow, k: black, w: white)
# color="0.75" creates a 75% gray
# You can use hexcodes color="#eeefff"
# You can use color names found next like this color="burlywood"
# https://en.wikipedia.org/wiki/Web_colors
# alpha defines the percentage of opacity

# The default line width is 1, so to double it put in 2 and so forth

# There are many line styles 
# matplotlib.org/3.1.0/gallery/lines_bars_and_markers/linestyles.html
# You can also provide a sample like '-.'

# Markers can mark your provided points on the graph
# https://matplotlib.org/3.3.0/api/markers_api.html
# You can change the markersize as well

# markerfacecolor changes the marker fill color
# markeredgecolor changes the marker stroke color
# markeredgewidth changes the markers stroke size



axes_3.plot(data['x_1'], data['y_1'],color='navy', lw=1.5, 
            ls='-.', marker='*', markersize=5, markerfacecolor=to_rgba('k', 0), 
            markeredgecolor=to_rgba('k', 0), markeredgewidth=1)

axes_3.set_xlim([0,4])
axes_3.set_ylim([-0.1,16])

# Add a grid, color, dashes(5pts 1 pt dashes separated by 2pt space)
axes_3.grid(True, color='0.7', dashes=(5,2,1,2))

# Set grid background color
axes_3.set_facecolor(to_rgba('turquoise', 0.1))

fig_3.savefig('plot4.png', bbox_inches='tight')