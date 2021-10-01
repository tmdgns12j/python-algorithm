#소수찾기 set() permutation() 조합 경우의수
#에라토스테네스의 체 참고
#한자리 숫자가 적힌 종이조각들이 들어있다
#종이를 붙여 소수를 몇개 만들수있는지 출력
from itertools import permutations
numbers="17"
def solution(numbers):
    new=set()
    answer=[]
    numbers=list(numbers)
    for i in numbers:
        new.add(int(i))
    for i in range(2,len(numbers)+1):
        per=list(permutations(numbers,i))
        for i in per:
            i=int("".join(i))
            new.add(i)
    if 0 in new:
        new.remove(0)
    if 1 in new:
        new.remove(1)
    answer=len(new)
    for i in new:
        for j in range(2,i//2+1):
            if i%j==0:
                answer-=1
                break
    return answer
print(solution(numbers))