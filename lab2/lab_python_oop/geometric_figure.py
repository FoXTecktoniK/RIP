from abc import *
class geometric_figure(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        pass