from typing import List

from test_framework import generic_test


def get_max_trapped_water(heights: List[int]) -> int:
    # TODO you fill in here.
    return 0


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "max_trapped_water.py", "max_trapped_water.tsv", get_max_trapped_water
        )
    )
