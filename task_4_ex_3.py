"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter: str = ' ') -> list:
    if not (isinstance(str_to_split, str) and isinstance(delimiter, str)):
        raise ValueError()

    for i in range(len(str_to_split) - (n := len(delimiter)) + 1):
        if str_to_split[i:i + n] == delimiter:
            return [str_to_split[:i]] + split_alternative(str_to_split[i + n:], delimiter)

    return [str_to_split]
