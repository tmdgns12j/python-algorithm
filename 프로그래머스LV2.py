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


#스킬트리 for else
#선행스킬이 주어질때 스킬트리에 정해진 순서대로 찍어야한다.
#가능한 스킬트리의 개수를 출력
skill="CBD"
skill_trees=["BACDE", "CBADF", "AECB", "BDA","CBAD","CBD"]
def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees :
        skills=list(skill)
        for s in i:
            if s in skills:
                if s!= skills.pop(0):
                    break
        else:
            answer+=1
    return answer
print(solution(skill, skill_trees))
#4


#구명보트
#사람들의 몸무게와 구명보트의 최대 kg이 주어진다
#2명씩밖에 탈수없다
#필요한구명보트의 최소수를 구하자
from collections import deque
people=[40,70, 50, 80, 50]
limit=220
def solution(people, limit):
    c=0
    people.sort()
    q=deque(people)
    while len(q)>=1:
        if len(q)==1:
            c+=1
            break
        if q[0]+q[-1]<=limit:
            q.pop()
            q.popleft()
            c+=1
        else:
            q.pop()
            c+=1
    return c
print(solution(people, limit))



#기능개발
#진행도와 진행속도가 주어진다
#배포는 하루의 끝에 이루어지고 배포는 순차적으로 이루어질때
#각 배포마다 몇개의 기능이 배포되는지 출력
#[2,4]
#완성되는데의 날짜를 계산후 그 특성을 이용해 출력해도 상관없을듯
from collections import deque
progresses=[93, 30, 55, 60, 40, 65]
speeds=    [1, 30, 5, 10, 60, 7]
def solution(progresses, speeds):
    answer=[]
    queue=deque(progresses)
    squeue=deque(speeds)
    while queue:
        check=0
        for i in range(len(queue)):
            if queue[i]<100:
                queue[i]+=squeue[i]
        for i in range(len(queue)):
            if queue[0]>=100 :
                queue.popleft()
                squeue.popleft()
                check+=1
            else:
                break
        if check!=0:
            answer.append(check)
    return answer
print(solution(progresses, speeds))


#더 맵게, 힙 heap() heapq() heapify(), heappush()
#음식의 스코빌지수가 주어진다
#모든 음식의 지수를 K이상으로 만들때 필요한 횟수를 구하여라
#불가능하면 -1 출력
#섞은 음식의 지수 = 가장 맵지않은 음식 지수+(두번째로 맵지않은 지수 * 2)
#우선순위큐 가능하지않을까
import heapq
scoville=[1,2]
K=3
def solution(scoville, K):
    heapq.heapify(scoville)#힙으로 변경
    check=0
    answer=0
    for i in scoville:#초기부터 K를 넘을때 처리
        if i>=K:
            check+=1
    if check==len(scoville):
        return 0
    check=0
    while check!=len(scoville):
        c1=heapq.heappop(scoville)#가장 작은값을 빼줌
        c2=heapq.heappop(scoville)
        new=c1+c2*2
        heapq.heappush(scoville, new)
        answer+=1
        for i in scoville:
            if i>=K:
                check+=1
            else:
                check=0
                break
        if check==len(scoville):
            return answer
        elif len(scoville)==1:
            return -1
print(solution(scoville, K))



#타겟넘버 recursion 재귀, dfs
#숫자들이 주어진다
#이 숫자들을 적절히 더하거나 빼서 타겟넘버를 만들고
#가능한 방법의 수를 출력하라
numbers=[1, 1, 1, 1, 1]
target=3
answer=0
def solution(numbers, target):
    def dfs(i,number,sum):
        global answer
        sum+=number
        if i==len(numbers)-1:
            if sum==target:
                answer+=1
        else:
            dfs(i+1,numbers[i+1],sum)
            dfs(i+1,-numbers[i+1],sum)
    sum=0
    dfs(0,numbers[0],sum)
    dfs(0,-numbers[0],sum)
    return answer
print(solution(numbers, target))


#짝지어 제거하기 큐 deque queue
#문자열이 주어질때 연속하는 두개의문자를 제거한다
#전부다 지워지면 1출력 그렇지않으면 0출력
from collections import deque
s="baabaa"
def solution(s):
    queue=deque()
    queue.append(s[0])
    for i in range(1,len(s)):
        queue.append(s[i])
        if len(queue)<2:
            pass
        elif queue[-1]==queue[-2]:
            queue.pop()
            queue.pop()
    if len(queue)==0:
        return 1
    else:
        return 0
print(solution(s))



