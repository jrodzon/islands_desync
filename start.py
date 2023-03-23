import sys

from Island import Island


def main():
    island_count = int(sys.argv[1])

    islands = [Island.remote(i) for i in range(island_count)]

    for island in islands:
        island.start.remote(
            filter(lambda isl: isl.island_id != island.island_id, islands)
        )


if __name__ == '__main__':
    main()


