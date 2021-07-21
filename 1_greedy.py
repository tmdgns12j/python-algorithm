***
#동전, 거스름돈
#거스름돈의 액수가 주어지면 줘야할 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수
# 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오. 거스름돈은 항상 $5.00 이하
#  손님이 받는 동전의 개수를 최소로 하려고 한다
# 예를 들어, $1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.
n=int(input())
for i in range(n) :  #거스름돈 몇번
    change=int(input()) #줄 거스름돈 입력
    qua=int(0) #쿼터 초기화
    da=int(0) #다임 초기화
    ni=int(0) #니켈 초기화
    pe=int(0) # 페니 초기화
    while change>0 :  #
        if change>=25 :
            qua+=1
            change-=25
        elif change>=10 :
            da+=1
            change-=10
        elif change>=5 : 
            ni+=1
            change-=5
        elif change>=1 :
            pe+=1
            change-=1
    print(qua, da, ni, pe,end=" ")
***
#동전 500, 100, 50, 10, 5, 1
#1000원을 내고 잔돈을받자
#1. 가격입력
#2. 동전최소개수 출력
price = int(input())
exchange=1000-price
cnt=int(0)
while exchange!=0 :
    if exchange>=500 :
        exchange-=500
        cnt+=1
    elif exchange>=100 :
        exchange-=100
        cnt+=1
    elif exchange>=50 :
        exchange-=50
        cnt+=1
    elif exchange>=10 :
        exchange-=10
        cnt+=1
    elif exchange>=5 :
        exchange-=5
        cnt+=1
    elif exchange>=1 :
        exchange-=1
        cnt+=1
print(cnt)

#상자에 책넣기 백준1434 2시간
#1. 박스개수, 책개수 입력
#2. 박스의크기 입력
#3. 책의 크기 입력
#박스에 책을넣되 박스의 크기가 책의 크기보다 커야함
#박스에 책을 최대한 많이넣자

#풀이 : 책을 박스에넣으려하지말고 박스를 책에 맞추자
#박스크기-=책의크기
a,b=input().split()
boxc=int(a)
bookc=int(b)
box=input().split()
book=input().split()
sum=int(0)
for i in range(boxc) : #3 3
    box[i]=int(box[i])
for j in range(bookc) : #3
    book[j]=int(book[j])

for i in range(bookc) :
    for j in range(boxc) :
        if box[j]>=book[i] :
            box[j]-=book[i]
            break

for i in range(boxc) :
    sum+=box[i]
print(sum)


#백준2810 컵홀더개수
#S는 솔로석 LL은 커플석
#컵홀더는 *S*LL*S*LL*LL*이런식임
#쓸수있는 컵홀더 개수를 찾자
#풀이 : 컵홀더개수의 비밀을찾자
#좌석수-커플석(LL)수 or 솔로만있을때 솔로수만
n=int(input()) #좌석개수 SLLS -> 4
sit=str(input()) #좌석입력 SLLLLSSLL
lcnt=int(0) #L갯수
scnt=int(0) #S갯수
for i in range(n) : #좌석에 L있나 훑어볼꺼임
    if sit[i]=='L' : #L있으면 +1
        lcnt+=1
    else :           #S있으면 +1
        scnt+=1
if lcnt!=0 : #L이 하나라도있으면
    print(len(sit)+1-int(lcnt/2)) #좌석+1에 커플좌석수/2
if scnt==len(sit) : #솔로들 수 출력
    print(scnt)

#2839 최소개수
#5키로 3키로봉지
#무게가 주어지면 봉지를 최소로사용하여 봉지개수 구하기
# 1. 무게입력
# 2. 봉지갯수 출력
#풀이 : 3씩 빼면서 5로 나누어떨어지는지 보기
#거꾸로 생각해보기**
kg=int(input())
three=int(0)
while(kg>=0) :
    if kg%5==0 or kg==0 :
        print(int(kg/5)+three)
        break
    else :
        kg-=3
        three+=1
if kg<0 :
    print(-1)


#11399
#최소로 줄 기다리기
#정렬문제 sort()사용
# 1. 인원수
# 2. 인당 걸리는시간 입력
#  1,2,3 -> 1+ 1+2+ 1+2+3
# 3. 출력
n=int(input())#사람수
arr=input().split()#인당 걸리는시간
sum=int(0)#시간 초기화
for i in range(len(arr)) : #시간 입력
    arr[i]=int(arr[i])

arr.sort() # 정렬

for i in range(len(arr)) : 
    sum+=arr[i]*((len(arr))-i)
print(sum)

#1789 수들의합
#서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
# 1. 합한수 S 입력
# 2. N(S까지의 합한개수)의 최대값 출력
#풀이: S가 주어졌을때 1+2+....n 이 N이 최소개수가 되는방법
#S=200일때 200이거나 200을 넘기는 합을 구함(210)
#여기서 넘치는값을 빼면됨 -10
#그럼 19개
n=int(input()) #S입력
sum=int(0)#합초기화
i=int(0)#N을 위한 갯수 초기화
while(sum<n) : #S를넘기는 합
    i+=1 #N을위한 카운트겸 1+2+3을 위함
    sum+=i

if sum>n : #S를 초과한경우 값을 빼주어야하기때문에 -1
    print(i-1)
else :
    print(i)

