"""
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
"""

nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())
s = sorted(arr, key = lambda x: x[k])
[print(str.join(' ', map(str, s[i]))) for i in range(n)]    
