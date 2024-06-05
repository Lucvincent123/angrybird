from .Vector import Vector

class Planet:
    slots = ["name", "mass", "radius", "color", "position", "image", "velocity"]

    def __init__(self, name, mass, radius, color, position, velocity = Vector(0, 0)):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.color = color
        self.position = position
        self.image = None
        self.velocity = velocity

    def move(self, delta_t):
        """Update the planet position after a duration of time moving with its velocity

        Args:
            delta_t (_float_): the duration of time (in seconds) in which the planet has moved
        """        
        self.position += delta_t * self.velocity 

    def update_velocity(self, new_velocity):
        """Update the velocity of the planet

        Args:
            new_velocity (_obj_ Vector): the new velocity
        """        
        self.velocity = new_velocity

    def update_velocity_with_acceleration(self, acceleration, delta_t):
        """Update the velocity after a duration of time moving with the acceleration

        Args:
            acceleration (_obj_ Vector): the acceleration (in m.s^-2)
            delta_t (_obj_ Vector): the duration of time (in seconds) in which the planet has moved
        """        
        self.velocity += delta_t * acceleration

    def translate(self, vector):
        """Update the planet position after translating it by a vector 

        Args:
            vector (_obj_ Vector): the translation vector
        """        
        self.position += vector

    def acceleration_on(self, planet, G):
        """Calculate the acceleration that this planet create upon another planet

        Args:
            planet (_obj_ Planet): the planet suffers
            G (_float_): the gravitational constant

        Returns:
            _obj_ Vector: the acceleration vector
        """        
        vector_distance = self.position - planet.position 
        distance = abs(vector_distance)
        acceleration = G * self.mass / (distance**3) /1000000000000000* vector_distance 
        return acceleration
    
    def is_hovered(self, mouse_position):
        """Check if the planet is hovered

        Args:
            mouse_position (_obj_ Vector): the mouse position vector

        Returns:
            _bool_: True if the planet is hovered and False otherwise
        """        
        distance = abs(self.position - mouse_position)
        if distance <= self.radius:
            return True
        else:
            return False
        
    def update_position(self, vector):
        """Update the planet position without changing the pointer of the position attribute

        Args:
            vector (_obj_ Vector): the new position vector
        """        
        self.position = vector

    def copy(self):
        """Make a copy of the planet in order to not change the origin planet

        Returns:
            _obj_ Planet: the copy of the planet not its pointer
        """        
        return Planet(self.name, self.mass, self.radius, self.color, self.position, self.velocity)