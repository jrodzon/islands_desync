from typing import List

import ray

from islands_desync.geneticAlgorithm.run_hpc.run_algorithm_params import \
    RunAlgorithmParams
from islands_desync.Island import Island


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

        computations = ray.get(
            [
                island.start.remote(island, topology[island_id], self.params)
                for island_id, island in enumerate(islands)
            ]
        )

        return [computation.start.remote() for computation in computations]
