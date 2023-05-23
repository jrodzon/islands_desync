import time
from typing import List

import ray

from islands_desync.geneticAlgorithm.run_hpc.run_algorithm_params import (
    RunAlgorithmParams,
)
from islands_desync.islands.core.Island import Island
from islands_desync.islands.core.SignalActor import SignalActor


class IslandRunner:
    def __init__(self, CreateTopology, SelectAlgorithm, params: RunAlgorithmParams):
        self.CreateTopology = CreateTopology
        self.SelectAlgorithm = SelectAlgorithm
        self.params: RunAlgorithmParams = params

    def create(self) -> List[ray.ObjectRef]:
        islands = [
            Island.remote(i, self.SelectAlgorithm())
            for i in range(self.params.island_count)
        ]

        topology = self.CreateTopology(
            self.params.island_count, lambda i: islands[i]
        ).create()

        # computations = [
        #     ray.get(
        #         islands[0].start.remote(islands[0], topology[0], self.params)
        #     )
        # ]
        #
        # from glob import glob
        # paths = glob(".", recursive=True)
        # for p in paths:
        #     print(p)
        #
        # computations.extend(
        #     ray.get(
        #         [
        #             island.start.remote(island, topology[island_id], self.params)
        #             for island_id, island in enumerate(islands[1:])
        #         ]
        #     )
        # )

        signal_actor = SignalActor.remote(self.params.island_count)

        computations = ray.get(
            [
                island.start.remote(island, topology[island_id], self.params, signal_actor)
                for island_id, island in enumerate(islands)
            ]
        )

        print("Starting " + str(len(computations)) + "comps")

        return [computation.start.remote() for computation in computations]
