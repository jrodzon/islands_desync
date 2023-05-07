import asyncio
import sys

from islands_desync.IslandRunner import IslandRunner
from islands_desync.topologies import RingTopology


import ray
from selectAlgorithm import RandomSelect

from islands_desync.geneticAlgorithm.run_hpc.run_algorithm_params import (
    RunAlgorithmParams,
)


def main():
    if sys.argv[2] != " ":
        ray.init(_temp_dir=sys.argv[2])

    params = RunAlgorithmParams(
        island_count=int(sys.argv[1]),
        number_of_emigrants=int(sys.argv[3]),
        migration_interval=int(sys.argv[4]),
        dda=sys.argv[5],
        tta=sys.argv[6],
        series_number=1,
    )

    computation_refs = IslandRunner(RingTopology, RandomSelect, params).create()

    ray.get(computation_refs)


if __name__ == "__main__":
    main()
