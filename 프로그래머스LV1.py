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


#같은숫자는 싫어
#배열이 주어질때 연속적으로나타나는 숫자는 하나만남긴다
#0~9정수
arr=[1,1,3,3,0,1,1]
def solution(arr):
    answer=[]
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            arr[i-1]=-1
    for i in range(len(arr)):
        if arr[i]!=-1:
            answer.append(arr[i])   
    return answer
print(solution(arr))
#[1, 3, 0, 1]

#2016년
#2016년의 달과 일을 입력하면 해당하는 요일 출력
#2016년은 윤년
a=5
b=24
def solution(a, b):
    mon=[31,29,31,30,31,30,31,31,30,31,30,31]
    day=['FRI','SAT','SUN','MON','TUE','WED','THU']
    sum=0
    for i in range(a-1): #4
        sum+=mon[i]
    d=(sum+b)%7
    answer=day[d-1]
    return answer
print(solution(a,b))
#TUE


#가운데 글자 가져오기
#문자열이 주어질때 가운데 문자를 출력
#짝수는 두개
s="abcde"
def solution(s):
    c=len(s)
    answer=''
    if c%2!=0:
        answer=s[len(s)//2]
    else:
        answer=s[len(s)//2-1]+s[len(s)//2]
    return answer
print(solution(s))
#c


#나누어 떨어지는숫자배열
#나누어 떨어지는 숫자를 출력
#없다면 배열에 -1을 담아 출력
arr=[5, 9, 7, 10]
divisor=5
def solution(arr, divisor):
    answer = []
    c=0
    for i in range(len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
            c=c+1
    if c==0:
        answer.append(-1)
        return answer
    answer.sort()
    return answer
print(solution(arr,divisor))
#5,10



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



#크레인 인형뽑기 게임
#게임(board)이 주어지고 인형의 종류가 숫자로 표현되어있다
#크레인의 명령(moves)가 주어진다
#크레인이 명령에 따라 해당하는 인형을 바구니에 옮긴다
#이웃하는 인형의 종류가 같으면 사라질때 사라진 인형의 개수를 구하여라
#딱봐도 스택구조 문제임 쉬움
board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
# [0,0,0,0,0]
# [0,0,1,0,3]
# [0,2,5,0,1]
# [4,2,4,4,2]
# [3,5,1,3,1]
def solution(board, moves):
    new=[0]
    score=0
    for i in moves:
        for j in range(len(board)):
            test1=board[j][i-1]
            if board[j][i-1]!=0:# 4찾음
                test2=new[-1:]
                if test2[-1]==board[j][i-1]: #쌓인거랑 뽑은거랑 같으면
                    new.pop()
                    board[j][i-1]=0
                    score+=2
                    break
                else :
                    new.append(board[j][i-1])
                    board[j][i-1]=0
                    break
    return score
print(solution(board, moves))



#없는숫자더하기
#숫자(numbers)가 주어질때 0~9까지숫자중 없는숫자를 더하여라
numbers=[1,2,3,4,6,7,8,0]
def solution(numbers):
    numbers.sort()
    arr=[0,1,2,3,4,5,6,7,8,9]
    sum=0
    for i in arr:
        if i not in numbers:
            sum+=i
    return sum
print(solution(numbers))



#포켓몬
#여러 종류의 포켓몬(nums)이 주어진다
#포켓몬은 N/2마리를 가져갈수있을때
#최대한 여러종류의 포켓몬을 가져가자
#포켓몬 종류의 수를 구하여라
nums=[1,2,3,4,5,6]
def solution(nums):
    choice=len(nums)//2
    temp=[]
    c=0#리턴값
    nums.sort()
    for i in nums:
        if i not in temp:
            temp.append(i)
            c+=1
            choice-=1
        if choice==0:
            break
    return c
print(solution(nums))



#약수의 개수와 덧셈
#left right가 주어진다
#left에서 right까지 약수의 개수가 짝수면 더하고 홀수면 뺀다
#이때 합을 구하자
left=13
right=17
def solution(left, right):
    sum=0
    for i in range(left,right+1):
        e=left
        if e**0.5%1==0:#제곱수면
            sum-=e
            left+=1
        else :
            sum+=e
            left+=1
    return sum
print(solution(left, right)) #43




#3진법 뒤집기
#자연수n이 주어질때 3진법으로 변환하고 앞뒤로 뒤집은 후
#다시 10진법으로 표현하여라
#진법,진수변환 int()
n=125
def solution(n):
    arr=[]
    number=""
    sum=0
    while n>0:          #3진수로 변환
        arr.append(n%3)
        n=n//3
    number=list(map(str,arr))
    answer="".join(number)
    answer=int(answer)
    answer=str(answer)
    l=len(answer)
    answer=int(answer)
    print(answer)#22111
    for i in range(1,l+1):# 1,2
        sum=sum+answer%(10**1)*(3**(i-1))
        answer=answer//10
    return sum

#다른풀이
#진법,진수변환 int()
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)#3진법 변환
    return answer
print(solution(n))



#예산
#부서별 신청한 지원금(d)과 예산(budget)이 주어진다
#이때 지원할수있는 부서의수를 구하여라(최대)
d=[2,2,3,3]
budget=10
def solution(d, budget):
    d.sort() #1 2 3 4 5
    result=0
    for i in d:
        budget-=i
        if budget<0:
            break
        else:
            result+=1
    return result
print(solution(d,budget))



#비밀지도
#zfill() str에 사용 가능하며 왼쪽을 0으로 채워줌
n=6
arr1=[46, 33, 33 ,22, 31, 50]
arr2=[27 ,56, 19, 14, 14, 10]
def solution(n, arr1, arr2):
    arr=[]
    num=0
    for i in range(n):
        num=arr1[i]|arr2[i]
        bin=format(num,'b')#str
        bin=bin.zfill(n)
        temp=bin.replace('1','#')
        temp=temp.replace('0',' ')
        arr.append(temp)
    return arr
print(solution(n,arr1,arr2))




#두 개 뽑아서 더하기
#정수 배열이 주어진다
#서로다른 위치에있는 두 수를 뽑아 더해서 만들수있는 모든 수를 배열에 오름차순으로 담아 출력
numbers=[5,0,2,7]
def solution(numbers):
    arr=set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j:
                temp=numbers[i]+numbers[j]
                arr.add(temp)
            else:
                break
    arr=list(arr)
    arr.sort()
    return arr 
print(solution(numbers))



#다트게임
dartResult="1S*2T*3S"
def solution(dartResult):
    dartResult=dartResult.replace('10','N')
    arr=[]
    sum=0
    for i in dartResult:
        c=0
        if i.isdigit():
            i=int(i)
            arr.append(i)
        elif i=='N':
            i=10
            arr.append(i)
        elif i=='S':
            arr[-1]=arr[-1]**1
        elif i=='D':
            arr[-1]=arr[-1]**2
        elif i=='T':
            arr[-1]=arr[-1]**3
        elif i=='*':
            for j in range(len(arr)-1,-1,-1):#2 3
                arr[j]=arr[j]*2
                c+=1
                if c==2:
                    break
        elif i=='#':
            arr[-1]=-arr[-1]
    for i in arr:
        sum+=i
    return sum
print(solution(dartResult))


#부족한 금액 계산하기
#놀이기구의 가격(price) 소지한금액(money) 타고싶은횟수(count)가 주어진다
#가격은 n번째 이용한다면 이용료의n배를 받는다
#3 6 9 12...
#모자라는 금액을 구하고 모자라지않으면 0을 리턴
price=3
money=20
count=4
def solution(price, money, count):
    sum=0
    for i in range(1,count+1):
        sum+=price*i
    result=sum-money
    if money>=sum:
        return 0
    return result
print(solution(price, money, count))


#문자열과 n이 주어질때
#각 문자열의 n번째 문자로 정렬한다
#n문자가 같을때는 사전순으로 정렬
strings=["sun", "bed", "car"]
n=1
def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x:x[n])
print(solution(strings,n))



#문자열 내림차순으로 배치하기
#주어진 문자열을 내림차순으로 정렬하여라
#join()
s="Zbcdefg"
def solution(s):
    s=list(s)
    s.sort(reverse=True)
    answer="".join(s)
    return answer
print(solution(s))


#문자열다루기 기본 isdigit(), isnum()
#문자열의 길이가 4또는6이고 숫자로만 구성되어있는지 확인하는 함수 작성
def solution(s):
    if (len(s)==4 or len(s)==6) and s.isdigit():
        return True
    else:
        return False


#서울에서 김서방찾기
#배열이 주어질때 Kim의 위치를 찾아라
seoul=["Jane", "Kim"]
def solution(seoul):
    num=seoul.index('Kim')
    return"김서방은 %d에 있다" % num
print(solution(seoul))


#수박수박수박수?
#n이 주어질때 수박패턴을 유지하여 출력
#n=3 수박수   n=4 수박수박
n=3
def solution(n):
    arr=['수','박']
    new=[]
    if n%2==0:
        return "수박"*(n//2)
    else:
        for i in range(n):
            new.append(arr[i%2])
        return "".join(new)
print(solution(n))


#문자열을 정수로바꾸기
s="-1234"
def solution(s):
    return int(s)
print(solution(s))


#약수의합
n=12
def solution(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=i
    return sum
print(solution(n))



#이상한 문자 만들기
#문자열s가 주어진다
#단어의 짝수번째 알파벳은 대문자 홀수번째는 소문자로 출력한다
s="try  h"
def solution(s):
    new=[]
    s=list(s)
    c=0
    check=0
    for i in s:
        if i==" ":
            check=0
            new.append(i)
        elif check%2==0: #짝수면
            i=i.upper()
            s[c]='1'
            new.append(i)
            check+=1
        else:
            i=i.lower()
            s[c]='1'
            new.append(i)
            check+=1
        c+=1
    return "".join(new)
print(solution(s))


#자릿수더하기
N=987
def solution(N):
    N=str(N)
    N=list(N)
    sum=0
    for i in N:
        i=int(i)
        sum+=i
    return sum
print(solution(N))


#자연수 뒤집어 배열로 만들기
n=12345
def solution(n):
    n=str(n)
    n=list(n)
    new=[]
    for i in range(len(n)-1,-1,-1):
        new.append(int(n[i]))
    return new
print(solution(n))


#정수 내림차순으로 배치하기
n=12345
def solution(n):
    n=str(n)
    n=list(n)
    n.sort(reverse=True)
    s=""
    for i in n:
        s+=i
    return int(s)
print(solution(n))


#정수 제곱근 판별
#sqrt()루트함수, pow() n제곱 함수
import math
n=122
def solution(n):
    sqrt=math.sqrt(n)
    if sqrt%1==0:
        return int(pow(sqrt+1,2))
    else:
        return -1
print(solution(n))


#제일 작은 수 제거하기
arr=[4,3,2,1]
def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0 or arr==[10]:
        arr = [-1]
    return arr
print(solution(arr))


#최대공약수와 최소공배수
#gcd()최대공약수
#lcm()최대공약수 3.9부터 가능하다함
import math
n=6
m=9
def solution(n, m):
    if math.gcd(n,m)==1:
        return [1,n*m]
    else:
        return [math.gcd(n,m),n*m//math.gcd(n,m)]
print(solution(n, m))


#콜라츠 추측
num=626331
def solution(num):
    c=0
    while num!=1:
        if num%2==0:
            num=num//2
        else:
            num=num*3+1
        c+=1
        if c==500:
            return -1
    return c
print(solution(num))


#평균 구하기
arr=[1,2,3,4]
def solution(arr):
    sum=0
    for i in arr:
        sum+=i
    avg=sum/len(arr)
    return avg
print(solution(arr))


#하샤드수
x=10
def solution(x):
    temp=list(str(x))
    sum=0
    for i in temp:
        i=int(i)
        sum+=i
    if x%sum==0:
        return True
    else:
        return False
print(solution(x))


#핸드폰 번호 가리기
phone_number="01033334444"
def solution(phone_number):
    phone_number=list(phone_number)
    for i in range(len(phone_number)-5,-1,-1):
        phone_number[i]='*'
    return "".join(phone_number)
print(solution(phone_number))


#행렬의 덧셈
arr1=[[1,2],[2,3]]
arr2=[[3,4],[5,6]]
def solution(arr1, arr2):
    answer=[[0 for i in range(len(arr1[0]))] for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j]=arr1[i][j]+arr2[i][j]
    return answer
print(solution(arr1, arr2))
#다른풀이
#numpy tolist()
#그냥하는게 훨~~~~~~~~~씬 빠름 비추
import numpy as np
def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()

#x만큼 간격이 있는 n개의 숫자
x=-4
n=2
def solution(x, n):
    answer=[]
    temp=0
    for i in range(1,n+1):
        temp=x*i
        answer.append(temp)
    return answer
print(solution(x, n))