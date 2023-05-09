import time

import ray
from Emigration import Emigration

from islands_desync.geneticAlgorithm.algorithm.genetic_island_algorithm import \
    GeneticIslandAlgorithm
from islands_desync.geneticAlgorithm.migrations.ray_migration import \
    RayMigration
from islands_desync.geneticAlgorithm.run_hpc.create_algorithm_hpc import \
    create_algorithm_hpc
from islands_desync.geneticAlgorithm.run_hpc.run_algorithm_params import \
    RunAlgorithmParams


@ray.remote
class Computation:
    def __init__(
        self,
        island,
        n: int,
        islands,
        select_algorithm,
        algorithm_params: RunAlgorithmParams,
    ):
        self.island = island
        self.n: int = n

        self.emigration = Emigration.remote(islands, select_algorithm)
        migration = RayMigration(island, self.emigration)

        self.algorithm: GeneticIslandAlgorithm = create_algorithm_hpc(
            n, migration, algorithm_params
        )

    def start(self):
        start = time.time()

        self.algorithm.run()
        result = self.algorithm.get_result()

        run_time = time.time() - start

        calculations = {
            "island": self.n,
            "iterations": self.algorithm.step_num,
            "time": run_time,
            "ips": self.algorithm.step_num / run_time,
        }

        print(f"\nIsland: {self.n} Fitness: {result.objectives[0]}")

        return calculations
