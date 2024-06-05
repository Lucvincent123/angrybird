import tkinter as tk

#models
from models.Universe import Universe
from models.Planet import Planet
from models.Vector import Vector
# controllers
import controllers.constants as c
from controllers.Loop import Loop
from controllers.Controller import Controller
from controllers.EventHandler import EventHandler
#views
from views.Window import Window
from views.SwitchModeButton import SwitchModeButton
from views.NormalButton import NormalButton
from views.Menu import Menu
from views.InputCreate import InputCreate

class App(tk.Tk):
    slots = ["mode", "status", "new_planet", "arrow", "arrow_image"]

    def __init__(self):
        # Initiate the window
        super().__init__()
        self.title(c.APP_TITLE)
        self.geometry("+0+0")

        self.mode = "view"
        self.status = "active"
        self.new_planet = None
        self.new_planet_velocity = 0
        self.arrow = None
        self.arrow_image = None
        self.mouse_position = Vector(0, 0)
        self.controller = Controller(self)
        self.handler = EventHandler(self, Vector, InputCreate, Planet)
        self.universe = Universe()
        self.draw_loop = Loop(self, int(c.DELTA_T * 1000), self.draw_universe)
        ######################################################################################

        ######################################################################################
        # 2 canvas
        ## Background canvas
        self.background = Window(self, c.WIDTH, c.HEIGHT, c.BACKGROUND_COLOR_BUTTON)
        self.background.pack()
        ## Universe canvas
        self.canvas = Window(self.background, c.WIDTH - 2 * c.RADIUS_BUTTON - c.THICKNESS_OUTLINE_BUTTON, c.HEIGHT - 2 * c.RADIUS_BUTTON - c.THICKNESS_OUTLINE_BUTTON, c.BACKGROUND_COLOR)
        self.canvas.place(x = 2 * c.RADIUS_BUTTON + c.THICKNESS_OUTLINE_BUTTON, y = 2 * c.RADIUS_BUTTON + c.THICKNESS_OUTLINE_BUTTON)
        ##########################################################################################################################################################################################
        #################################################################################################################################################################
        # Buttons
        ## Switch mode button
        self.switch_mode_button = SwitchModeButton(self.background, c.RADIUS_BUTTON, c.THICKNESS_OUTLINE_BUTTON, c.BACKGROUND_COLOR_BUTTON, c.FOREGROUND_COLOR_BUTTON)
        self.switch_mode_button.draw((32.5, 32.5))
        ## horizontal tool menu
        self.tool_menu = Menu("horizontal", (120, 32.5), 10)
        ### Create button
        self.create_button = NormalButton(self.background, c.RADIUS_BUTTON, c.THICKNESS_OUTLINE_BUTTON, c.BACKGROUND_COLOR_BUTTON, c.FOREGROUND_COLOR_BUTTON, "CREATE")
        self.tool_menu.add_button(self.create_button)
        ### Delete button
        self.delete_button = NormalButton(self.background, c.RADIUS_BUTTON, c.THICKNESS_OUTLINE_BUTTON, c.BACKGROUND_COLOR_BUTTON, c.FOREGROUND_COLOR_BUTTON, "DELETE")
        self.tool_menu.add_button(self.delete_button)
        
        self.tool_menu.draw()
        self.tool_menu.hide()
        #################################################################################################################################################################
        # Events
        ## App
        self.bind("<KeyPress>", self.handler.press)
        ## Canvas
        self.canvas.bind("<Motion>", self.handler.move_with_mouse)
        self.canvas.bind("<Button-1>", self.handler.click_canvas)
        self.canvas.bind("<ButtonRelease-1>", self.handler.unclick_canvas)
        self.canvas.bind("<Button-3>", self.handler.left_click_canvas)
        ## Menu
        ### Switch mode button
        self.switch_mode_button.bind("<Button-1>", self.handler.switch_mode)
        ### Create button
        self.create_button.bind("<Button-1>", self.handler.press_create_button)
        ### Delete button
        self.delete_button.bind("<Button-1>", self.handler.press_delete_button)
        #######################################################################################
        self.draw_loop.start()
        
    def draw_universe(self):
        self.controller.draw_universe()
        if self.mode == "view":
            self.universe.move(c.DELTA_T)
            self.universe.update_velocity(c.DELTA_T, c.G)
            print(self.universe.planets)
        if self.mode == "choosing position":
            self.controller.erase_planet(self.new_planet)
            self.controller.draw_planet(self.new_planet)

    def activate(self):
        self.status = "active"

    def desactivate(self):
        self.status = "disable"

if __name__ == "__main__":
    app = App()
    app.mainloop()