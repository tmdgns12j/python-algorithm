#백준
from collections import deque
n=int(input())
for i in range(n):
    command=input()
    command=command.replace('RR','')
    c=int(input())
    arr=input()[1:-1].split(',')
    queue=deque(arr)
    if c==0:
        arr=[]
    for j in command:
        if j=='R':
            arr=arr[::-1]
        else:
            if len(arr)==0:
                print("error")
                break
            else:
                arr.pop(0)
    else:
        print('['+','.join(arr)+']')