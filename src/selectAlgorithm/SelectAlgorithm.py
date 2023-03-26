from abc import ABC
from abc import abstractmethod


class SelectAlgorithm(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def choose(self, items):
        pass
