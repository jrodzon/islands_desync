from time import sleep

class Computation:

    def __init__(self, island, n: int):
        self.island = island
        self.n: int = n
        self.start()

    def start(self):
        while True:
            self.iteration()

    def iteration(self):
        sleep(4.0)
        self.island.communicate('From computation %s' % self.n)
