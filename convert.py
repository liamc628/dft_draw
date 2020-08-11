import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.animation import FuncAnimation
# import draw_input
import new_draw_input


"""
returns
fft: frequency distribution based on 'points'
phase: initial phase angles
fft_ind: indicies of the 'num' largest fft values
"""
def freq(points, num):

    #discrete fourier transform
    fft = np.fft.fft(points)
    N = fft.size

    phase = np.angle(fft)
    fft = (1 / N) * np.abs(fft)

    # FFT bar plot
    #plt.bar(bin, fft)

    # find indices of the 'num' largest values
    fft_ind = (-fft).argsort()[:num]
    fft_ind = np.sort(fft_ind)


    # only keep the 'num' largest values
    fft = fft[fft_ind]
    phase = phase[fft_ind]


    return fft, phase, fft_ind


def draw(t):
    global x_data
    global y_data
    global circ
    global lines

    # draws path
    x_val = np.dot(z_amps, np.cos(2 * np.pi * bin * t + z_phase))
    y_val = np.dot(z_amps, np.sin(2 * np.pi * bin * t + z_phase))

    x_data = np.append(x_data, x_val)
    y_data = np.append(y_data, y_val)

    line.set_xdata(x_data)
    line.set_ydata(y_data)

    # draws circles
    for i in range(1, circ.size):
        c_prev = circ[i - 1]
        circ[i].center = (c_prev.center[0]+c_prev.radius * np.cos(2 * np.pi * bin[i-1] * t + z_phase[i-1]),
                          c_prev.center[1]+c_prev.radius * np.sin(2 * np.pi * bin[i-1] * t + z_phase[i-1]))

    # draws lines
    for i in range(lines.size):
        lines[i].set_data([circ[i].center[0],circ[i].center[0]+circ[i].radius*np.cos(2*np.pi*bin[i]*t+z_phase[i])],
                                         [circ[i].center[1],circ[i].center[1]+circ[i].radius*np.sin(2*np.pi*bin[i]*t+z_phase[i])])

    return line,


def init_circles():
    global z_amps
    global z_phase
    global bin

    ind = np.argsort(-z_amps)
    z_amps = z_amps[ind]
    z_phase = z_phase[ind]
    bin = bin[ind]

    """
    print('z_amps', z_amps)
    print('z_phase', z_phase)
    print('bin',bin)
    """


    circ = np.array([plt.Circle((0,0), z_amps[0], fill = False)])
    for i in range(1, z_amps.size):
        prev_phase = z_phase[i-1]
        prev_amp = z_amps[i-1]
        circ = np.append(circ, plt.Circle((prev_amp*np.cos(prev_phase), prev_amp*np.sin(prev_phase)), z_amps[i], fill=False))
        # print(circ[i].center)
    return circ




x_data = np.array([])
y_data = np.array([])


N = new_draw_input.data.size
T = 1 # increase to slow down
fs = new_draw_input.data.size/T # number of freq. samples/unit

print(N)
num_cycles = 100 # max number of cycles used (increase for more precision)


t = np.linspace(0, T, N)
bin = np.fft.fftfreq(N, d=1/fs)


# horizontal line test
# z_amps, z_phase, fft_indices = freq(np.exp(2*np.pi*1j*t)+np.exp(-2*np.pi*1j*t), num_cycles)

# square test
# z_amps, z_phase, fft_indices = freq(10*(np.array([-1,0,1,1,1,0,-1,-1])+1j*np.array([1,1,1,0,-1,-1,-1,0])), num_cycles)

# triangle test
#z_amps, z_phase, fft_indices = freq(10*(np.array([-1,-0.5,0,0.5,1,0])+1j*np.array([0,0.5,1,0.5,0,0])), num_cycles)

# user data
z_amps, z_phase, fft_indices = freq(new_draw_input.data, num_cycles)



bin = bin[fft_indices]


fig, ax = plt.subplots()
ax.axis('off')

ax.set_xlim(0, new_draw_input.d.width)
ax.set_ylim(-new_draw_input.d.height,0)
line, = ax.plot(0, 0)


step = 0.01
interval = 50

circ = init_circles()

#init lines
lines = np.array([])
for i in range(circ.size):
    lines = np.append(mlines.Line2D([circ[i].center[0], circ[i].center[0]+circ[i].radius*np.cos(z_phase[i])],
                                    [circ[i].center[1], circ[i].center[1]+circ[i].radius*np.sin(z_phase[i])]), lines)
for i in range(circ.size):
    ax.add_patch(circ[i])
    ax.add_line(lines[i])


animation = FuncAnimation(fig, func=draw, frames=np.arange(0, T, step), interval=interval)
plt.show()




