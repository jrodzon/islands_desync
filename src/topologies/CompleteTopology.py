from typing import Dict, List

from src.topologies import Topology


class CompleteTopology(Topology):
    def __init__(self, size):
        super().__init__(size)

    def create(self) -> Dict[int, List]:

        res = {i: self.connected_to_i(i) for i in range(self.size)}
        return res

    def connected_to_i(self, i):
        return list(filter(lambda num: num != i, range(self.size)))