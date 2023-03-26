import random
import time
from time import sleep

import ray

from Emigration import Emigration


@ray.remote
class Computation:

    def __init__(self, island, n: int, islands, select_algorithm):
        self.island = island
        self.n: int = n
        self.emigration = Emigration.remote(islands, select_algorithm)
        self.population = ['Obj 1 z wyspy %s' % n, 'Obj 2 z wyspy %s' % n, 'Obj 3 z wyspy %s' % n]

    def start(self):
        while True:
            self.iteration()

    def iteration(self):
        immigrants: [str] = ray.get(self.island.get_immigrants.remote())

        if (len(immigrants) > 0):
            print('Wyspa %s dostaje %s' % (self.n, immigrants))

        self.population.append(immigrants)

        sleep(4.0)  # computation

        target_num = random.randint(0, 2)
        print('Wyspa %s Emigruje %s' % (self.n, self.population[target_num]))
        self.emigration.emigrate.remote(self.population[target_num])
