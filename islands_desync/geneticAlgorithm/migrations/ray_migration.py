from typing import Dict, List

import ray

from islands_desync.Emigration import Emigration
from islands_desync.geneticAlgorithm.migrations.Migration import Migration


class RayMigration(Migration):
    def __init__(self, islandActor, emigration: Emigration):
        super().__init__()
        self.emigration = emigration
        self.islandActor = islandActor

    def migrate_individuals(self, individuals_to_migrate):
        for individual in individuals_to_migrate:
            # print("%s: Emigruje %s" % (self.islandActor, individual))
            self.emigration.emigrate.remote(individual)

    def receive_individuals(
        self, step_num: int, evaluations: int
    ) -> (List, Dict | None):
        return ray.get(self.islandActor.get_immigrants.remote()), None
