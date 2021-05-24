"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
  Note: use `string.ascii_lowercase` for list of alphabet letters

Note: raise TypeError in case of wrong data type

Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
>>> {'o'}
print(chars_in_one(*test_strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(chars_in_two(*test_strings))
>>> {'h', 'l', 'o'}
print(not_used_chars(*test_strings))
>>> {'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'}
"""
import string


def test_data(data):
    if not all(type(el) is str for el in data):
        raise TypeError


def chars_in_all(*strings):
    test_data(strings)

    if len(strings) < 2:
        return set()

    return set(strings[0]).intersection(*[set(el) for el in strings[1:]])


def chars_in_one(*strings):
    test_data(strings)

    if len(strings) < 2:
        return set(strings[0])

    return set(strings[0]).union(*[set(el) for el in strings[1:]])


def chars_in_two(*strings):
    if len(strings) < 2:
        raise ValueError

    test_data(strings)
    all_s = ''.join(strings)

    for letter in set(all_s):
        all_s = all_s.replace(letter, '', 1)

    return set(all_s)


def not_used_chars(*strings):
    return set(string.ascii_lowercase).difference(set(''.join(strings)))
