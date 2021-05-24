"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]`
which splits the `string` by indexes specified in `indexes`. 
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```
"""


def split_by_index(string, indexes):
    if not (isinstance(string, str) and isinstance(indexes, list)):
        raise ValueError()

    result = []
    last_valid_index = 0

    for index in indexes:
        if isinstance(index, int) and index > last_valid_index:
            result.append(string[last_valid_index:index])
            last_valid_index = index

    return result + [string[last_valid_index:]] if last_valid_index < len(string) else result
