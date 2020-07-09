import time

start = time.time()
Data = [1,20,5,6,9,2,10,15,7,3,8]
n = 10
for y in range(0,len(Data)):
    item = Data[y]
    for x in range(0,len(Data)):
        if n-item == Data[x] and x != y:
            print('('+str(item)+','+str(Data[x])+')')
end = time.time()
time = end-start
print(time)