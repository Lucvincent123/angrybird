from .Vector import Vector

class System:
    def __init__(self):
        self.planets = []
    
    def add_planet(self, planet):
        self.planets.append(planet)

    def draw(self, window):
        for planet in self.planets:
            planet.draw(window)

    def move(self):
        for planet in self.planets:
            planet.move()

    def update_velocity(self):
        nb_planets = len(self.planets)
        for i in range(nb_planets):
            acceleration = Vector(0, 0)
            # A completer
            
            self.planets[i].update_velocity_with_acceleration(acceleration)


