#개미전사
n=int(input())
arr=list(map(int,input().split()))
d=[0]*100

d[0] = arr[0]
d[1] = max(arr[0],arr[1])#둘중에 큰거고름

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+arr[i])
print(d[n-1])

#
x=int(input())# 26
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