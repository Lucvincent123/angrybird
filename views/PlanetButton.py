from .Button import Button
class PlanetButton(Button):
    slots = ["planet", "planet_image", "name_image"]

    def __init__(self, canvas, R, thickness, background_color, foreground_color, planet):
        super().__init__(canvas, R, thickness, background_color, foreground_color)
        self.planet = planet
        self.planet_image = None
        self.name_image = None

    def draw(self, position):
        """Draw the button 

        Args:
            position (_ArrayLike_): the position of the center of the button
        """     """

        Args:
            position (_type_): _description_
        """        
        super().draw(position)
        x, y = position
        R = self.R * 0.6
        self.planet_image = self.canvas.create_oval(x - R, y - R, x + R, y + R, fill=self.planet.color)
        self.name_image = self.canvas.create_text(x, y + R + 2, text=self.planet.name, fill=self.foreground_color, anchor="center")

    def clear(self):
        """Clear the button
        """        
        self.canvas.delete(self.background)
        self.canvas.delete(self.planet_image)
        self.canvas.delete(self.name_image)

    def bind(self, event, callback):
        """Bind a event listener to the button

        Args:
            event (_obj_ Event): the event
            callback (_function_): the callback function
        """     
        super().bind(event, callback)
        self.canvas.tag_bind(self.planet_image, event, callback)
        self.canvas.tag_bind(self.name_image, event, callback)

    