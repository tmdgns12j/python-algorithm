백준 2579 계단오르기  
계단은 연속해서 두계단까지 밟을수있음  
연속된 세계단은 불가능  
마지막 계단은 무조건 밟아야함  
점수의 최대값 구하여라  
 1. 계단개수 N
 2. 각각의 계단 점수 입력
 3. 최대값 출력

![stair](https://user-images.githubusercontent.com/69194442/130168354-5a930da2-b3a3-4c22-b9d6-5091e22df7e4.PNG)

```
n=int(input())
stair=[]
d=[0]*(n+1)
for i in range(n):
    stair.append(int(input()))
#print(stair)
for i in range(n):
    if i==0:
        d[i]=stair[i]
    if i==1:
        d[i]=d[0]+stair[i]
    if i>=2:
        d[i]=max(stair[i]+stair[i-1]+d[i-3],stair[i]+d[i-2])
print(d[n-1])
```
