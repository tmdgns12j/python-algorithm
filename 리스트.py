#append() 리스트에 값을 추가할때 사용
score=[1,2,3,5,8,9]
for i in range(2) :
    score.append(int(input("입력 : ")))
print(score) #[1,2,3,5,8,9, ?, ?]

#리스트 값 조회하기
score=[1,2,3,5,8,9]
for scores in range(score) :
    print(scores)

#리스트 클래스 list()
list1=list()# 공백 리스트 생성
list1=[]#위와 동일
list2=list("hello") #H,e,l,l,o 리스트
list3=list(range(0,5))#0,1,2,3,4리스트

#인덱스 슬라이싱
score=[1,2,3,5,8,9]
print(score[1:4])#2,3,5

#insert() 리스트 원하는위치에 요소삽입
#append는 리스트의 끝에 삽입
score=[2,3,4,5]
score.insert(0,1)#0번째에 1삽입
print(score)

#.index로 위치찾기
list=["0번","1번","2번","3번"]
index = list.index("0번")
print(index)

#요소 삭제하기 pop() 원하는 위치의 요소 삭제
list=["0번","1번","2번","3번"]
list.pop(1)
print(list)

#요소삭제하기 remove() 일치하는 값의 요소를 삭제
list=["0번","1번","2번","3번"]
list.remove("1번")
print(list)

#정렬 sort()
score=[6,5,4,3,2,1]
score.sort()
print(score)

#리스트의 깊은복사 list()이용
#score의 값이 변하지 않음
score=[6,5,4,3,2,1]
copy=list(score)
copy[0]=10
print(score)
print(copy)

#리스트 컴프리핸션(list comprehension)
#리스트에 식을 넣을수있음
s=[x**2 for x in range(10)]
print(s)

#count() 갯수세기
a=int(input())
b=int(input())
c=int(input())
multi=a*b*c

for i in range(10) :
    list_multi=list(str(multi))
    print(list_multi.count(str(i)))

#map()
#공백을 기준으로 구분된 데이터를 입력받을때 사용
a=list(map(int, input().split()))
print(a)

a, b, c=map(int,input().split())
print(a,b,c,end=" ")