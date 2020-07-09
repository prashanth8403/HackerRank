#1004 1554
ls = []
num = int(input())
num = str(num)
for x in range(0,len(num)):
    ls.append(num[x])
for x in range(0,len(ls)):
    if ls[x] == '0':
        ls[x] = 5
n = ''
for item in ls:
    n+=str(item)
print(int(n))