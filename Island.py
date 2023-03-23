import ray

from Computation import Computation
from select import SelectAlgorithm


@ray.remote(num_cpus=1)
class Island:
    def __init__(self, island_id: int, select_algorithm: SelectAlgorithm):
        self.island_id: int = island_id
        self.computation = None
        self.islands: [Island] = []
        self.select_algorithm: SelectAlgorithm = select_algorithm

    def start(self, islands: ['Island']):
        self.computation = Computation(self, self.island_id)
        self.islands = islands

    def communicate(self, msg):
        destination: Island = self.select_algorithm.choose(self.islands)
        destination.receive_msg(msg)

    def receive_msg(self, msg):
        print('Island %s received: %s' % self.island_id, msg)

    def __repr__(self):
        return "Island %s" % self.id
