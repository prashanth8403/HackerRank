# Enter your code here. Read input from STDIN. Print output to STDOUT
data = []
for i in range(0,4):
    data.append(input())
header = data[0].split(' ')
array = data[1].split(' ')
a = data[2].split(' ')
b = data[3].split(' ')
n = int(header[0])
m = int(header[1])
x = 0

for item in array:
    for aitem in a:
        if item == aitem:
            for xitem in array:
                if xitem == aitem:
                    x+=1
            a.remove(aitem)
for item in array:
    for bitem in b:
        if item == bitem:
            for xitem in array:
                if xitem == bitem:
                    x-=1
            b.remove(bitem)
print(x) 