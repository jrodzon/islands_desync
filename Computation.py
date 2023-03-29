import random
from time import sleep

import ray

from Emigration import Emigration
from Immigrant import Immigrant


@ray.remote
class Computation:

    def __init__(self, island, n: int, islands, select_algorithm):
        self.island = island
        self.n: int = n
        self.emigration = Emigration.remote(islands, select_algorithm)
        self.population = [Immigrant(0, n,'Obj 1 z wyspy %s' % n), Immigrant(0, n, 'Obj 2 z wyspy %s' % n), Immigrant(0, n, 'Obj 3 z wyspy %s' % n)]

    def start(self):
        while True:
            self.iteration()

    def iteration(self):
        immigrants: Immigrant = ray.get(self.island.get_immigrants.remote())

        if len(immigrants) > 0:
            print('Wyspa %s: dostaje %s' % (self.n, immigrants))

        self.population += immigrants

        print('Wyspa %s: wszyscy osobnicy: %s' % (self.n, self.population))

        sleep(2.0)  # computation

        for member in self.population:
            member.increment_iteration()

        if len(self.population) > 0:
            target_num = random.randint(0, len(self.population) - 1)
            print('Wyspa %s: Emigruje %s' % (self.n, str(self.population[target_num])))
            self.emigration.emigrate.remote(self.population.pop(target_num))
