import json
import sys
from datetime import datetime

import ray
from islands.core.IslandRunner import IslandRunner
from islands.selectAlgorithm import RandomSelect
from islands.topologies import RingTopology

from islands_desync.geneticAlgorithm.run_hpc.run_algorithm_params import (
    RunAlgorithmParams,
)
from islands_desync.islands.topologies.TorusTopology import TorusTopology


def main():
    if sys.argv[2] != " ":
        ray.init(_temp_dir=sys.argv[2], num_cpus=4)
    
    params = RunAlgorithmParams(
        island_count=int(sys.argv[1]),
        number_of_emigrants=int(sys.argv[3]),
        migration_interval=int(sys.argv[4]),
        dda=sys.argv[5],
        tta=sys.argv[6],
        series_number=1,
        sequence_lenght=int(sys.argv[7])
    )
    # ray.init(_temp_dir='/tmp/ray')

    # params = RunAlgorithmParams(
    #     island_count=5,
    #     number_of_emigrants=5,
    #     migration_interval=5,
    #     dda=datetime.today().strftime("%Y%m%d"),
    #     tta=datetime.now().strftime("%H%M%S"),
    #     series_number=1,
    # )

    computation_refs = IslandRunner(RingTopology, RandomSelect, params).create()

    results = ray.get(computation_refs)

    iterations = {result["island"]: result for result in results}

    with open(
        "logs/"
        + "iterations_per_second"
        + datetime.now().strftime("%m-%d-%Y_%H%M")
        + ".json",
        "w",
    ) as f:
        json.dump(iterations, f)


if __name__ == "__main__":
    main()
