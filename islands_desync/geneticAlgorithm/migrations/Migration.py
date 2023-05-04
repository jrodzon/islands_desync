from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Dict, List


class Migration(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def migrate_individuals(self, individuals_to_migrate, iteration_number: int):
        pass

    @abstractmethod
    def receive_individuals(
            self, step_num: int, evaluations: int
    ) -> (List, Dict | None):
        pass
