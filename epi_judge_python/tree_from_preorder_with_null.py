import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    # TODO you fill in here.
    return BinaryTreeNode()


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == "null" else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_from_preorder_with_null.py",
            "tree_from_preorder_with_null.tsv",
            reconstruct_preorder_wrapper,
        )
    )
