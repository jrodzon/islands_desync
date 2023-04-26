import asyncio
import sys

import ray

from Island import Island
from selectAlgorithm import RandomSelect
from src.geneticAlgorithm.run_hpc.run_algorithm_params import RunAlgorithmParams


async def main():
    if sys.argv[2] != " ":
        ray.init(_temp_dir=sys.argv[2])

    params = RunAlgorithmParams(
        island_count=int(sys.argv[1]),
        number_of_emigrants=int(sys.argv[3]),
        migration_interval=int(sys.argv[4]),
        dda=sys.argv[5],
        tta=sys.argv[6],
        series_number=1
    )

    islands = [
        Island
        .remote(i, RandomSelect())
        for i in range(params.island_count)
    ]

    refs = [
        island.start.remote(island,
                            list(map(lambda other_island: other_island[1],
                                     filter(lambda other_island: other_island[0] != island_id, enumerate(islands))
                                     )),
                            params
                            )
        for island_id, island in enumerate(islands)
    ]

    await asyncio.wait(refs)


if __name__ == '__main__':
    asyncio.run(main())
