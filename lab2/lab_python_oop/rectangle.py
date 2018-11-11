from .geometric_figure import *
from .colour_figure import *
class rectangle(geometric_figure):
    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour_figure(colour)
    def area(self):
        return (self.width * self.height)
    def name(self):
        return('Прямоугольник');
    def __repr__(self):
        return '{} цвета {}, шириной {}, высотой {} и площадью {}'.format(self.name(), self.colour.colour, self.width, self.height, self.area())