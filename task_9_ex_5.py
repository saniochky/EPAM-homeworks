"""
Implement function count_letters, which takes string as an argument and
returns a dictionary that contains letters of given string as keys and a
number of their occurrence as values.

Example:
print(count_letters("Hello world!"))
Result: {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

Note: Pay attention to punctuation.
"""


def count_letters(s: str) -> dict:
    if type(s) is not str:
        raise TypeError

    my_dict = {}

    for sym in set(s):
        if sym.isalpha():
            my_dict[sym] = s.count(sym)

    return my_dict
