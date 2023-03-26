import asyncio
import sys
import time

import ray

from Island import Island
from selectAlgorithm import RandomSelect


async def main():
    island_count = int(sys.argv[1])

    islands = [
        Island
        .remote(i, RandomSelect())
        for i in range(island_count)
    ]

    refs = [
        island.start.remote(island,
                            list(map(lambda other_island: other_island[1],
                                     filter(lambda other_island: other_island[0] != island_id, enumerate(islands))
                                     ))
                            )
        for island_id, island in enumerate(islands)
    ]

    await asyncio.wait(refs)


if __name__ == '__main__':
    asyncio.run(main())
