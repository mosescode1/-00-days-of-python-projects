import math


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius must be positive')
        
        if value != self._radius:
            self._radius = value
            self._area = None
    
    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self._radius ** 2
        return self._area

c = Circle(10)
print(c.area())