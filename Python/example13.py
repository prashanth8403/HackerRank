# geeks
# abdcba
x = -1
data = []
s = input()
for x in range(0,len(s)):
    data.append(s[x])
dict = {}
for i in range(0,len(data)-1):
    if data[i] != data[i+1]:
        for k in range(i,len(data)-i):
            if data[i] == data[k]:
                dict[data[i]] = k
    else:
        x=i
        break
if x != -1:
    print(data[x],data[x+1])
else:
    print(dict)
