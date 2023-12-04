#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#


def highestValuePalindrome(s, n, k):
    # Write your code here

    # two pointers left and right for traversing from both ends
    left = 0
    right = len(s) - 1

    result = list(s[::])

    while left <= right and k >= 0:
        # if not equal than replace the value with the maximum one
        if result[left] != result[right]:
            result[left] = max(result[left], result[right])
            result[right] = max(result[left], result[right])
            k -= 1

        left += 1
        right -= 1

    # it means that we can make above string palindrome within the max limit of changes allowed
    if k < 0:
        return '-1'

    left = 0
    right = len(s) - 1

    while left <= right and k > 0:
        # string is of odd length and we are at center
        if left == right and k > 0:
            result[left] = result[right] = "9"
            k -= 1
            continue

        # if current character is less than 9 then we can replace it with 9 if swaps are available
        if result[left] < "9":
            if k > 0 and result[left] != s[left] or result[right] != s[right]:
                # if we have already swap that index then we can ignore that and replace its value with 9
                result[left] = result[right] = "9"
                # only single swap is needed because we discarded the previous swap
                k -= 1
            elif k >= 2 and result[left] != result[right]:
                # if they are not previously swapped then replaced both with 9 and dec by 2 because we have done 2 swaps
                result[left] = result[right] = "9"
                k -= 2

        left += 1
        right -= 1

    return "".join(result)


if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    # n = 4
    # k = 1
    # s = "3043"

    result = highestValuePalindrome(s, n, k)

    # print(result)

    fptr.write(result + '\n')

    fptr.close()
