from .geometric_figure import *
from .colour_figure import *
from .rectangle import *
class square(rectangle):
    def __init__(self, height, colour):
        self.side = height
        self.colour = colour_figure(colour)
    def area(self):
        return (self.side * self.side)
    def name(self):
        return('Квадрат');
    def __repr__(self):
        return '{} цвета {}, со стороной {} и площадью {}'.format(self.name(), self.colour.colour, self.side, self.area())