#가장 큰 수 lambda 람다식
#수가 주어질때 숫자를 조합하여 가장 큰 수를 만들어라
#풀이 : numbers원소는 1000이하, 문자열비교 사용
#문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교합니다. 물론 같으면, 다음 인덱스도 비교합니다. 비교한 결과 [6, 2, 10]의 순으로 정렬됩니다.
numbers=[40,404]
def solution(numbers):
    new=[]
    if numbers.count(0)==len(numbers):
        return str(0)
    numbers=list(map(str,numbers))
    new=sorted(numbers,key=lambda x:x*3,reverse=True)#1000이하라 자리수 맞춰줌666 616161, 아스키코드로 차례대로 비교
    return "".join(new)
print(solution(numbers))
#실패한풀이 dict()사용
# def solution(numbers):
#     numbers.sort()
#     print(numbers)
#     arr={}
#     new=[]
#     for i in numbers:
#         arr[i]=i//(10**(len(str(i))-1))
#     arr=sorted(arr, key=lambda x:arr[x],reverse=True)
#     for i in arr:
#         i=str(i)
#         new.append(i)
#     return "".join(new)
# print(solution(numbers))


#프린터
#문서의 중요도가 순서대로 담긴배열(priority)이 주어진다
#숫자가 클수록 중요함
#location은 인쇠를 요청한 문서의 위치
#location이 몇번째로 인쇄되는지 출력
from collections import deque
priorities=[1, 1, 9, 1, 1, 1]
location=0
def solution(priorities, location):
    queue=deque(priorities)
    arr=[i for i in range(len(priorities))]
    arr=deque(arr)
    count=0
    while queue:
        m=max(queue)
        temp1=queue.popleft()
        temp2=arr.popleft()
        if temp1==m:
            count+=1
            if temp2==location:
                return count
        else:
            queue.append(temp1)
            arr.append(temp2)
print(solution(priorities, location))
#다른풀이 any()
# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer


