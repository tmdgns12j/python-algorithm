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
#개수n을 입력받아 오름차순으로 정력
#시간제한 3초 메모리 8mb
#풀이 : 직접 비교하여 정렬하는 방법이아닌
#해당하는 값을 인덱스에 동일한 번호로 나온 횟수만큼 더해줌
#인덱스를 순차적으로 인덱스의 값만큼 출력
import sys
i = int(sys.stdin.readline())
num = [0]*10001
for _ in range(i):
    num[int(sys.stdin.readline())] += 1
for j in range(10001):
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