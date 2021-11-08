#  Observations:
#     * The item list must be sorted;
#     * Returns the position of the item in the list;
#
#
#
#             LEFT               MIDDLE              RIGHT
#              \/                  \/                  \/
#  indexes:   [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]  [8]
#            |--------------------------------------------|
#  values:   | 20 | 23 | 25 | 28 | 35 | 36 | 40 | 41 | 42 |
#            |--------------------------------------------|
#
#
#  Running Time:
#     * Best-case O(1)
#     * Average O(log n)
#     * Worst-case O(log n)
#

from typing import List, Optional, TypeVar

T = TypeVar("T", int, str)


def binary_search(list_of_items: List[T], target: T) -> Optional[int]:
    left = 0  # Top of the list.
    right = len(list_of_items) - 1  # Position of the last item on the list.

    while (
        left <= right
    ):  # Keep going while LEFT value (lower) is below or equal to the RIGHT (higher).
        middle = (left + right) // 2  # Position of the MIDDLE item on the list.

        guess = list_of_items[middle]
        if guess == target:  # Found the target item in the MIDDLE.
            return middle
        elif guess > target:  # The guess was TOO HIGH.
            right = middle - 1
        else:  # The guess was TOO LOW.
            left = middle + 1

    return None  # The target item doesn't exist.
