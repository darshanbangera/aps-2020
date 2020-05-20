#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    # Write your code here
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 = sum1 + arr[i][i]
        sum2 = sum2 + arr[i][n-i-1]

    return abs(sum1-sum2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.close()
