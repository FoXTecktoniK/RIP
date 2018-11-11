import math
from .geometric_figure import *
from .colour_figure import *
class circle(geometric_figure):
    def __init__(self, R, colour):
        self.radius = R
        self.colour = colour_figure(colour)
    def area(self):
        return (self.radius * self.radius * math.pi) 
    def name(self):
        return('Круг');
    def __repr__(self):
        return '{} цвета {}, радиуса {} и площадью {}'.format(self.name(), self.colour.colour, self.radius, self.area())