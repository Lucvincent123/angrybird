import tkinter as tk
from threading import Thread

import constants as c
from Loop import Loop
from models import Window, System, Planet

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.geometry("800x500")
        self.title(c.APP_TITLE)
        self.geometry("+0+0")
        self.canvas = Window.Window(c.CANVAS_WIDTH, c.CANVAS_HEIGHT, c.BACKGROUND_COLOR)
        self.earth = Planet.Planet(10, 10, "lightblue", 100, 100)
        self.sun = Planet.Planet(100, 40,"lightyellow", 500, 500)
        # self.earth.draw(self.canvas)
        self.solar_system = System.System()
        self.solar_system.add_planet(self.earth)
        self.solar_system.add_planet(self.sun)
        self.earth.update_velocity((1,2))
        Loop(self, 100, self.draw_system)
        # self.solar_system.draw(self.canvas)
        self.after(5000, self.turn)

    def turn(self):
        self.earth.update_velocity((1, -1))

    def draw_system(self):
        self.solar_system.draw(self.canvas)
        self.solar_system.move()

if __name__ == "__main__":
    app = App()
    app.mainloop()
    # print("hello")
