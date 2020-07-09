    
import os
import sys

def main(argv):
    path = 'D:\\Programs\\python\\units'+'\\'+argv[0]
    files = os.listdir(path)
    for filename in files:
        data = open(path+'\\'+filename,'r')
        data = list(data)
        for item in data:
            print(item.split(',')[int(argv[1])-1])

if __name__ == "__main__":
    main(sys.argv[1:])