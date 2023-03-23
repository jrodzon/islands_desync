import random

from selectAlgorithm.SelectAlgorithm import SelectAlgorithm


class RandomSelect(SelectAlgorithm):
    def __init__(self):
        super().__init__()

    def choose(self, items):
        return random.choice(items)