#소수찾기 set() permutation() 조합 경우의수
#에라토스테네스의 체 참고
#한자리 숫자가 적힌 종이조각들이 들어있다
#종이를 붙여 소수를 몇개 만들수있는지 출력
from itertools import permutations
numbers="17"
def solution(numbers):
    new=set()
    answer=[]
    numbers=list(numbers)
    for i in numbers:
        new.add(int(i))
    for i in range(2,len(numbers)+1):
        per=list(permutations(numbers,i))
        for i in per:
            i=int("".join(i))
            new.add(i)
    if 0 in new:
        new.remove(0)
    if 1 in new:
        new.remove(1)
    answer=len(new)
    for i in new:
        for j in range(2,i//2+1):
            if i%j==0:
                answer-=1
                break
    return answer
print(solution(numbers))


#주식가격
#초 단위로 기록된 주식가격이 주어진다
#가격이 떨어지지않은기간이 몇초인지 구하자
prices=[1,2,3,2,3]
def solution(prices):
    dp=[0]*len(prices)
    for i in range(len(prices)):
        for j in range(i,len(prices)-1):
            if prices[i]<=prices[j]:
                dp[i]+=1
            else:
                break
    return dp
print(solution(prices))


#오픈채팅방 dict()
#들어오고 나간 사람을 바뀐이름으로 화면에 출력
#풀이 : 아이디에 해당하는 닉네임을 저장한뒤 그걸 가져옴
record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(record):
    answer=[]
    db=dict()
    for i in range(len(record)):
        record[i]=record[i].split()
        if record[i][0]=="Leave":
            continue
        db[record[i][1]]=record[i][2]
    for i in range(len(record)):
        if record[i][0]=="Enter":
            answer.append("%s님이 들어왔습니다." %db[record[i][1]])
        elif record[i][0]=="Leave":
            answer.append("%s님이 나갔습니다." %db[record[i][1]])
    return answer
print(solution(record))

#첫 풀이 : 아이디에 해당하는 닉네임을 전부 찾아 바꾸고 출력함
# 굳이 바꿔줄 필요가 없었음(시간초과)
record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(record):
    answer=[]
    for i in range(len(record)):
        record[i]=record[i].split()
        if "Leave"==record[i][0]:
            record[i].append('0')
    for i in range(len(record)-1,-1,-1):
        id=record[i][1]
        name=record[i][2]
        if "Change"==record[i][0]:
            for j in range(len(record)):
                if record[j][1]==id:
                    record[j][2]=name
                if record[j][0]=="Change":
                    record[j][0]='0'
        elif "Enter"==record[i][0]:
            for j in range(len(record)):
                if record[j][1]==id:
                    record[j][2]=name
    for a,b,c in record:
        if a=="Enter":
            answer.append("%s님이 들어왔습니다." %c)
        elif a=="Leave":
            answer.append("%s님이 나갔습니다." %c)
    return answer
print(solution(record))



#수식 최대화 abs() isdigit() eval()(문자열을 수식으로 계산해줌) permutation()
#풀이 : 너무복잡했음
# 1. 숫자와 부호를 두개의 배열로 나눔
# 2. 등호의 경우의수 리스트로 생성(permutation)
# 3. 3중for 돌려주면서 결과값 dp에 저장

from itertools import permutations
expression="100-200*300-500+20"
def solution(expression):
    cal=[]
    num=expression
    for i in range(len(expression)):
        if expression[i].isdigit():
            continue
        else:
            cal.append(expression[i])
            num=num.replace(expression[i],' ')
    num=num.split()
    # print(num)
    # print(cal)
    new=['-','+','*']
    new=list(permutations(new,3))
    dp=[0]*len(new)
    # print(new)
    for i in range(len(new)):
        # print('dp=',dp)
        copynum=list(num)
        copycal=list(cal)
        for j in range(len(new[0])):
            k=0
            while 1:# for j in range(len(cal)):
                if k>=len(copycal):
                    break
                if new[i][j]==copycal[k]:
                    copynum[k]=str(eval(copynum[k]+copycal[k]+copynum[k+1]))
                    copynum.pop(k+1)
                    copycal.pop(copycal.index(copycal[k]))
                    # print(copynum)
                    dp[i]=abs(int(copynum[k]))
                    k=0
                    continue
                k+=1
    return max(dp)
print(solution(expression))


# H-Index
#논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index
#정렬보다는 greedy에 가까운듯..
# 풀이 : h번 이상 인용된 논문이 h편 이상만 잘 짜면됨
citations=[1,4]
def solution(citations):
    citations.sort() #최적화를 위한 정렬
    answer=0
    for i in range(max(citations)+1): #논문이 인용된 횟수의 최대값
        count=0
        for j in citations:
            if j>=i: # j번 인용된 논문이 i번보다 클때
                count+=1
        if count>=i: # i번이상 인용된 논문이 i편이상일때
            answer=i
    return answer
print(solution(citations))
#다른풀이 이해불가;
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


#못품X
#가장 큰 정사각형 찾기
#dp(i,j까지의 정사각형 최대 길이)
#풀이 : 1,1부터 왼쪽, 위쪽, 좌상, 을 확인
#모두 1이면 변의길이를 i,j에 +1해준다
board=[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
def solution(board):
    answer=board[0][0]
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]==1:
                board[i][j]=min(board[i-1][j-1],board[i-1][j],board[i][j-1])+1
                answer=max(answer,board[i][j])
    return answer**2
print(solution(board))



#큰 수 만들기
#number이 주어질때 k개의 숫자를 지워 최대값을 만들지
#풀이 : 9999인 경우를 따로 처리해주는 생각을 해야함
#처음에는 number에서 사용한건0으로 바꾸었지만 시간초과
#사용한 데이터는 꼭 삭제해야 시간초과가 걸리자않음
number="4177252841"
k=4
def solution(number, k):
    l=len(number)
    answer=""
    start=0
    finish=k+1
    for i in range(l-k):
        new=number[0:finish]
        if '9' in new:
            answer+='9'
            start=number.index('9')+1
        else:
            m=max(new)
            answer+=m
            start=number.index(m)+1
        number=number.replace(number[0:start],'',1)
        finish=finish-start+1
    return answer
print(solution(number, k))
# number="1231234"
# k=3
# def solution(number, k):
#     l=len(number)
#     answer=""
#     start=0
#     s=0
#     for i in range(l-k):
#         new=number[start:k+1+i]
#         if '9' in new:
#             answer+='9'
#             start=number.index('9')+1
#         else:
#             m=max(new)
#             answer+=m
#             start=number.index(m)+1
#         number=number.replace(number[s:start],'0'*(start-s),1)
#         s=start
#     return answer
# print(solution(number, k))



#카펫 약수구하기, 제곱근구하기 sqrt()
#brown과 yellow(중앙)의 개수가 주어질때 카펫의 가로세로를 구하여라
#그리디같음
#규칙만 찾아주면됨
import math
brown=8
yellow=1
def solution(brown, yellow):
    h=0
    arr=[]#yellow의 약수들어갈곳
    sqrt=int(math.sqrt(yellow))
    for i in range(1,sqrt+1): #약수구하기
        if yellow%i==0:
            arr.append(yellow//i)
    print(arr)
    for i in arr: #핵심
        if(brown+yellow)%(i+2)==0: #너비%가로==0 이면 세로를 구할수있음
            h=(brown+yellow)//(i+2)
    return [(brown+yellow)//h,h]
print(solution(brown, yellow))
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