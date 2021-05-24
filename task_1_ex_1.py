"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('operand1', type=float)
parser.add_argument('operation', type=str)
parser.add_argument('operand2', type=float)

operation_determinant = {
        '+': lambda operand1, operand2: operand1 + operand2,
        '-': lambda operand1, operand2: operand1 - operand2,
        '*': lambda operand1, operand2: operand1 * operand2,
        '/': lambda operand1, operand2: operand1 / operand2
    }


def calculate(args):
    if operation := operation_determinant.get(args.operation):
        return operation(args.operand1, args.operand2)
    raise NotImplementedError()


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
