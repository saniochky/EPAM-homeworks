"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""
import argparse


def check_input(capacity, bars_weight, bars_amount):
    if len(bars_weight) != bars_amount or sum(_ < 1 for _ in bars_weight + [capacity, bars_amount]) != 0:
        raise ValueError


def bounded_knapsack(args):
    return knapsack_rec(args.W, args.w, args.n)


def knapsack_rec(capacity, bars_weight, bars_amount):
    if bars_amount == 0:
        return 0

    if bars_weight[0] > capacity:
        return knapsack_rec(capacity, bars_weight[1:], bars_amount - 1)

    else:
        return max(
            bars_weight[0] + knapsack_rec(capacity - bars_weight[0], bars_weight[1:], bars_amount - 1),
            knapsack_rec(capacity, bars_weight[1:], bars_amount - 1)
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-W', type=int)
    parser.add_argument('-w', nargs='*', type=int)
    parser.add_argument('-n', type=int)

    args = parser.parse_args()
    check_input(args.W, args.w, args.n)

    print(bounded_knapsack(args))


if __name__ == '__main__':
    main()
