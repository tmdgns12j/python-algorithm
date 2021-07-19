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