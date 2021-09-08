#2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
n=int(input())
first=0
second=1
hap=0
for i in range(n):
    if n==0 or n==1:
        print(1)
        break
    else :
        hap=first+second
        second=first
        first=hap
if n!=0 and n!=1:
    print(hap%1234567)

#str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
#예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
def solution(s):
    s=s.replace('"','')
    arr=list(map(int,s.split()))
    answer = str(min(arr))+' '+str(max(arr))
    return answer


#N개의 최소공배수 gcd()
#N개의 배열이 주어질때 최소공배수를 구하여라
arr=[2,6,8,14]
def solution(arr):
    m=max(arr)
    while 1:
        c=0
        for i in arr:
            if m%i==0:
                c+=1
            else:
                m+=1
                break
        if c==len(arr):
            break
    return m
print(solution(arr))    #168

#다른풀이 gcd()사용
# from fractions import gcd
# def nlcm(num):      
#     answer = num[0]
#     for n in num:
#         answer = n * answer / gcd(n, answer)
#     return answer


#땅따먹기 dp
#4열의 N행 배열이 주어질때 N행까지의 최대값을 구하여라
#같은열은 연속으로 선택할수없다.
land=[[1,2,3,5],[5,6,7,8],[4,3,2,1]]
def solution(land):
    for i in range(len(land)-1):
        land[i+1][0]+=max(land[i][1],land[i][2],land[i][3])
        land[i+1][1]+=max(land[i][0],land[i][2],land[i][3])
        land[i+1][2]+=max(land[i][0],land[i][1],land[i][3])
        land[i+1][3]+=max(land[i][0],land[i][1],land[i][2])
    
    return max(land[len(land)-1])
print(solution(land)) #16



#최솟값 만들기 dp
#길이가 같은 두개의 배열이 주어진다
#A,B에서 각각 한개의숫자를 뽑아 곱한다
#곱한 수의 합이 최소가 되도록 만들자
A=[1, 4, 2]
B=[5, 4, 4]
def solution(A,B):
    n=len(A)
    A.sort()
    B.sort(reverse=True)
    dp=[0]*n
    for i in range(n):
        dp[i]=dp[i-1]+A[i]*B[i]
    return dp[n-1]
print(solution(A,B))


#행렬의 곱셈
#2차원배열 초기화
#2차원 배열의 곱을 구하여라(항상 계산할수 있게 나옴)
arr1=[[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2=[[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(len(arr2[0]))
def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr2[0]))] for i in range (len(arr1))]
    for i in range(len(arr1)): #3
        for j in range(len(arr2[0])):#열
            for k in range(len(arr1[0])):
                answer[i][j]+=arr1[i][k]*arr2[k][j]
    return answer
print(solution(arr1,arr2))


#피보나치수 dp
#n이 주어질때 n번째피보나치수를 구하여라
n=5
def solution(n):
    dp=[0]*(n+1)
    for i in range(n+1):
        if i==0:
            dp[i]=0
        elif i==1:
            dp[i]=1
        else :
            dp[i]=dp[i-2]+dp[i-1]
    return dp[n]%1234567
print(solution(n))



#JadenCase 문자열 만들기 join()
#JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
#문자열을 JadenCase로 바꾼 뒤 출력
s="  aa    a"
def solution(s):
    answer=""
    s=s.lower()
    s=s.split(" ")
    print(s)
    for i in range(len(s)):
        if s[i]!="":
            s[i]=s[i].replace(s[i][0],s[i][0].upper(),1)
    answer=" ".join(s)
    return answer
print(solution(s))
#추가 capitalize() 줜나쉽게풀림 ㄱ-
s="      aa a"
s=s.lower()
s=s.split(" ")
print(s)
for i in range(len(s)):
    s[i]=s[i].capitalize()
print(s)
answer=" ".join(s)
print(answer)


#숫자의 표현
#n이 주어질때 n이 연속된 숫자의 합으로 이루어질 수있다.
#이때 연속된 숫자의 합으로 이루어지는 개수를 구하여라
#n=9
#2 3 4
#4 5
#9
#3개
n=3
def solution(n):
    answer = 0
    c=0
    for i in range(1,n+1):
        sum=0
        for j in range(i,n+1):
            sum+=j
            if sum==n:
                c+=1
                break
            elif sum>n:
                break
    return c
print(solution(n))



#다음 큰 숫자 format() 2진수
#자연수 n이 주어진다
#n보다 크고 n을 2진수로 치환했을때 1의 개수가 같은 최소값을 구하여라
n=78
def solution(n):
    bin=format(n,'b')
    c=bin.count('1')#n의 1개수
    z=0
    while c!=z:
        n+=1
        bin=format(n,'b')
        z=bin.count('1')
    return n
print(solution(n))


#올바른 괄호
#괄호 형식이 올바르게 열리고 닫혔는지 구분하는 프로그램 완성
s="(()))("
def solution(s):
    c1=0
    c2=0
    if s[0]=="(":
        for i in range(len(s)):
            if s[i]=="(":
                c1+=1
            else :
                c2+=1
            if c1<c2:
                return False
        if c1==c2:
            return True
        else :
            return False
    else:
        return False
print(solution(s))
#-----------------------------------------------------LV3

# I 숫자 -> 큐에 숫자를 삽입함
# D 1 -> 큐에서 최대값 삭제
# D -1 -> 큐에서 최소값 삭제
# 큐가 비어있으면 [0,0], 비어있지않으면[최대값,최소값] 출력
#원소는 “명령어 데이터” 형식으로 주어집니다. 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
#빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.
operations=["I 7","D -1","D 1","I 5"]
queue=[]
answer=[0,0]
for i in range(len(operations)):
    c,n=operations[i].split()
    if c=='I':
        n=int(n)
        queue.append(n)
    elif c=='D':
        if len(queue)==0:
            continue
        n=int(n)
        if n==1:
            queue.remove(max(queue))
        if n==-1:
            queue.remove(min(queue))

if len(queue)==0:
    print(answer)
else:
    answer[0]=max(queue)
    answer[1]=min(queue)
    print(answer)