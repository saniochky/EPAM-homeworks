"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import argparse


interpreter = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100
    }


def check_number(number):
    for sym in number:
        if sym not in interpreter:
            raise ValueError()

    for sym in interpreter:
        if interpreter[sym] // 5 in interpreter.values():
            if number.count(sym) > 1:
                raise ValueError()
            continue

        if number.count(sym) > 4 or sym * 4 in number:
            raise ValueError()


def from_roman_numerals(number):
    check_number(number)
    result = 0
    last_sym = 'C'
    pre_last_sym = 'C'

    for sym in number:
        result += interpreter[sym]

        if interpreter[sym] > interpreter[last_sym]:
            result -= 2 * interpreter[last_sym]
            if interpreter[sym] > interpreter[pre_last_sym]:
                raise ValueError()

        pre_last_sym = last_sym
        last_sym = sym

    if result < 101:
        return result
    raise ValueError()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=str)

    args = parser.parse_args()
    print(from_roman_numerals(args.number))


if __name__ == "__main__":
    main()
