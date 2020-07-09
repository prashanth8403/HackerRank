num = int(input())
d = len(str(bin(num)[2:]))
new = str(bin(num)[2:])[::-1]
for x in range(0,32-d):
    new += '0'
print(int(new,2))
