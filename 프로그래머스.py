#대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
#예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다
def solution(s):
    s=str(s)
    s=s.lower()
    pcount=int(0)
    ycount=int(0)
    for i in range(len(s)) :
        if s[i]=='p' : pcount+=1
        if s[i]=='y' : ycount+=1
    if pcount==ycount :
        return True
    else :
        return False

#함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

def solution(x, n):
    answer=[0]*n
    i=int(0)
    if x>0 :
        for x in range(x,n*x+1,x) :
            if i==n : break
            answer[i]=x
            i+=1
    else :
        for x in range(x,n*x-1,x) :
            if i==n : break
            answer[i]=x
            i+=1
    return answer

#정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요
def solution(arr):
    answer = 0
    answer = sum(arr)/len(arr)
    return answer

#음양더하기
#정수와 부호가 각각 주어질때 이들의 합을 구하라
absolutes=[4,7,12]
signs=[True,False,True]
def solution(absolutes, signs):
    answer=0
    for i in range(len(absolutes)):
        if signs[i]==True:
            pass
        else:
            absolutes[i]=-absolutes[i]
        answer+=absolutes[i]
    return answer
print(solution(absolutes,signs))


#내적
#a,b가 주어질때 a[0]*b[0]+..a[n]*b[n]구하여라
a=[1,2,3,4]
b=[-3,-1,0,2]
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer+=a[i]*b[i]
    return answer
# def solution(a, b):
#     answer = 0
#     for x, y in zip(a,b):
#         answer += x*y
#     return answer
print(solution(a,b))


#K번째수
# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.
array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
def solution(array, commands):
    answer = []
    for start,end,k in commands:
        r=array[start-1:end]
        r.sort()
        answer.append(r[k-1])   
    return answer
print(solution(array,commands))



#2016년(윤년)
# 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.
def solution(a, b):
    sum=int(0)
    day=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    date=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1) : 
        sum+=date[i]
    sum=sum+b
    sum=sum%7
    return day[sum-1]


#체육복
#전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
#체육수업을 들을 수 있는 학생의 최댓값을 return
#도난학생 1이상 여벌체육복학생 1이상, 여벌이있는경우만 빌려줄수있음
#앞뒤+1로만 빌려줄수있음
#정렬을 해주면 더 큰 기대값을 얻을수있어서 테케13번 정렬해주면 맞게됨
n=5
lost=[2,4]
reserve=[3,1]
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    r=len(reserve)
    copy=list(lost)
    answer = 0
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            copy.remove(i)
    lost=list(copy)
    for i in lost:#copy
        if i-1 in reserve:
            copy.remove(i)
            reserve.remove(i-1)
        elif i+1 in reserve:
            copy.remove(i)
            reserve.remove(i+1)
    answer=n-len(copy)
    return answer
print(solution(n, lost, reserve))



#소수찾기, 에라토스테네스의 체, set()
#1~n까지의 소수개수를 구하여라
#n=2이상  1000000이하
#효율성문제
#이중포문 O(N^2)이여서 틀렸었음
n=10
def solution(n):
    answer = 0
    #set()을 쓴 이유는 차집합 해주려고
    arr=set([i for i in range(3,n+1,2)]) #2의배수를 빼고 생성해줌
    #print(arr)
    for i in range(3,n+1,2): #홀수
        if i in arr:
            arr-=set([i for i in range(i*2,n+1,i)])#해당 홀수의 다음배수부터 삭제 3이면 6부터 9 12...
    #print(arr)
    answer=len(arr)+1#2포함시켜줘야함
    return answer
print(solution(n))



#소수만들기 combination, 조합
#숫자nums가 주어질때 숫자 3개의 합이 소수가 되는 경우의 수를 구하여라
from itertools import combinations
nums=[1,2,3,4]
def check(temp):#6
    for i in range(2,temp):
        if temp%i==0:
            return False
    return True
def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    for i in range(len(combi)):
        temp=sum(combi[i])
        if check(temp):
            answer+=1
    return answer
print(solution(nums))



