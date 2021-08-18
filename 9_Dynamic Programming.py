#개미전사
#식량창고 개수 N이주어짐
#식량창고에 저장된 식량개수 K주어짐
#개미전사가 얻을수 있는 식량의 최대값 구하기
#최소 한칸이상 떨어진 식량창고를 약탈해야함
n=int(input())
arr=list(map(int,input().split()))
d=[0]*100

d[0] = arr[0]
d[1] = max(arr[0],arr[1])#둘중에 큰거고름

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+arr[i])
print(d[n-1])

#1로만들기
#X가 5로 나누어떨어지면 5로나눔
#X가 3으로 나누어떨어지면 3으로나눔
#X가 2로 나누어떨어지면 2로나눔
#X에서 1을뺌
#이 4개의 연산으로 1을만드는데 필요한 연산횟수의 최소값 구하기
x=int(input())
d=[0]*x
for i in range(2,x+1):
    d[i]=d[i-1]+1
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)
print(d[x])

#화폐구성
n,m = map(int,input().split())
array=[]
for i in range(n):
    array.append(int(input()))

d=[10001]*(m+1)

d[0]=0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]] != 10001:
            d[j]=min(d[j],d[j-array[i]]+1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])



#백준 1463
#1로만들기
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다
# 위 3가지연산 사용횟수의 최소값 구하기
#풀이 : 점화식만 잘 구하면 됨
n=int(input())
d=[0]*(n+1)

for i in range(2,n+1):
    d[i]=d[i-1]+1
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
print(d[n])



#백준 9095
#1,2,3 더하기
#정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성
# 1. 테스트케이스개수 T입력
# 2. T만큼 11까지의 정수n입력 ->0일때도 처리해야 오류가 안남
#풀이 : 점화식
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
d=[0]*12
d[0]=1
for j in arr:
    for i in range(0,j+1):
        if i==1:
            d[1]=1
        if i==2:
            d[2]=2
        if i==3:
            d[3]=4
        if i>3:
            d[i]=d[i-3]+d[i-2]+d[i-1]
    print(d[j])



#백준 1003  n>=2 f(n)=(n-1)+f(n-2)
#피보나치함수를 재귀함수로 처리할때 0과 1이 몇번 출력되는지 구하여라
# 1. 테스트케이스 갯수 T
# 2. N입력
#풀이 : 점화식
t=int(input())
for i in range(t):
    n=int(input())
    c0=0
    c1=0
    d0=[0]*(n+1) #0개수
    d1=[0]*(n+1) #1개수
    for i in range(n+1):
        if i==0:
            d0[i]=1
        if i==1:
            d1[i]=1
        if i>=2:
            d0[i]=d0[i-2]+d0[i-1]
            d1[i]=d1[i-2]+d1[i-1]
    print(d0[n],d1[n])


#백준 11726
n=int(input())
d=[0]*(n+1)
for i in range(1,n+1):
    if i==1:
        d[i]=1
    if i==2:
        d[i]=2
    if i>=3:
        d[i]=d[i-2]+d[i-1]
print(d[n]%10007)



#백준 1149  RGB거리
#집이N개 주어진다 한개의 집에는 RGB중 하나로 칠할수있고 각 색에대한 비용이 주어진다
#이웃하는 집에 같은색을 연속으로 칠할수없다 RRG=>X
#N개의 집을 칠할때 드는 최소비용을 구하자
# 풀이 : 점화식 구하는게 좀 까다로웠음 과정을 표현하는게 중요한듯
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
#print(arr)

for i in range(1,n):
    arr[i][0]+=min(arr[i-1][1],arr[i-1][2])
    arr[i][1]+=min(arr[i-1][0],arr[i-1][2])
    arr[i][2]+=min(arr[i-1][1],arr[i-1][0])
print(min(arr[n-1][0],arr[n-1][1],arr[n-1][2]))