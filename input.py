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