s="aaabbaaa"
def solution(s):
    count=[]
    c=1
    temp=0
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            c+=1
        else:
            count.append(c)
            c=1
        if i==len(s)-1:
            count.append(c)
    if s[0]==s[-1]:
        temp=count[0]+count[-1]
        count.pop()
        count[0]=temp
    count.sort()
    return count
print(solution(s))