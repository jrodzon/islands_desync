import ray
from Emigration import Emigration
from islands_desync.geneticAlgorithm.migrations.ray_migration import RayMigration

from islands_desync.geneticAlgorithm.run_hpc.create_algorithm_hpc import (
    create_algorithm_hpc,
)
from islands_desync.geneticAlgorithm.run_hpc.run_algorithm_params import (
    RunAlgorithmParams,
)


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

        self.algorithm = create_algorithm_hpc(n, migration, algorithm_params)

    def start(self):
        self.algorithm.run()
        result = self.algorithm.get_result()
        print(f"\nIsland: {self.n} Fitness: {result.objectives[0]}")

        self.finish()

    def finish(self):
        ray.kill(self.emigration)
        ray.kill(self.island)
        ray.actor.exit_actor()
