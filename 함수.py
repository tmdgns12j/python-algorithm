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