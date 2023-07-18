import math

class Vector2d:
    def __init__(self, x, y):
        """VECTOR MATCHES Y, X FORMAT"""
        self.x = x
        self.y = y
        self.distance = math.sqrt(x**2 + y**2)
        self.is_zero = y == 0 and x == 0
        if not self.is_zero:
            self.angle = math.acos(x/self.distance) / math.pi * 180
        else:
            self.angle = None
        self.is_1d = not (self.y != 0 and self.x != 0)
    
    def __getitem__(self, index):
        if index == 1:
            return self.x
        elif index == 0:
            return self.y
        else:
            raise IndexError

    def __eq__(self, value):
        if type(value) == Vector2d:
            return self.x == value.x and self.y == value.y
        elif type(value) in {tuple, list}:
            if len(value) == 2:
                return self.x == value[0] and self.y == value[1]
            else:
                return False
        else:
            return False

    def __ne__(self, value):
        return not self.__eq__(self, value)

    def __add__(self, value):
        if type(value) == Vector2d:
            return Vector2d(self.y + value.y, self.x + value.x)
        elif type(value) in {int, float}:
            return Vector2d(self.y + value, self.x + value)
        elif type(value) in {tuple, list}:
            return Vector2d(self.x + value[0], self.y + value[1])
        else:
            raise TypeError(f"Can't add {type(value)} and Vector2d together")

    def __mul__(self, value):    
        if type(value) in {int, float}:
            return Vector2d(self.x * value, self.y * value)
        else:
            raise TypeError(f"Can't multiply {type(value)} and Vector2d together")
        
    def __truediv__(self, value):
        if type(value) in {int, float}:
            return Vector2d(self.x / value, self.y / value)
        else:
            raise TypeError(f"Can't divide Vector2d by {type(value)}")