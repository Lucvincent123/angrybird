from .Button import Button

class NormalButton(Button):
    slots = ["text", "text_image"]

    def __init__(self, canvas, R, thickness, background_color, foreground_color, text):
        super().__init__(canvas, R, thickness, background_color, foreground_color)
        self.text = text
        self.text_image = None

    def draw(self, position):
        """Draw the background of the button 

        Args:
            position (_ArrayLike_): the position of the center of the button
        """        
        super().draw(position)
        x, y = position
        self.text_image = self.canvas.create_text(x, y, text=self.text, anchor="center", fill=self.foreground_color)

    def bind(self, event, callback):
        """Bind a event listener to the button foreground

        Args:
            event (_obj_ Event): the event
            callback (_function_): the callback function
        """       
        super().bind(event, callback)
        self.canvas.tag_bind(self.text_image, event, callback)

    def hide(self):
        """Hide the button
        """        
        super().hide()
        self.canvas.itemconfig(self.text_image, state="hidden")

    def show(self):
        """Show the button
        """        
        super().show()
        self.canvas.itemconfig(self.text_image, state="normal")
    