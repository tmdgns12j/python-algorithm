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