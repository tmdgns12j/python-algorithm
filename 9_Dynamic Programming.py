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