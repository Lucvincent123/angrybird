from math import sqrt
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+ str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)
    
    def __iadd__(self, vector):
        self.x += vector.x
        self.y += vector.y
        return self
    
    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)
    
    def __isub__(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        return self
    
    def __call__(self):
        return (self.x, self.y)
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
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