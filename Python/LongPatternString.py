#!/bin/python3

"""

Lilah has a string,s , of lowercase English letters that she repeated infinitely many times.

Given an integer,n , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string s='abac' and ,n=10 the substring we consider is ,abacabacab the first 10  characters of her infinite string. There are 4 occurrences of a in the substring.

"""

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
