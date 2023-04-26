from abc import ABC
from abc import abstractmethod
from typing import List, Dict
from collections import defaultdict


class Migration(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def migrate_individuals(self, individuals_to_migrate):
        pass

    @abstractmethod
    def receive_individuals(self, step_num: int, evaluations: int) -> (List, Dict | None):
        pass
