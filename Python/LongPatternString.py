#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    for x in range(len(s)):
        if s[x] == 'a':
            count+=1
    factor = n%len(s)
    if factor != 0:
        count=count*int(n/len(s))
        for x in range(factor):
                if s[x] == 'a':
                    count+=1
    else:
        count=count*int(n/len(s))
    return count

if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(result)
