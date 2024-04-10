from .Vector import Vector

class Planet:
    def __init__(self, mass, radius, color, position, velocity=Vector(0, 0)):
        self.mass = mass
        self.radius = radius
        self.color = color
        self.position = position
        self.image = None
        self.velocity = velocity

    def move(self):
        self.position += self.velocity

    def update_velocity(self, new_velocity):
        self.velocity = new_velocity

    def update_velocity_with_acceleration(self, acceleration):
        self.velocity += acceleration

    def draw(self, window):
        window.delete(self.image)
        x, y = self.position()
        radius = self.radius
        color = self.color
        self.image = window.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, width=0)