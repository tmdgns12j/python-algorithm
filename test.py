import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    temp=0
    command=sys.stdin.readline().split()
    if len(command)==2:
        temp=int(command[1])
        arr.append(temp)
    elif command[0]=="top":
        if len(arr)==0:
            print('-1')
        else:
            print(arr[-1])
    elif command[0]=='size':
        print(len(arr))
    elif command[0]=='empty':
        if len(arr)==0:
            print('1')
        else:
            print('0')
    elif command[0]=='pop':
        if len(arr)==0:
            print('-1')
        else:
            print(arr.pop())