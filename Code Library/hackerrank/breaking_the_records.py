#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mn = scores[0]
    mx = scores[0]
    cmn = 0
    cmx = 0
    for i in range(1,len(scores)):
        if scores[i] < mn:
            cmn = cmn+1
            mn = scores[i]
        if scores[i] > mx:
            cmx = cmx +1
            mx = scores[i]
    return [cmx,cmn]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
