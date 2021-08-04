#선택정렬 O(N^2)
# 1. 가장 앞부터 가장 뒤까지 탐색하면서 가장 작은값의위치(j)를 min_index에 저장
# 2. 가장 앞과 min_index를 교체
# 3. 반복
array=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index=i     #0부터 시작하기 위함
    for j in range(i+1,len(array)):     #1부터 끝까지(0부터 시작했으니까)
        if array[min_index]>array[j]:   #지금까지 작은값보다 탐색한값이 더 작으면
            min_index=j                 #탐색한값을 저장
    array[i], array[min_index] = array[min_index], array[i]     #스왑
print(array)

#삽입정렬 O(N)~O(N^2)
#정렬이 되어있을수록 줄어드는듯
# 1. n과 n-1을 비교
# 2. n이 더 작으면 n-1과 교체
# 3. 0번지 까지 반복 (5 7 9 0 -> 5 7 0 9 -> 5 0 7 9 -> 0 5 7 9)
# 4. 다음으로 이동
# 5. 반복
array=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):     #0부터 끝까지
    for j in range(i,0,-1):     #n부터 0까지 -1씩 탐색
        if array[j]< array[j-1]:    #n-1이 더 작으면
            array[j], array[j-1] = array[j-1],array[j]  #스왑
        else:   #바꿀필요가없으면 빠져나옴
            break
print(array)


#퀵정렬 O(NlogN)~O(N^2)
#일반적인 정렬 라이브러리방식


#계수정렬 데이터의개수N, 데이터(양수)중 최대값 K일때 O(N+K)
#공간복잡도도 O(N+K)라 공간복잡도가 ㅈㄴ구림
#데이터의 크기 범위가 제한되어 정수형태로 표현할 수 있을때 사용가능
#동일한값의 데이터가 여러번 등장할때 유리
array=[7,5,9,0,3,1,6,2,4,8]
count = [0]*(max(array)+1)#1부터 시작하기위해 크기+1
for i in range(len(array)):
    count[array[i]]+=1  # count에서 해당하는 배열의 위치 +1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')

#백준2750, 2751
#n개의 번호 받아서 정렬하기
#풀이 : 그냥 sort()씀
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(n):
    print(arr[i])

#백준11650
#2차원 좌표 정렬
# 1. 점의 개수 n 입력
# 2. n만큼 좌표 입력
# 3. 정렬후 출력
#풀이 : 처음에 출력형식오류? 로 틀렸다고나왔다
#end=' '때문에 뒤에 공백이 생겨 그런거같아서 출력 방법을 바꾸어 정답
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
    #arr[i].sort
arr.sort()

# for i in range(n):
#     print()
#     for j in range(2):
#         print(arr[i][j],end=' ')
for i in range(n):
    print(arr[i][0],arr[i][1])



#백준 10989
#계수정렬
#개수n을 입력받아 오름차순으로 정력
#시간제한 3초 메모리 8mb
#풀이 : 직접 비교하여 정렬하는 방법이아닌
#해당하는 값을 인덱스에 동일한 번호로 나온 횟수만큼 더해줌
#인덱스를 순차적으로 인덱스의 값만큼 출력
#pypy3는 메모리초과가 뜨지만 python으로 채점하면 맞았습니다가뜸(?)
# sys.stdout.write를쓰면 괜찮다는 이야기도있음
import sys
i = int(sys.stdin.readline())
num = [0]*10001
for _ in range(i):
    num[int(sys.stdin.readline())] += 1
for j in range(len(num)):
    if(num[j]>0):
       for f in range(num[j]):
           print(j)



#백준 1427
n=str(input())
arr=[]
for i in n:
    arr.append(int(i))
#print(arr)
arr.sort(reverse=True)
for i in range(len(arr)):
    print(arr[i],end='')


#백준 1026
n=int(input())
sum=int(0)
a=list(map(int,input().split()))
b=list(map(int,input().split()))

for i in range(n):
    sum+=max(b)*min(a)
    b.remove(max(b))
    a.remove(min(a))
print(sum)



#백준 1931 정렬,그리디, lambda
#n개의 회의 일정이 주어진다 회의실에 최대한 많은 회의를 잡자
#끝나는시간과 시작시간이 일치할수있음
# 1. 회의n개 입력
# 2. 회의 시작시간 끝시간 입력
# 3. 출력
#풀이 : 정렬문제에 있긴하지만 그리디에 더 가까워보임
#핵심은 시작시간으로 정렬후 끝나는시간으로 정렬하는것
#그래야 가장 많은 회의를 담을수있음
#난 생각못했음
import sys
input = sys.stdin.readline  #숙지할것
n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
#print(arr)
arr.sort()
arr.sort(key=lambda x:x[1])     #람다식도 숙지
#print(arr)

start=0
end=0
count=0
for time in arr:
    if time[0]>=start:
        start=time[1]
        count+=1
print(count)



#백준 1764
#듣도 못한 사람과 보도못한 사람이 주어진다 듣보를 구하자
# 1. 듣도(n) 보도(m) 못한 사람수 입력
# 2. 듣도못한사람 입력
# 3. 보도못한사람 입력
# 4. 듣보수와 사람 출력
#풀이 : 처음에는 일반적인 리스트로 풀었다 하지만 시간초과
#set을 사용한 교집합이 핵심
import sys
n,m=map(int,sys.stdin.readline().split())
nlisten=['']*n
nsee=['']*m

for i in range(n):
    nlisten[i]=sys.stdin.readline().rstrip()
for i in range(m):
    nsee[i]=sys.stdin.readline().rstrip()
s1 = set(nlisten)
s2 = set(nsee)
result=sorted(list(s1 & s2))

print(len(result))
for i in range(len(result)):
    print(result[i])
# n,m=map(int,input().split())
# nlisten=[]
# nsee=[]
# new=[]
# for i in range(n):
#     nlisten.append(input())

# for i in range(m):
#     nsee.append(input())

# for person in nlisten:
#     if person in nsee:
#         new.append(person)
# new.sort()
# print(len(new))
# for i in range(len(new)):
#     print(new[i])



#백준 1946 정렬,그리디
#서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다
# 1. 테스트케이스(t)수 입력
# 2. 성적수(n)입력
# 3. 서류심사성적 면접시험성적 입력
# 4. 신입사원 최대인원 출력
#풀이 : 생각보다 무난한문제
#정렬을 하면 규칙이보임
#처음에는 이중for문을 썼음 O(N^2)여서 시간초과가 뜬거같아 구성을바꿔 정답
import sys
t=int(sys.stdin.readline().rstrip())
k=0
for k in range(t):
    n=int(sys.stdin.readline().rstrip())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,sys.stdin.readline().split())))
    arr.sort()
    
    count=0
    min = arr[0][1]
    for i in range(1,n):
        if arr[i][1]<min:
            count+=1
            min=arr[i][1]
    print(count+1)
# import sys
# t=int(sys.stdin.readline().rstrip())
# k=0
# for k in range(t):
#     n=int(sys.stdin.readline().rstrip())
#     arr=[]
#     for i in range(n):
#         arr.append(list(map(int,sys.stdin.readline().split())))
#     arr.sort(reverse=True)

#     ncount=0
#     j=0
#     for seq in arr:
#         count=0
#         j+=1
#         for i in range(j,n):
#             if seq[1]>arr[i][1]:
#                 break
#             else : 
#                 count+=1
#                 if count == n-j:
#                     ncount+=1
#                     break
#     print(ncount+1)
