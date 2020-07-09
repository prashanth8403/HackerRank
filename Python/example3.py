data = input()
values = data.split()
exp = input()
exp = exp.split()
value = 0

if len(exp) > 1:
    for index in range(0,len(exp)):
        item = exp[index]
        factor = 1
        if item == 'x':
            factor = int(data[0])
            if index > 0:
                if exp[index-1] == '+':
                    value += int(data[0])
                else:
                    value -= int(data[0])
            else:
                value += int(data[0])
        elif item[0] == 'x':
            temp = int(item[-1])
            for x in range(0,temp):
                factor*= int(data[0])
            if index == 0:
                value+=factor
            else:
                if exp[index-1] == '+':
                    value+=factor
                else:
                    value-=factor
        elif len(item) >= 6:
                temp = int(item[-1])
                for x in range(0,temp):
                    factor*= int(data[0])
                factor *= int(item[0])
                if index == 0:
                    value+=factor
                else:
                    if exp[index-1] == '+':
                        value+=factor
                    else:
                        value-=factor
        elif item[0].isnumeric():
            factor = int(item[0])
            if index == 0:
                value+=factor
            else:
                if exp[index-1] == '+':
                    value+=factor
                else:
                    value-=factor
else:
    if exp[-1][0].isnumeric() and exp[-1][2] != 'x':
        factor = 1
        temp = int(exp[-1][-1])
        for x in range(0,temp):
            factor*= int(data[0])
        factor *= int(exp[-1][0])
        value = factor
    elif exp[-1] == 'x':
        value = int(data[0])
    elif exp[-1][0].isnumeric():
        value = int(exp[-1][0])
    else:
        factor = 1
        temp = int(exp[-1][-1])
        for x in range(0,temp):
            factor*= int(data[0])
        value=factor
if int(values[1]) == value:
    print('True')
else:
    print('False')