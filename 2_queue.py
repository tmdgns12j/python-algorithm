#큐 기본
#FIFO
#덱을 쓰는이유 : 리스트로 큐의 기능을 구현할 수도 있지만 시간복잡도가 덱이 더 좋음
from collections import deque
queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
print(queue)
queue.popleft()
print(queue)
queue.append(1)
queue.append(4)
print(queue)
queue.popleft()
print(queue)
queue.reverse()
print(queue)


#백준 2161 큐
#제일 위에카드를 버림, 그다음 제일위에 카드를 제일 아래로 옮김
#버린카드를 순서대로 출력
# 1 2 3 4 -> 1 3 2 4
# 1. 1~N장의 카드 주어짐
# 2. 버린카드 출력
#풀이 : 큐의 FIFO를 이용함
num=int(input()) # N 설정
a=[0]*num #1~N까지의 배열생성(카드 초기화시켜줄꺼임)
temp=[0]*num #버린키드를 담아둘 배열
for i in range(1,num+1) : #1~n으로 배열 초기화
    a[i-1]=int(i) # 1~N까지 카드로 초기화

for i in range(num) :
    temp[i]=a[0] #맨 윗카드를 버림
    a.pop(0)#버린거 배열에서 삭제
    if len(a) == 0 : break #배열에 값이 하나도없다면 끝냄
    a.append(a[0]) #맨 윗카드를 뒤로복사
    a.pop(0)#옮긴카드 삭제

for i in range(num) :
    print(temp[i],end=" ")

#백준1158
n,k=input().split()
n=int(n)
k=int(k)
a=[0]*n
temp=[0]*n
count=int(0)
j=int(0)
for i in range(n) :
    a[i]=i+1
i=int(0)
while(j!=n) :
    if a[i] != 0 :
        count+=1
        if count==k :
            temp[j]=a[i]
            j+=1
            a[i]=0
            count=0
    i+=1
    if i==len(a) :
        i=0
print('<',end='')
for i in range(n) :
    if i==n-1 :
        print(str(temp[i])+'>')
    else :
        print(temp[i],end=", ")


#LV2짝지어 제거하기 큐 deque queue
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