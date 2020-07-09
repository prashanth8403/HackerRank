
"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

"""


if __name__ == '__main__':
    temp = ''
    data = []
    inputx = []
    N = int(input())
    for x in range(0,N):
        temp += input() + '\n'
    inputx = temp.split('\n')
    #print(inputx)
    for command in inputx:
        if command[0:2] == 'in':
            content = command.split(' ')
            data.insert(int(content[1]),int(content[2]))
        elif command[0:2] == 'pr':
            print(data)
        elif command[0:2] == 'po':
            data.pop()
        elif command[0:2] == 'so':
            data.sort()
        elif command[0:3] == 'rev':
            data = data[::-1]
        elif command[0:3] == 'rem':
            content = command.split(' ')
            data.remove(int(content[1]))
        elif command[0:2] == 'ap':
            content = command.split(' ')
            data.append(int(content[1]))