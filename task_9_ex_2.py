"""
Write a function that checks whether a string is a palindrome or not.
Return 'True' if it is a palindrome, else 'False'.

Note:
Usage of reversing functions is required.
Raise ValueError in case of wrong data type

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
"""


def is_palindrome(test_string: str) -> bool:
    if type(test_string) is not str:
        raise ValueError

    test_string = test_string.lower()
    for sym in test_string:
        if not sym.isalpha():
            test_string = test_string.replace(sym, '')

    return test_string == "".join(reversed(test_string))
