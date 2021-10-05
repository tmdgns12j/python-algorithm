#절대값 abs()
a=abs(-3)
print(a)

#첫째자리에서 반올림 함수 round()
a=round(1.331141)
print(a)

#최대값 max()
a=max(20,30,40,10)
print(a)

#str() 문자열로 변환
#str()은 각 글자를 배열에 한칸씩 넣어줌
#str(100) -> 1 0 0
a=100
a=str(a)
if a=="100" : #문자열인지 검증
    print(a)

#count() 갯수세기
a=int(input())
b=int(input())
c=int(input())
multi=a*b*c

for i in range(10) :
    list_multi=list(str(multi))
    print(list_multi.count(str(i)))

#sort()
family=[('정승훈',25,173),('정안',29,155),('아무개',33,158),('정무개',50,165)]
family.sort() # 첫번째 요소로 정렬됨
print(family)
family.sort(key = lambda x:x[1], reverse=True) #두번째 요소로 정렬 내림차순
print(family)

#sorted()
#sorted()를 써도 원래의 배열에는 구조변경이 없음
family=[('정승훈',25,173),('정안',29,155),('아무개',33,158),('정무개',50,165)]
sorted(family, key = lambda x:x[2])
print(sorted(family, key = lambda x:x[2]))
print(family)

#프로그래머스 LV1 실패율 참고 sorted(), lambda
N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]
def solution(N, stages):
    l=len(stages)
    result={}
    c=0
    for i in range(1,N+1):
        if l!=0:
            c=stages.count(i)
            result[i]=c/l
            l-=c
        else:
            result[i]=0
    print(result)               #그냥 출력시 키와 값 다나옴
    print(result[1])            #해당하는 값이나옴
    print(sorted(result))       #정렬시 키값만 출력됨
    return sorted(result, key=lambda x:result[x],reverse=True)
print(solution(N,stages))
# {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0.0}
# [1, 2, 3, 4, 5]
# 0.125
# [3, 4, 2, 1, 5]

#Counter() 개수
#백준 10816
#Counter()의 위치는 원소의 값이랑 일치한다.
#10원소의 개수는 N[10]
import sys
from collections import Counter
n = int(sys.stdin.readline().rstrip())
N=list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
M=list(map(int,sys.stdin.readline().split()))
cnt=0
N=Counter(N)
for i in M:
    print(N[i])


#zip()
#프로그래머스 LV1.내적 문제 참조
def solution(a, b):
    answer = 0
    for x, y in zip(a,b):
        answer += x*y
    return answer

#combinations(), 콤비, 조합
from itertools import combinations
arr=[1,2,3,4]
combi=list(combinations(arr,3))
print(combi)
#[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

#enumerate()
#배열의 인덱스값과 값을 불러올수있음
#프로그래머스 LV1 모의고사 참고
test = [1,2,3] 
for index, value in enumerate(test): 
    print(index,value)


#gcd()최대공약수
#LV2 N개의 최소공배수 참조
from fractions import gcd
def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer

#capitalize() 각 문자열의 앞글자를 대문자로 바꿔줌
s="      aa a"
s=s.lower()
s=s.split(" ")
print(s)
for i in range(len(s)):
    s[i]=s[i].capitalize()
print(s)
answer=" ".join(s)
print(answer)
#      Aa A

#title() 각 단어의 앞글자를 대문자로 바꿔줌
s="aa bb cc Dd rR"
s=s.title()
print(s)
#Aa Bb Cc Dd Rr

#LV2 다음 큰 숫자 참조
#2진법 치환 format(), 다른진법도 가능
n=4
bin=format(n,'b')#b는 binary의미 o, x 등등 가능
print(bin) #100


#LV1 3진법뒤집기 참조
#진법,진수변환 int()
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)#3진법 변환 ********
    return answer
print(solution(n))


#LV1 비밀지도
#str.zfill(n) str에 사용 가능하며 왼쪽을 n자리수만큼 0으로 채워줌
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



#문자열다루기 기본 isdigit(), isnum()
#문자열의 길이가 4또는6이고 숫자로만 구성되어있는지 확인하는 함수 작성
def solution(s):
    if (len(s)==4 or len(s)==6) and s.isdigit():
        return True
    else:
        return False



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


#LV2소수찾기 set() permutation() 조합 경우의수
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