import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from PIL import Image, ImageFilter
from matplotlib.animation import FuncAnimation

"""
image_path = "C:\\Users\\monke\\OneDrive\\Desktop\\yod.jpeg"
im = Image.open(image_path)
im = image.filter(ImageFilter.FIND_EDGES)
im.show()
"""

def test(t):
    global c
    c.radius = t
    ax.add_patch(c)
    return []


fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
line, = ax.plot(0, 0)



c = plt.Circle((0,0),1)
animation = FuncAnimation(fig, func = test,  frames=np.arange(0, 1, 0.01), interval=10, blit=True)
plt.show()








