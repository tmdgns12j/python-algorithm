numbers=[4,30,2]
def solution(numbers):
    arr={}
print(solution(numbers))
#sorted()
#sorted()를 써도 원래의 배열에는 구조변경이 없음
#프로그래머스 LV1 실패율 참고 sorted(), lambda
# N=5
# stages=[2, 1, 2, 6, 2, 4, 3, 3]
# def solution(N, stages):
#     l=len(stages)
#     result={}
#     c=0
#     for i in range(1,N+1):
#         if l!=0:
#             c=stages.count(i)
#             result[i]=c/l
#             l-=c
#         else:
#             result[i]=0
#     print(result)               #그냥 출력시 키와 값 다나옴
#     print(result[1])            #해당하는 값이나옴
#     print(sorted(result))       #정렬시 키값만 출력됨
#     return sorted(result, key=lambda x:result[x],reverse=True)
# print(solution(N,stages))