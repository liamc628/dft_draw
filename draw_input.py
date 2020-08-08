from matplotlib import pyplot as plt
import numpy as np

class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
        self.cid = line.figure.canvas.mpl_connect('button_release_event', self)

    def __call__(self, event):
        #print('click', event)
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)
x_ax = [-15,15]
y_ax = [-15,15]
ax.set_xlim(x_ax[0], x_ax[1])
ax.set_ylim(y_ax[0], y_ax[1])

line, = ax.plot([], [], linestyle = '', marker = '.')
linebuilder = LineBuilder(line)
plt.show()
data = (np.array(linebuilder.xs)+1j*np.array(linebuilder.ys))