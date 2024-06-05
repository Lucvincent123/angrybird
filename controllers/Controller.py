class Controller:
    slots = ["app"]

    def __init__(self, app) -> None:
        self.app = app

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
            planet (_obj_ Planet): The planet needs to be drawn
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


    