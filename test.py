from itertools import permutations
numbers="17"
def solution(numbers):
    numbers=list(map(int,numbers))
    print(numbers)
    per=list(permutations(numbers,2))
    print(per[0])
print(solution(numbers))