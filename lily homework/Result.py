import math
import os
import random
import re
import sys


def findNoOfSwaps(arr):
    # hashMap for storing in key : value pair. Use for storing indexes of values in array
    hashMap = {}

    result = 0

    for i in range(len(arr)):
        # storing value as key and index as value
        hashMap[arr[i]] = i

    sortedArray = sorted(arr)

    for i in range(len(arr)):
        if arr[i] != sortedArray[i]:
            # increment the counter
            result += 1

            index = hashMap[sortedArray[i]]
            hashMap[arr[i]] = index

            # swap the elements
            arr[i], arr[index] = arr[index], arr[i]

    return result


def lilysHomework(arr):
    # we are calculating absolute difference so sometime if we sort in descending then probably less number of swaps will be needed
    # so instead of calculating again for descending we send reverse of array
    return min(findNoOfSwaps(arr), findNoOfSwaps(arr[::-1]))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    # arr = [3, 7, 25, 15]

    result = min(lilysHomework(arr), lilysHomework(arr[::-1]))

    fptr.write(str(result) + "\n")

    fptr.close()
