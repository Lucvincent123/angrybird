from .constants import KEY_TRANSLATE_SPEED, RADIUS_BUTTON, THICKNESS_OUTLINE_BUTTON, BACKGROUND_COLOR_BUTTON, FOREGROUND_COLOR_BUTTON, FILE_PATH

class EventHandler:
    slots = ["app", "Vector", "InputCreate", "Planet", "PlanetButton"]

    def __init__(self, app, vector_model, input_create_model, planet_model, planet_button_model) -> None:
        ## main
        self.app = app
        #######################################################################################################
        ## Some useful model from main
        self.Vector = vector_model
        self.InputCreate = input_create_model
        self.Planet = planet_model
        self.PlanetButton = planet_button_model

    def press(self, event):
        ## Move the screen by pressing Up, Down, Left, Right key
        if self.app.status == "active":
            if event.keysym == "Right":
                self.app.universe.translate(KEY_TRANSLATE_SPEED * self.Vector(1, 0))
            elif event.keysym == "Left":
                self.app.universe.translate(KEY_TRANSLATE_SPEED * self.Vector(-1, 0))
            elif event.keysym == "Up":
                self.app.universe.translate(KEY_TRANSLATE_SPEED * self.Vector(0, -1))
            elif event.keysym == "Down":
                self.app.universe.translate(KEY_TRANSLATE_SPEED * self.Vector(0, 1))

    def click_background(self, event):
        ## Click on the planet menu
        if self.app.status == "active":
            button_hovered = self.app.controller.planet_button_hovered(event.x, event.y)
            if button_hovered >= 0:
                planet = self.app.universe.planets[button_hovered]
                canvas = self.app.canvas
                center = self.Vector(canvas.width / 2, canvas.height / 2)
                translation_vector = center - planet.position
                self.app.universe.translate(translation_vector)

    def move_with_mouse(self, event):
        ## Moving mouse on the universe screen
        if self.app.status == "active":
            if self.app.canvas.is_clicked:
                ## Move the universe screen
                previous_mouse_position = self.app.mouse_position
                current_mouse_position = self.Vector(event.x, event.y)
                translation_vector = current_mouse_position - previous_mouse_position
                self.app.universe.translate(translation_vector)
            self.app.mouse_position.update(self.Vector(event.x, event.y))

            if self.app.mode == "choosing direction":
                ## Showing the direction of the velocity of the new planet
                if self.app.arrow_image:
                    self.app.canvas.delete(self.app.arrow_image)
                tail = self.app.new_planet.position
                self.app.arrow = self.app.mouse_position - tail
                head = tail + 100 / abs(self.app.arrow) * self.app.arrow 
                self.app.arrow_image = self.app.canvas.create_line(tail.x, tail.y, head.x, head.y, arrow="last", fill="white")
    
    def click_canvas(self, event):
        ## Click on the universe screen
        if self.app.status == "active":
            self.app.canvas.is_clicked = True
            if self.app.mode == "delete":
                ## Mode delete
                planet_clicked = self.app.controller.planet_hovered()
                if planet_clicked >= 0:
                    button_removed = self.app.planet_menu.remove_button(planet_clicked)
                    button_removed.clear()
                    self.app.planet_menu.update()
                    planet_deleted = self.app.universe.delete_planet(planet_clicked)
                    self.app.controller.erase_planet(planet_deleted)

    def unclick_canvas(self, event):
        ## Unclick on the universe screen
        if self.app.status == "active":
            self.app.canvas.is_clicked = False  

    def left_click_canvas(self, event):
        ## Left click on the universe screen
        if self.app.status == "active":
            if self.app.mode == "choosing position":
                ## Choosing the position of the new planet
                self.app.new_planet.update_position(self.Vector(event.x, event.y))
                self.app.mode = "choosing direction"
            elif self.app.mode == "choosing direction" and self.app.arrow:
                ## Choosing the direction of the velocity of the new planet
                self.app.new_planet.update_velocity(self.app.arrow.transform_to_module(self.app.new_planet_velocity))
                if self.app.arrow_image:
                    self.app.canvas.delete(self.app.arrow_image)
                new_planet_copy = self.app.new_planet.copy()
                self.app.universe.add_planet(new_planet_copy)
                self.app.planet_menu.add_button(self.PlanetButton(self.app.background,
                                                                  RADIUS_BUTTON,
                                                                  THICKNESS_OUTLINE_BUTTON,
                                                                  BACKGROUND_COLOR_BUTTON,
                                                                  FOREGROUND_COLOR_BUTTON,
                                                                  new_planet_copy))
                self.app.planet_menu.update()
                self.app.controller.erase_planet(self.app.new_planet)
                self.new_planet = None
                self.new_planet_velocity = 0
                self.arrow = None
                self.arrow_image = None
                self.app.mode = "config"
                self.app.switch_mode_button.activate()
                self.app.tool_menu.activate()
    
    def switch_mode(self, event):
        ## Press switch mode button
        if self.app.switch_mode_button.status == "active":
            if self.app.mode == "view":
                self.app.switch_mode_button.switch_to_config_mode()
                self.app.mode = "config"
                self.app.tool_menu.show()
            elif self.app.mode in ("config", "delete"):
                self.app.switch_mode_button.switch_to_view_mode()
                self.app.mode = "view"
                self.app.tool_menu.hide()

    def press_create_button(self, event):
        ## Press create button
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

    def press_delete_button(self, event):
        ## Press delete button
        if self.app.delete_button.status == "active":
            self.app.mode = "delete"

    def press_save_button(self, event):
        ## press save button
        if self.app.save_button.status == "active":
            self.app.controller.save(FILE_PATH)

    

