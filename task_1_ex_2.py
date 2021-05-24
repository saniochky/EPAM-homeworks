"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse
import math
import operator


def calculate(args):
    if (operation := args.op) in dir(math):
        return getattr(math, operation)(*args.exp)
    elif operation in dir(operator):
        return getattr(operator, operation)(*args.exp)
    raise NotImplementedError()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('op', type=str)
    parser.add_argument('exp', type=float, nargs='*')

    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
