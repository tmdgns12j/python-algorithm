#자기 자신을 다시 호출함
#파이썬은 최대깊이(재귀)제한이있어서 돌리다보면 초과뜸, 깊이제한 설정해줘야함
#RecursionError: maximum recursion depth exceeded while calling a Python object
#재귀함수는 stack구조로 쌓이게됨, 그래서 stack사용할때 재귀를 이용하는 경우가 많음
i=int(0)
def recursive_f():
    global i
    i+=1
    #if i==100 : return
    print(i, end=" ")
    print("알고리즘EZ")
    recursive_f()
recursive_f()

#재귀 구조알아보기
#결과 : 
# 1번째 재귀함수...n번째 재귀함수 n번째 재귀함수종료...1번째 재귀함수 종료
def recursive_f(i) :
    if i==5 : return
    print(i,'번째 재귀함수')
    recursive_f(i+1)
    print(i, '번째 재귀함수 종료')
recursive_f(1)

#팩토리얼
def factorial(i) :
    if i<=1:
        print("1")
        return 1
    print(i,'*',end=" ")
    return i*factorial(i-1)
print(factorial(5))

#유클리드호제법 gce(최대공약수 구하기)/함수도있음