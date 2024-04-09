class Planet:
    def __init__(self, mass, radius, color, x, y):
        self.mass = mass
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.image = None
        self.velocity = (0, 0)

    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def update_velocity(self, new_velocity):
        self.velocity = new_velocity

    def draw(self, window):
        window.delete(self.image)
        x = self.x
        y = self.y
        radius = self.radius
        color = self.color
        self.image = window.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, width=0)