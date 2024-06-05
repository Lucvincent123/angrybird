class Menu:
    slots = ["direction", "position", "distance", "buttons", "positions_buttons"]

    def __init__(self, direction, position, distance):
        self.direction = direction
        self.position = position
        self.distance = distance
        self.buttons = []
        self.positions_buttons = []

    def add_button(self, button):
        """Add a button to the menu

        Args:
            button (_obj_ Button): the button to add
        """        
        # Calculate the position for that button
        i = len(self.buttons)
        if i < 1:
            self.positions_buttons.append(self.position)
        else:
            prev_button = self.buttons[-1]
            prev_button_position = self.positions_buttons[-1]
            if self.direction == "horizontal":
                self.positions_buttons.append((prev_button_position[0] + 
                                               prev_button.R + button.R + 
                                               (prev_button.thickness + button.thickness) / 2 + 
                                               self.distance, 

                                               prev_button_position[1]))
            elif self.direction == "vertical":
                self.positions_buttons.append((prev_button_position[0], 
                                               
                                               prev_button_position[1] + 
                                               prev_button.R + button.R + 
                                               (prev_button.thickness + button.thickness) / 2 + 
                                               self.distance))
        #########################################################################################
        self.buttons.append(button)

    def draw(self):
        """Draw the menu on the canvas
        """        
        for i in range(len(self.buttons)):
            self.buttons[i].draw(self.positions_buttons[i])

    def hide(self):
        """Hide the menu
        """        
        for button in self.buttons:
            button.hide()

    def show(self):
        """Show the menu
        """        
        for button in self.buttons:
            button.show()

    def activate(self):
        for button in self.buttons:
            button.activate()

    def desactivate(self):
        for button in self.buttons:
            button.desactivate()