n=int(input())
num=[]
def solution(n,num):
    for i in range(n):
        num.append(int(input()))
    num.sort()
    if n==1:
        return num[0]
    hap=0
    dp=[0]*n
    dp[0]=num[0]
    for i in range(1,n):
        dp[i]=dp[i-1]+num[i]
    return sum(dp)-dp[0]

print(solution(n,num))