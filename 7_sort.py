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