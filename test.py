#백준 1541
s=input()
cal=[]
for i in range(len(s)):
    if s[i].isdigit():
        continue
    else:
        cal.append(s[i])
        s=s.replace(s[i],' ',1)
s=s.split()
for i in range(len(s)):
    s[i]=int(s[i])
i=0
while '+' in cal:
    if cal[i]=='+':
        s[i]+=s[i+1]
        s.pop(s.index(s[i+1]))
        cal.pop(cal.index('+'))
        i=0
    else:
        i+=1
result=s[0]
for i in range(1,len(s)):
    result-=s[i]
print(result)