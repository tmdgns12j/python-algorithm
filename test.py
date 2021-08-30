N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]
def solution(N, stages):
    l=len(stages)
    result={}
    c=0
    for i in range(1,N+1):
        if l!=0:
            c=stages.count(i)
            result[i]=c/l
            l-=c
        else:
            result[i]=0
    print(result)
    print(result[1])
    print(sorted(result))
    return sorted(result, key=lambda x:result[x],reverse=True)
print(solution(N,stages))
# {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0.0}
# [1, 2, 3, 4, 5]
# [3, 4, 2, 1, 5]