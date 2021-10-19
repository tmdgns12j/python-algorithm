s="ababccccc"
def solution(s):
    start=0
    c=1
    temp=""
    line=""
    for i in range(1,len(s)//2+1):
        for j in range(0,len(s),i):
            if temp==s[start:i]:
                c+=1
            else:
                if c==1:
                    line+=temp
                else:
                    line=line+str(c)+temp
                c=1
            temp=s[start:i]
            start=i

print(solution(s))