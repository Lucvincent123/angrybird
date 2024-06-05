# import constants as c
from .Button import Button

class SwitchModeButton(Button):
    slots = ["lines", "eye", "mode"]

    def __init__(self, canvas, R, thickness, background_color, foreground_color):
        super().__init__(canvas, R, thickness, background_color, foreground_color)
        self.lines = []
        self.eyes = []
        self.mode = "view"

    def draw(self, position):
        """Draw the background of the button 

        Args:
            position (_ArrayLike_): the position of the center of the button
        """     
        super().draw(position)
        x, y = position
        d = (self.R + self.thickness / 2) * 0.3
        R = self.R
        # Draw  the 3 lines 
        for i in range(3):
            self.lines.append(self.canvas.create_line(x - R * 0.5, 
                                                      y + (i - 1) * d, 
                                                      x + R * 0.5,
                                                      y + (i - 1) * d, 
                                                      fill=self.foreground_color, 
                                                      width=self.thickness, 
                                                      state="hidden"))
        #################################################################################
        # Draw the eye
        ## Draw the big oval
        self.eyes.append(self.canvas.create_oval(x - R * 0.5,
                                                y - d,
                                                x + R * 0.5,
                                                y + d,
                                                fill=self.foreground_color))
        ## Draw the small oval
        self.eyes.append(self.canvas.create_oval(x - R * 0.3,
                                           y - R * 0.3,
                                           x + R * 0.3,
                                           y + R * 0.3,
                                           fill=self.background_color))
    
    def bind(self, event, callback):
        """Bind a event listener to the button foreground

        Args:
            event (_obj_ Event): the event
            callback (_function_): the callback function
        """       
        super().bind(event, callback)
        for item in self.eyes:
            self.canvas.tag_bind(item, event, callback)
        for item in self.lines:
            self.canvas.tag_bind(item, event, callback)

    def switch_to_view_mode(self):
        """show the eye and hide the 3 lines
        """        
        for item in self.eyes:
            self.canvas.itemconfig(item, state="normal")
        for item in self.lines:
            self.canvas.itemconfig(item, state="hidden")

    def switch_to_config_mode(self):
        """show the 3 lines and hide the eye
        """        
        for item in self.eyes:
            self.canvas.itemconfig(item, state="hidden")
        for item in self.lines:
            self.canvas.itemconfig(item, state="normal")
