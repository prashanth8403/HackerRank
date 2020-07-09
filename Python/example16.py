#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    visited = []
    pairs = 0
    for x in range(0,n):
        cur = ar[x]
        if x not in visited:
            for y in range(x+1,n):
                if cur == ar[y] and y not in visited:
                    print(x,y,ar[x],ar[y],visited)
                    pairs+=1
                    visited.append(y)
                    break
    return pairs

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
