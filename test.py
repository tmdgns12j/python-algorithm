from itertools import permutations
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