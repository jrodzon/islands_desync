import asyncio

import ray
from Computation import Computation
from selectAlgorithm import SelectAlgorithm

from islands_desync.geneticAlgorithm.run_hpc.run_algorithm_params import (
    RunAlgorithmParams,
)


@ray.remote
class Island:
    def __init__(self, island_id: int, select_algorithm: SelectAlgorithm):
        self.island_id: int = island_id
        self.computation = None
        self.islands: [Island] = []
        self.immigrants = []
        self.select_algorithm: SelectAlgorithm = select_algorithm

    async def start(
        self, island_handle, islands: ["Island"], algorithm_params: RunAlgorithmParams
    ):
        self.islands = islands
        self.computation = Computation.remote(
            island_handle,
            self.island_id,
            islands,
            self.select_algorithm,
            algorithm_params,
        )
        self.computation.start.remote()

        # zacznij oddawac procesor dla sqoich innych metod
        while True:
            await asyncio.sleep(0)

    async def receive_immigrant(self, immigrant):
        print("Wyspa %s: dostaje imigranta: %s" % (self.island_id, str(immigrant)[:10]))
        self.immigrants.append(immigrant)

    async def get_immigrants(self):
        return [self.immigrants.pop(0) for _ in self.immigrants]

    def __repr__(self):
        return "Island %s" % self.island_id
