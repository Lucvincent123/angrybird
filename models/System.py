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