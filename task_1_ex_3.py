""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Sign = '+' | '-'
Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""
import argparse


def check_formula(user_input):
    last_element = '+'
    result = 0
    operation_determinant = {
        '+': lambda operand1, operand2: operand1 + operand2,
        '-': lambda operand1, operand2: operand1 - operand2
    }
    exp = ''.join(user_input).replace(' ', '').replace('+', ' + ').replace('-', ' - ').split()

    for element in exp:
        if element.isnumeric():
            result = operation_determinant[last_element](result, int(element))
        elif element not in operation_determinant or last_element in operation_determinant:
            return False, None

        last_element = element

    return last_element not in operation_determinant, result if last_element not in operation_determinant else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('user_input')

    args = parser.parse_args()
    print(check_formula(args.user_input))


if __name__ == '__main__':
    main()
