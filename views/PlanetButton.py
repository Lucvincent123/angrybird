from .Button import Button
class PlanetButton(Button):
    slots = ["planet", "planet_image"]

    def __init__(self, canvas, R, thickness, background_color, foreground_color, planet):
        super().__init__(canvas, R, thickness, background_color, foreground_color)
        self.planet = planet
        self.planet_image = None

    def draw(self, position):
        """Draw the background of the button 

        Args:
            position (_ArrayLike_): the position of the center of the button
        """     """

        Args:
            position (_type_): _description_
        """        
        super().draw(position)
        # self.planet_image = self.canvas.create_oval()

    