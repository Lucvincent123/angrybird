import tkinter as tk

class Window(tk.Canvas):
    def __init__(self, width, height, background_color):
        super().__init__(width=width, height=height, background=background_color)
        self.width = width
        self.height = height
        self.pack()
        self.bind("<Configure>", self.reset_size)
    
    def reset_size(self, event):
        self.width = event.width
        self.height = event.height
        # print(self.width, self.height)