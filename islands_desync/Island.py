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

    async def receive_immigrant(self, immigrant_iteration):
        print("Wyspa %s: dostaje imigranta: %s" % (self.island_id, str(immigrant_iteration)[:10]))
        # immigrant, iteration_number = immigrant_iteration
        self.immigrants.append(immigrant_iteration)

    async def get_immigrants(self):
        return [self.immigrants.pop(0) for _ in self.immigrants]

    async def finish(self):
        ray.actor.exit_actor()

    def __repr__(self):
        return "Island %s" % self.island_id
