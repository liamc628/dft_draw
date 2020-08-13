import numpy as np
from tkinter import *
from tkinter import ttk


class Draw:
    def __init__(self, root):
        self.root = root
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.root.geometry("%dx%d" %(self.width, self.height))
        self.root.configure(bg = 'black')
        self.canvas = Canvas(root, bg = 'black', width = self.width, height = self.height)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.start)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.data_x = np.array([])
        self.data_y = np.array([])


    def start(self, event):
        self.prev_x = event.x
        self.prev_y = event.y
        self.data_x = np.append(self.data_x, self.prev_x)
        self.data_y = np.append(self.data_y, self.prev_y)


    def draw(self, event):
        x = event.x
        y = event.y
        self.data_x = np.append(self.data_x, x)
        self.data_y = np.append(self.data_y, y)

        self.canvas.create_line(self.prev_x,self.prev_y,x,y, fill = "white", width = 1)
        self.prev_x = x
        self.prev_y = y

root = Tk()
d = Draw(root)
root.mainloop()

data = (d.data_x - 1j*d.data_y)
print(data)
data = data + (-d.width/2+1j*d.height/2)
print(data)

