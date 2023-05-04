from typing import Dict, List

import ray

from islands_desync.Emigration import Emigration
from islands_desync.geneticAlgorithm.migrations.Migration import Migration


class RayMigration(Migration):
    def __init__(self, islandActor, emigration: Emigration):
        super().__init__()
        self.emigration = emigration
        self.islandActor = islandActor

    def migrate_individuals(self, individuals_to_migrate, iteration_number, island_number):
        print('Emigracja %s iter: %s' %(island_number, iteration_number))
        for individual in individuals_to_migrate:
            # print("%s: Emigruje %s" % (self.islandActor, individual))
            self.emigration.emigrate.remote((individual, iteration_number))

    def receive_individuals(
        self, step_num: int, evaluations: int
    ) -> (List, Dict | None):

        new_individuals = ray.get(self.islandActor.get_immigrants.remote())

        new_individuals, migrant_iteration_numbers = zip(*new_individuals)

        migration_at_step_num = {
            "step": step_num,
            "ev": evaluations,
            "iteration_numbers": migrant_iteration_numbers
        }

        return list(new_individuals), migration_at_step_num
