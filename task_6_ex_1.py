"""
Implement function combine_dicts, which receives a changeable
number of dictionaries (keys - letters, values - integers)
and combines them into one dictionary.

Dict values should be summarized in case of identical keys.

Example:
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

combine_dicts(dict_1, dict_2)
Result: {'a': 300, 'b': 200, 'c': 300}

combine_dicts(dict_1, dict_2, dict_3)
Result: {'a': 600, 'b': 200, 'c': 300, 'd': 100}
"""


def combine_dicts(*dicts):
    final_dict = {}

    for dictionary in dicts:
        for key, value in dictionary.items():
            if not key.isalpha() or len(key) > 1:
                raise KeyError()
            if type(value) is not int:
                raise ValueError()
            if key not in final_dict:
                final_dict[key] = 0

            final_dict[key] += value

    return final_dict
