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