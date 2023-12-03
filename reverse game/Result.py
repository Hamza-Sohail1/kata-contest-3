#!/bin/python3

import math
import os
import random
import re
import sys


def reverse_game(n, k):
    # if element is from first half of original array
    # then start finding it from start else start finding it from end
    if k < n // 2:
        return k * 2 + 1
    else:
        return (n - k - 1) * 2


if __name__ == "__main__":
    t = int(input().strip())

    for i in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])

        # n = 3
        # k = 1

        print(reverse_game(n, k))
