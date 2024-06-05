import tkinter as tk

class Window(tk.Canvas):
    slots = ["width", "height", "is_clicked"]

    def __init__(self, root, width, height, background_color):
        super().__init__(root, width=width, height=height, background=background_color)
        self.width = width
        self.height = height
        self.is_clicked = False
        self.bind("<Configure>", self.update_size)

    def update_size(self, event):
        self.width = event.width
        self.height = event.height


