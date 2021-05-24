"""
Write 2 functions:
1. Function 'is_sorted', determining whether a given list of integer values of arbitrary length
is sorted in a given order (the order is set up by enum value SortOrder).
List and sort order are passed by parameters. Function does not change the array, it returns
boolean value.

2. Function 'transform', replacing the value of each element of an integer list with the sum
of this element value and its index, only if the given list is sorted in the given order
(the order is set up by enum value SortOrder). List and sort order are passed by parameters.
To check, if the array is sorted, the function 'is_sorted' is called.

Example for 'transform' function,
For [5, 17, 24, 88, 33, 2] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “descending” sort order the values in the array are changing to [15, 11, 5]

Note:
Raise TypeError in case of wrong function arguments data type;
"""
from enum import Enum


class SortOrder(Enum):
    ASCENDING = "ascending"
    DESCENDING = "descending"


def is_sorted(num_list: list[int], sort_order: SortOrder) -> bool:
    if isinstance(sort_order, SortOrder) and isinstance(num_list, list) and all(type(x) is int for x in num_list):
        if sort_order.value == "ascending":
            return num_list == sorted(num_list, reverse=False)
        return num_list == sorted(num_list, reverse=True)

    raise TypeError()


def transform(num_list: list[int], sort_order: SortOrder) -> list[int]:
    if isinstance(sort_order, SortOrder) and isinstance(num_list, list) and all(type(x) is int for x in num_list):
        if is_sorted(num_list, sort_order):
            for index, value in enumerate(num_list):
                num_list[index] = value + index

        return num_list

    raise TypeError()
