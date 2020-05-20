#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    c1 = 0
    c2 = 0
    c3 = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            c1 = c1 + 1
        elif arr[i] < 0:
            c2 = c2 + 1
        else:
            c3 = c3 + 1
    print(round(c1/len(arr),6))
    print(round(c2/len(arr),6))
    print(round(c3/len(arr),6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
