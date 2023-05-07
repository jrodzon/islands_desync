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

        self.algorithm = create_algorithm_hpc(
            n, migration, algorithm_params
        )

    def start(self):
        self.algorithm.run()
        result = self.algorithm.get_result()
        print(f"\nIsland: {self.n} Fitness: {result.objectives[0]}")

        self.finish()

    def finish(self):
        ray.kill(self.emigration)
        ray.kill(self.island)
        ray.actor.exit_actor()

    # def iteration(self):
    #
    #     self.iteration_count += 1
    #
    #     immigrants: [Immigrant] = ray.get(self.island.get_immigrants.remote())
    #
    #     if len(immigrants) > 0:
    #         print('%s: dostaje %s' % (self.island_description(), immigrants))
    #
    #     self.population += immigrants
    #
    #     print('%s: wszyscy osobnicy: %s' % (self.island_description(), self.population))
    #
    #     sleep(2.0)  # computation
    #
    #     for member in self.population:
    #         member.increment_iteration()
    #
    #     if len(self.population) > 0:
    #         target_num = random.randint(0, len(self.population) - 1)
    #         print('%s: Emigruje %s' % (self.island_description(), str(self.population[target_num])))
    #         self.emigration.emigrate.remote(self.population.pop(target_num))
    #
    # def island_description(self):
    #     return "Wyspa %s iter: %s" % (self.n, self.iteration_count)
