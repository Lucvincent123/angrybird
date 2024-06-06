import json

from .constants import RADIUS_BUTTON, THICKNESS_OUTLINE_BUTTON, BACKGROUND_COLOR_BUTTON, FOREGROUND_COLOR_BUTTON

class Controller:
    slots = ["app", "PlanetButton", "Planet", "Vector"]

    def __init__(self, app, planet_button_model, planet_model, vector_model) -> None:
        ## main
        self.app = app
        ##############################################################################
        ## Some useful models from main
        self.PlanetButton = planet_button_model
        self.Planet = planet_model
        self.Vector = vector_model

    def draw_planet(self, planet):
        """Draw a planet on the canvas

        Args:
            planet (_obj_ Planet): The planet needs to be drawn
        """        
        x, y = planet.position()
        radius = planet.radius
        color = planet.color
        planet.image = self.app.canvas.create_oval(x - radius, 
                                                   y - radius, 
                                                   x + radius, 
                                                   y + radius, 
                                                   fill=color, width=0)

    def erase_planet(self, planet):
        """Erase a planet on the canvas

        Args:
            planet (_obj_ Planet): The planet needs to be erased
        """        
        if planet.image:
            self.app.canvas.delete(planet.image)

    def draw_universe(self):
        """Draw the universe (all the planets) on the canvas
        """                  
        for planet in self.app.universe.planets:
            self.erase_planet(planet)
            self.draw_planet(planet)

    def planet_hovered(self):
        """Get the hovered planet  

        Returns:
            _int_: -1 if there is no planet hovered otherwise the index of the hovered planet in the planet list
        """
        nb_planets = len(self.app.universe.planets)
        found = False
        i = 0
        while i < nb_planets and not found:
            found = found or self.app.universe.planets[i].is_hovered(self.app.mouse_position)
            i += 1
        if found:
            return i - 1
        else: 
            return -1
        
    def reset_planet_menu(self):
        """Reset the planet menu
        """        
        self.app.planet_menu.empty()
        for planet in self.app.universe.planets:
            self.app.planet_menu.add_button(self.PlanetButton(self.app.background, 
                                              RADIUS_BUTTON, 
                                              THICKNESS_OUTLINE_BUTTON,
                                              BACKGROUND_COLOR_BUTTON, 
                                              FOREGROUND_COLOR_BUTTON, 
                                              planet))
        self.app.planet_menu.update()
        
    def save(self, path):
        """Save the progress

        Args:
            path (_str_): the file path
        """          
        data = {
            "title" : "Gravitational simulation",
            "path" : "/",
            "planets" : [],
        }

        for planet in self.app.universe.planets:
            data["planets"].append(planet.to_dict())

        json_object = json.dumps(data, indent=4)

        with open(path, "w") as outfile:
            outfile.write(json_object)

    def load(self, path):
        """Load the progress

        Args:
            path (_str_): the file path
        """     
        try:
            with open(path, mode="r") as infile:
                data = json.load(infile)
                for planet in data["planets"]:
                    self.app.universe.add_planet(self.Planet(planet["name"],
                                                            planet["mass"],
                                                            planet["radius"],
                                                            planet["color"],
                                                            self.Vector(planet["x"], planet["y"]),
                                                            self.Vector(planet["vx"], planet["vy"])))
                    
                self.reset_planet_menu()
        except:
            pass

    def planet_button_hovered(self, mouse_x, mouse_y):
        """Get the hovered planet button

        Returns:
            _int_: -1 if there is no button hovered otherwise the index of the hovered button in the planet button list
        """
        nb_buttons = len(self.app.planet_menu.buttons)
        found = False
        i = 0
        while i < nb_buttons and not found:
            x, y = self.app.planet_menu.positions_buttons[i]
            distance_square = (mouse_x - x) ** 2 + (mouse_y - y) ** 2
            is_hovered = distance_square <= RADIUS_BUTTON ** 2
            found = found or is_hovered
            i += 1
        if found:
            return i - 1
        else: 
            return -1

    

    



    