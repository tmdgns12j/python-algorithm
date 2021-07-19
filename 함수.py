#절대값 abs()
a=abs(-3)
print(a)

#첫째자리에서 반올림 함수 round()
a=round(1.331141)
print(a)

#최대값 max()
a=max(20,30,40,10)
print(a)

#str() 문자열로 변환
#str()은 각 글자를 배열에 한칸씩 넣어줌
#str(100) -> 1 0 0
a=100
a=str(a)
if a=="100" : #문자열인지 검증
    print(a)

#count() 갯수세기
a=int(input())
b=int(input())
c=int(input())
multi=a*b*c

for i in range(10) :
    list_multi=list(str(multi))
    print(list_multi.count(str(i)))