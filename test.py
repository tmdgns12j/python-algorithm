s="aaccc"
def solution(s):
    
    for i in range(1,len(s)//2+1):#한번에 탐색범위
        line=""
        c=0
        temp=s[0:i]
        for j in range(0,len(s),i):#문자열 
            if temp==s[j:j+i]:
                c+=1
            else:
                if c==1:
                    line+=temp
                else:
                    line=line+str(c)+temp
                    temp=s[j:j+i]
                c=1
            if len(s)-j<=i:
                 line=line+str(c)+temp
print(solution(s))