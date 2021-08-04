a=input()
print(a)

b=input()
b=int(b)
print(b)

b=input()
b=float(b)
print(b)

a,b=input().split() #a,b를 space를 기준으로 나누어 두개 한번에 입력 1 3
print(a)
print(b)

a=input()
print(a,a,a) #입력받아 3번출력가능

a,b=input().split(':') # 3:43 입력하면 ':'가 구분자
print(a,b,sep=':') #seperate : 가 a : b로 입력

a,b,c = input().split('.')# 2010.3.12 입력
print(c,b,a,sep='-')# 12-3-2010 출력

s = input()#210712 입력
print(s[0:2], s[2:4], s[4:6], sep=' ') #21 07 12

a, b = input().split()#qwe rty
print(a+b)#qwerty

a,b=input().split()#3 4
c=int(a)+int(b)#int로 형변환
print(c)#7

a=input()
a=int(a,16)#a를 16진수 정수로 형변환
print("%o"%a)#8진수로 출력

a=ord(input())#ord()유니코드로 변환
print(a)

c=int(input())
print(chr(c))#int형 유니코드 char변환

a=input()
print(-int(a))#음수변환

a=ord(input())
print(chr(a+1))#a입력하면 b출력, 0입력하면 1출력 아스키코드에+1해준거임

a,b = input().split()
print(int(a)-int(b))#a-b

a,b = input().split()
print(float(a)*float(b))#a*b

a,b = input().split()#love 3 입력
print(a*int(b))#lovelovelove

a,b=input().split()# 2 10
c=int(a)**int(b)#거듭제곱
print(c)#1024

a,b=input().split()#10 3
c=int(a)//int(b)#나눈 몫
print(c)# 3

a,b=input().split()
c=int(a)%int(b) # 나머지
print(c)

a=float(input())#3.3333333
print( format(a, ".2f") )# 3.33 소수점 둘째자리까지 출력

a,b=input().split()
a=float(a)
b=float(b)
print(format(a/b,".3f"))

a,b = input().split()
a=int(a)
b=int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(float(a/b),".2f"))

a,b,c = input().split()
a=int(a)
b=int(b)
c=int(c)
print(format(float((a+b+c)/3),".2f"))

n=int(input())
print(bool(n))#0은 false 나머지 true

a=bool(int(input()))
print(not a)#

a,b=input().split()
print(bool(int(a)) and bool(int(b)))

a,b=input().split()
a = bool(int(a))
b = bool(int(b))
print((a and (not b)) or ((not a) and b))#nor 01 10 이 참

#-------------------------------------------sys.stdin.readline
import sys
n=sys.stdin.readline() 
print(n)    #개행문자까지 출력됨
n=sys.stdin.readline().split()
print(n)    #개행문자가 출려되지않음

input = sys.stdin.readline  #이런 방법도 가능함
n=input()
print(n)

arr=[]
arr.append(sys.stdin.readline())
arr.append(input())
print(arr)