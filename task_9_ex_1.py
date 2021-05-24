"""
Task_9_1
Implement `swap_quotes` function which receives a string and replaces all " symbols with ' and vise versa.
The function should return modified string.

Note:
Usage of built-in or string replacing functions is required.
"""


def swap_quotes(some_string: str) -> str:
    quote_code = ord("'")
    dbl_quote_code = ord('"')
    my_dict = {quote_code: dbl_quote_code,
               dbl_quote_code: quote_code}

    return some_string.translate(my_dict)
