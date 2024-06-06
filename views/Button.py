class Button:
    slots = ["canvas", "R", "thickness", "background_color", "foreground_color", "background", "status"]

    def __init__(self, canvas, R, thickness, background_color, foreground_color):
        self.canvas = canvas
        self.R = R
        self.thickness = thickness
        self.background_color = background_color
        self.foreground_color = foreground_color
        self.background = None
        self.status = "active"

    def draw(self, position):
        """Draw the background of the button 

        Args:
            position (_ArrayLike_): the position of the center of the button
        """        
        x, y = position
        thickness = self.thickness
        R = self.R
        background_color = self.background_color
        foreground_color = self.foreground_color
        self.background = self.canvas.create_oval(x - R, 
                                                  y - R, 
                                                  x + R, 
                                                  y + R, 
                                                  outline=foreground_color, 
                                                  width=thickness, 
                                                  fill=background_color)
          
    def hide(self):
        """Hide the button
        """        
        self.canvas.itemconfig(self.background, state="hidden")

    def show(self):
        """Show the button
        """        
        self.canvas.itemconfig(self.background, state="normal")
        
    def bind(self, event, callback):
        """Bind a event listener to the button

        Args:
            event (_obj_ Event): the event
            callback (_function_): the callback function
        """        
        self.canvas.tag_bind(self.background, event, callback)

    def activate(self):
        """Activate the button
        """        
        self.status = "active"

    def desactivate(self):
        """Desactivate the button
        """        
        self.status = "disable"

        
    