from itertools import permutations
from collections import deque
expression="100-200*300-500+20"
cal=[]
num=expression
for i in range(len(expression)):
    if expression[i].isdigit():
        continue
    else:
        cal.append(expression[i])
        num=num.replace(expression[i],' ')
num=num.split()
print(num)
print(cal)
new=['-','+','*']
new=list(permutations(new,3))
print(new)
queue=deque(cal)
# for i in range(len(new)):
#     for j in range(len(new[0])):
#         for k in range(len(cal)):
for i in new:
    a,b,c=i
    for j in range(len(cal)):
        if cal[j]==a: