import math
import os
import random
import re
import sys


def lilysHomework(arr):
    # we are calculating absolute difference so sometime if we sort in descending then probably less number of swaps will be needed
    sort = sorted(arr)
    rev = arr[::-1]

    # hashMap for storing in key : value pair. Use for storing indexes of values in array
    hashMap = {}

    for i in range(n):
        # storing value as key and index as value
        hashMap[sort[i]] = i

    swaps = 0
    i = 0

    while i < len(arr):
        if sort[i] == arr[i]:
            i += 1
            continue
        # increment the count of swap
        swaps += 1
        index = hashMap[arr[i]]
        # swap the elements
        arr[index], arr[i] = arr[i], arr[index]
        hashMap[sort[i]] += 1

    # for reversed array
    hashMap = {}
    for i in range(n):
        hashMap[sort[i]] = i

    swaps_rev = 0
    i = 0
    while i < len(arr):
        if sort[i] == rev[i]:
            i += 1
            continue
        swaps_rev += 1
        index = hashMap[rev[i]]
        rev[index], rev[i] = rev[i], rev[index]
        hashMap[sort[i]] += 1

    return min(swaps, swaps_rev)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
