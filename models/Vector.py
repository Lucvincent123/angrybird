from math import sqrt
class Vector:
    slots = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+ str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, vector):
        # v1 + v2
        return Vector(self.x + vector.x, self.y + vector.y)
    
    def __iadd__(self, vector):
        # v1 += v2
        self.x += vector.x
        self.y += vector.y
        return self
    
    def __sub__(self, vector):
        # v1 - v2
        return Vector(self.x - vector.x, self.y - vector.y)
    
    def __isub__(self, vector):
        # v1 -= v2
        self.x -= vector.x
        self.y -= vector.y
        return self
    
    def __call__(self):
        # v1()
        return (self.x, self.y)
    
    def __abs__(self):
        # abs(v1) the module of vector v1
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __rmul__(self, alpha):
        # alpha * v1
        return Vector(self.x * alpha, self.y * alpha)
    
    def update(self, vector):
        """Update the vector without changing its pointer

        Args:
            vector (_obj_ Vector): the vector used to update
        """        
        self.x = vector.x
        self.y = vector.y

    def transform_to_module(self, module):
        """Transform the vector to a vector with the same direction to the given module

        Args:
            module (_type_): _description_
        """        
        current_module = self.__abs__()
        return Vector(module / current_module * self.x, module / current_module * self.y)

    def copy(self):
        """Create a copy

        Returns:
            _obj_ Vector: the copy
        """        
        return Vector(self.x, self.y)

### Just to test    
if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(-1, 2)
    v3 = v1 - v2
    v1 -= v2
    print(v3)
    print(v1)
    x, y = v1()
    print(abs(v1))
    print(y)