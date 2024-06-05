from .constants import KEY_TRANSLATE_SPEED

class EventHandler:
    slots = ["app"]

    def __init__(self, app, vector_model, input_create_model, planet_model) -> None:
        self.app = app
        self.Vector = vector_model
        self.InputCreate = input_create_model
        self.Planet = planet_model

    def press(self, event):
        if self.app.status == "active":
            if event.keysym == "Right":
                self.app.universe.translate(KEY_TRANSLATE_SPEED * self.Vector(1, 0))
            elif event.keysym == "Left":
                self.app.universe.translate(KEY_TRANSLATE_SPEED * self.Vector(-1, 0))
            elif event.keysym == "Up":
                self.app.universe.translate(KEY_TRANSLATE_SPEED * self.Vector(0, -1))
            elif event.keysym == "Down":
                self.app.universe.translate(KEY_TRANSLATE_SPEED * self.Vector(0, 1))

    def move_with_mouse(self, event):
        if self.app.status == "active":
            print("move")
            print(self.app.mode)
            if self.app.canvas.is_clicked:
                previous_mouse_position = self.app.mouse_position
                current_mouse_position = self.Vector(event.x, event.y)
                translation_vector = current_mouse_position - previous_mouse_position
                print(translation_vector)
                self.app.universe.translate(translation_vector)
                
            self.app.mouse_position.update(self.Vector(event.x, event.y))


            if self.app.mode == "choosing direction":
                print("arrow")
                if self.app.arrow_image:
                    self.app.canvas.delete(self.app.arrow_image)
                tail = self.app.new_planet.position
                self.app.arrow = self.app.mouse_position - tail
                head = tail + 100 / abs(self.app.arrow) * self.app.arrow 
                self.app.arrow_image = self.app.canvas.create_line(tail.x, tail.y, head.x, head.y, arrow="last", fill="white")
    
    def click_canvas(self, event):
        if self.app.status == "active":
            self.app.canvas.is_clicked = True
            if self.app.mode == "delete":
                planet_clicked = self.app.controller.planet_hovered()
                if planet_clicked >= 0:
                    planet_deleted = self.app.universe.delete_planet(planet_clicked)
                    self.app.controller.erase_planet(planet_deleted)

    def unclick_canvas(self, event):
        if self.app.status == "active":
            self.app.canvas.is_clicked = False  

    def left_click_canvas(self, event):
        print("left click")
        print(self.app.mode)
        if self.app.status == "active":
            if self.app.mode == "choosing position":
                self.app.new_planet.update_position(self.Vector(event.x, event.y))
                self.app.mode = "choosing direction"
                print("choosing direction")
            elif self.app.mode == "choosing direction" and self.app.arrow:
                # self.app.arrow.transform_to_module(self.app.new_planet_velocity)
                # print(self.app.new_planet_velocity)
                # print()
                self.app.new_planet.update_velocity(self.app.arrow.transform_to_module(self.app.new_planet_velocity))
                if self.app.arrow_image:
                    self.app.canvas.delete(self.app.arrow_image)
                self.app.universe.add_planet(self.app.new_planet.copy())
                self.app.controller.erase_planet(self.app.new_planet)
                self.new_planet = None
                self.new_planet_velocity = 0
                self.arrow = None
                self.arrow_image = None
                self.app.mode = "config"
                self.app.switch_mode_button.activate()
                self.app.tool_menu.activate()
    
    def switch_mode(self, event):
        if self.app.switch_mode_button.status == "active":
            if self.app.mode == "view":
                self.app.switch_mode_button.switch_to_config_mode()
                self.app.mode = "config"
                self.app.tool_menu.show()
            elif self.app.mode in ("config", "delete"):
                self.app.switch_mode_button.switch_to_view_mode()
                self.app.mode = "view"
                self.app.tool_menu.hide()
            print("switch")

    def press_create_button(self, event):
        if self.app.status == "active":
            self.app.status = "loading"
            self.app.mode = "create"
            self.app.switch_mode_button.desactivate()
            self.app.tool_menu.desactivate()
            input_create = self.InputCreate(self.app)
            new_planet = input_create.planet
            self.app.status = "active"
            if new_planet != None:
                self.app.mode = "choosing position"
                self.app.new_planet = self.Planet(new_planet["name"],
                                                  new_planet["mass"],
                                                  new_planet["radius"],
                                                  new_planet["color"],
                                                  self.app.mouse_position)
                self.app.new_planet_velocity = new_planet["velocity"]
            else:
                self.app.mode = "config"
                print("out")

    def press_delete_button(self, event):
        if self.app.delete_button.status == "active":
            self.app.mode = "delete"
            print("delete")
