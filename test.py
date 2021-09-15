n=45
def solution(n):
    arr=[]
    number=""
    while n>0:
        arr.append(n%3)
        n=n//3
    number=list(map(str,arr))
    answer="".join(number)
    answer=int(answer)


    return answer
print(solution(n))