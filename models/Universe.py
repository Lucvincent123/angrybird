from .Vector import Vector

class Universe:
    slots = ["planets"]

    def __init__(self):
        self.planets = []
    
    def add_planet(self, planet):
        """Add a planet to the universe

        Args:
            planet (_obj_): the planet to add
        """        
        self.planets.append(planet)

    def move(self, delta_t):
        """Update the position of the universe (all planets) after a duration of time

        Args:
            delta_t (_float_): the duration of time (in seconds) in which the planets has moved
        """        
        for planet in self.planets:
            planet.move(delta_t)

    def update_velocity(self, delta_t, G):
        """Update the velocity of all planets in the universe after a duration of time with the gravitational effet between them

        Args:
            delta_t (_float_): the duration of time (in seconds) in which the planets has moved
            G (_float_): the gravitational constant
        """        
        nb_planets = len(self.planets)
        for i in range(nb_planets):
            acceleration = Vector(0, 0)
            for j in range(nb_planets):
                if j != i:
                    acceleration += self.planets[j].acceleration_on(self.planets[i], G)
            
            self.planets[i].update_velocity_with_acceleration(acceleration, delta_t)

    def translate(self, vector):
        """Update the whole universe position after translating it by a vector

        Args:
            vector (_obj_ Vector): the translation vector
        """        
        for planet in self.planets:
            planet.translate(vector)

    def delete_planet(self, index):
        """Delete the planet from the list by its index

        Args:
            index (_int_): the index of the planet 

        Returns:
            _obj_ Planet: the deleted planet
        """        
        return self.planets.pop(index)
        


