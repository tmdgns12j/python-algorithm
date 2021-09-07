arr1=[[1, 4], [3, 2], [4, 1]]
arr2=[[3, 3], [3, 3]]
x,y=arr1[0]
print(x,y)
print(len(arr2[0]))
def solution(arr1, arr2):
    answer = [[]]
    for i in range(len(arr1)): #3
        x,y=arr1[i]# 1 4
        for j in range(len(arr2[0])):#열
            answer[i].append(x*arr2[0][i]+y*arr2[1][i])
    return answer
print(solution(arr1,arr2))