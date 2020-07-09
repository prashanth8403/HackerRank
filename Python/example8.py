"""

4
add hack
add hacer
"""
words = []
in_ls = input()
data = in_ls.split()
#data[0] - 4
for x in range(1,int(data[0])):
    temp = data[x].split()
    if temp[0] == 'add':
        words.append(str(temp[1]))

for x in range(1,int(data[0])):
    temp = data[x].split() 
    if temp[0] == 'find':
        for item in words:
            lens = len(temp[1])
            if item[0:len] == temp[1]:
                #-----
                x = 0