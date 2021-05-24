"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(string: str) -> str:
    new_string = []

    for el in string:
        if el == '"':
            new_string.append("'")
        elif el == "'":
            new_string.append('"')
        else:
            new_string.append(el)

    return ''.join(new_string)
