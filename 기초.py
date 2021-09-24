#if문 조건문
a,b,c = input().split()
a=int(a)
b=int(b)
c=int(c)

if a%2==0:
    print(a)

if b%2==0:
    print(b)
    
if c%2==0:
    print(c)

#
a,b,c = input().split()
a=int(a)
b=int(b)
c=int(c)

if a%2==0:
    print("even")
else:
    print("odd")

if b%2==0:
    print("even")
else:
    print("odd")

if c%2==0:
    print("even")
else:
    print("odd")

#
a=int(input())
if a<0 :
    if a%2==0 :
        print("A")
    else :
        print("B")
else :
    if a%2==0 :
        print("C")
    else :
        print("D")

#학점
a=int(input())

if a>= 90 :
    print("A")
elif a>=70 :
    print("B")
elif a>=40 : 
    print("C")
elif a>=0 :
    print("D")

#
a=input()

if a=='A' :
    print("best!!!")
elif a=='B' :
    print("good!!")
elif a=='C' :
    print("run!")
elif a=='D' :
    print("slowly~")
else :
    print("what?")


#반복문 while문
a=1
while a!=0 :
    a=int(input())
    if a!=0 :
        print(a)

#5 입력 ->5 4 3 2 1
a=int(input())
while a>0 :
    print(a)
    a-=1

#4입력 1 2 3 4
a=int(input())
i=0
i=int(i)
while i<=a :
    print(i)
    i+=1

#반복문 for문
#range(끝)
#ange(시작, 끝)
#range(시작, 끝, 증감)
#시작수는포함 끝수는 미포함 n...n-1
a=int(input()) # 4 -> 0 1 2 3 4
for i in range(a+1) :
    print(i)

# a 까지 짝수합
a=int(input())
sum=int(0)
for i in range(a+1) :
    if i%2==0 :
        sum+=i
print(sum)



#q가아닐때까지 출력
a='c'
while a!='q' :
    a=input()
    print(a)


#리스트
n=int(input())
a=input().split()

for i in range(n) :
    a[i]=int(a[i])

d=[]
for i in range(24):
    d.append(0)

for i in range(n) :
    d[a[i]]+=1

for i in range(1,24) :
    print(d[i],end=' ')


#
n=int(input())
a=input().split()
for i in range(n) :
    a[i]=int(a[i])

for i in range(n-1,-1,-1) :
    print(a[i],end=' ')


#최소값 출력
n=int(input())
a=input().split()
f=int(100)
for i in range(n) :
    a[i]=int(a[i])

for i in range(n-1) :
    if a[i]>a[i+1] :
        a[i+1]=a[i+1]
    else :
        a[i+1]=a[i]
print(a[n-1])

n=int(input())


#문자열반복 1 2 abc ->aabbcc
for i in range(n) :
    a,b=input().split()
    a=int(a)
    sum=""
    for j in range(len(b)) :
        sum+=a*b[j]
    print(sum)


# OX점수 OOO->6점
n=int(input())
for i in range(n) :
    a=input()
    sum=int(0)
    score=int(1)
    for j in range(len(a)) :
        if a[j]=='O' :
            sum+=score
            score+=1

        else :
            score=1
    print(sum)


#예외처리
while 1 :
    try :
        a,b=input().split()
        a=int(a)
        b=int(b)
        print(a+b)
    except :
        break

#
a=input().split() #asdf sfd ewe fe ->단어개수 출력
print(len(a))# 4

#문자열
word = 'abcd'
print(word[0]) # a, 3->d, -1 ->d ,-4 ->a


#리스트
list =['a','b','v']
print(list)#출력 ['a','b','v']
print(list[0])# a

#letter에 f가 하나씩만 들어감
f="apple"
for letter in f :
    print(letter, end=" ")

#자음 삭제후 출력
n="aeiouAEIOU"
a=input('문자열 입력 : ')
result=""
for i in a :
    if i not in n :
        result+= i
print(result)

#자음모음 개수 나타내기
ja="aeiouAEIOU"
s=input()
result = ""
cj=int(0)
cm=int(0)
for letter in s :
    if letter not in ja :
        cj+=1
    else:
        cm+=1
print(cj,cm)

#백준 2577
#배열, count(), str()
a=int(input())
b=int(input())
c=int(input())
multi=a*b*c

for i in range(10) :
    list_multi=list(str(multi)) #곱한결과를 리스트에 숫자별로 저장하기위해 str로 변환, str()은 각 글자를 배열에 한칸씩 넣어줌
    print(list_multi.count(str(i)))

#map()
#공백을 기준으로 구분된 데이터를 입력받을때 사용
a=list(map(int, input().split()))
print(a)

a, b, c=map(int,input().split())
print(a,b,c,end=" ")

#더욱 빠르게 입력받기 (아마 자바의 buffer같은 거인듯)
#rstrip()는 enter제거
import sys
data = sys.stdin.readline().rstrip()
print(data)

# f-string / 3.6이상부터 가능
#문자열과 정수를 함께 출력할때 변환하지 않아도 됨
answer = 7
print(f"정답은 {answer} 입니다.")

#부등식
x=15
if 0<x<20:
    print("신기하지?")

#2차원배열 초기화
#프로그래머스 LV2 행렬의 곱셈 참조
arr1=[[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2=[[5, 4, 3], [2, 4, 1], [3, 1, 1]]
answer = [[0 for i in range(len(arr2[0]))] for i in range (len(arr1))]

#for else
#if else랑은 연결되지않음 if else 처럼 for else가 존재함
#파이썬만 가능함
#LV2 스킬트리 참조
arr=[1,2,3,4,5]
for i in arr:
    print(i)
    if i==4: #i==6
        print("멈춤")
        break
print("난 언제?")
#1 2 3 4 멈춤
#1 2 3 4 5 난언제?


#문자열출력 %d
#서울에서 김서방찾기
#배열이 주어질때 Kim의 위치를 찾아라
seoul=["Jane", "Kim"]
def solution(seoul):
    num=seoul.index('Kim')
    return"김서방은 %d에 있다" % num
print(solution(seoul))


#문자열다루기 기본 isdigit(), isnum(), isalpha
#문자열의 길이가 4또는6이고 숫자로만 구성되어있는지 확인하는 함수 작성
def solution(s):
    if (len(s)==4 or len(s)==6) and s.isdigit():
        return True
    else:
        return False