#실패율 딕셔너리 dict() {}, sorted(), lambda
# N은 존재하는스테이지, stages는 각각 도전중인 스테이지를 의미
# 실패율은 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 실패율이 높은 스테이지를 내림차순으로 출력
#풀이 : 딕셔너리를 사용하여 쉽게 풀수있음
#접근방법은 비슷하지만 키와 값을 동시에 초기화를 못했음
N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]
def solution(N, stages):
    result={}
    challenge=len(stages)
    for stage in range(1,N+1):
        if challenge !=0:
            count = stages.count(stage)
            result[stage]=count/challenge
            challenge-=count
        else:
            result[stage]=0
    return sorted(result, key=lambda x:result[x],reverse=True)
# def solution(N, stages):
#     answer = []
#     l=len(stages)
#     temp=0
#     fail=[0]*(N+2)
#     for i in stages:
#         fail[i]+=1
#     print(fail)
#     for i in range(1,len(fail)): #8
#         temp=fail[i]
#         fail[i]=fail[i]/l
#         l-=temp
#     print(fail)
#     x=dict.fromkeys(fail)
#     print(x)
#     c=0
#     for i in fail:
#         x[i]=c
#         c+=1
#     print(x)
#     return answer
print(solution(N,stages))




#완주하지 못한선수 zip()
#참가자와 완주자가 주어지고 1명의참가자빼고 모두 완주를한다.
#미 완주자를 출력하자
#1명만 남는 특징을 이용해아함
participant=["marina", "josipa", "nikola", "ana", "filipa"]
completion=["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for a,b in zip(participant, completion):
        if a != b:
            return a
    return participant.pop()
print(solution(participant,completion))


#모의고사
#수포자 3명이 각각arr1,arr2,arr3과 같이 찍을때 가장 많이맞춘 방법을 출력
#오름차순이고 맞춘 문제수가 같을때 모두 출력
answers=[5, 5, 5, 1, 4, 1]
def solution(answers):
    arr1=[1,2,3,4,5]
    arr2=[2,1,2,3,2,4,2,5]
    arr3=[3,3,1,1,2,2,4,4,5,5]
    c1=0
    c2=0
    c3=0
    answer = []
    for i in range(len(answers)):
        if arr1[i%5]==answers[i]:
            c1+=1
        if arr2[i%8]==answers[i]:
            c2+=1
        if arr3[i%10]==answers[i]:
            c3+=1
    result=[c1,c2,c3]
    print(result)
    for index, value in enumerate(result):
        if value==max(result):
            answer.append(index+1)
    answer.sort()
    return answer
print(solution(answers))




#신규 아이디 추천
import re
s=".abcdefghijklmn.p"
s=s.lower()#1
for i in s:     #2
    if not i.isalpha() and not i.isdigit() and i!='_' and i!='.' and i!='-':
        s=s.replace(i,'')
s=re.sub('\.\.*','.',s) #3
for i in range(2):
    s=re.sub('^\.|\.$','',s)    #4
    if len(s)==0:   #5
        s='a'
    if len(s)>=16:  #6
        s=s[:15]
    if len(s)<=2:   #7
        s+=s[len(s)-1]*(3-(len(s)))



#로또의 최고순위와 최저순위
from collections import Counter
lottos=[1,2,3,5,12,13]
win_nums=[11, 10, 4, 6, 7, 9]
c=0
def solution(lottos, win_nums):
    win_nums.sort()
    start=0
    end=len(lottos)-1
    answer=[]
    max=0
    min=0
    def binary(start,end,i):
        global c
        mid=(start+end)//2
        if start>end:
            return 0
        if win_nums[mid] == i:
            c+=1
        elif win_nums[mid]> i:
            binary(start,mid-1,i)
        else:
            binary(mid+1,end,i)
    
    for i in lottos:
        binary(start,end,i)
    N=Counter(lottos)
    if N[0]+c==6:
        max=1
    elif N[0]+c==5:
        max=2
    elif N[0]+c==4:
        max=3
    elif N[0]+c==3:
        max=4
    elif N[0]+c==2:
        max=5
    else :
        max=6
    if c==6:
        min=1
    elif c==5:
        min=2
    elif c==4:
        min=3
    elif c==3:
        min=4
    elif c==2:
        min=5
    else:
        min=6
    answer=[max,min]
    return answer

print(solution(lottos,win_nums))



#숫자 문자열과 영단어
# "one4seveneight" -> 1478
s="one4seveneight"
def solution(s):
    number=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10):
        j=str(i)
        s=s.replace(number[i],j)

    answer = int(s)
    return answer
print(solution(s))

#-----------------------------------------------------Lv2

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