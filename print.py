print("Hello")
print("'Hello'")
print('"Hello"')
print("\"!@#$%^&*()\'")
print("\\")

#문자열출력 %d
#서울에서 김서방찾기
#배열이 주어질때 Kim의 위치를 찾아라
seoul=["Jane", "Kim"]
def solution(seoul):
    num=seoul.index('Kim')
    return"김서방은 %d에 있다" % num
print(solution(seoul))