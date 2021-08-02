#선택정렬 O(N^2)
array=[7,5,9,0,3,1]
for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i], array[min_index] = array[min_index], array[i]
print(array)

#삽입정렬 O(N)~O(N^2)
#정렬이 되어있을수록 줄어드는듯
array=[7,5,9,0,3,1]
for i in range(len(array)):
    for j in range(i,0,-1):
        if array[j]< array[j-1]:
            array[j], array[j-1] = array[j-1],array[j]
        else:
            break
print(array)


#퀵정렬 O(NlogN)~O(N^2)
#일반적인 정렬 라이브러리방식






# # 백준 10815
# import sys
# n=int(sys.stdin.readline())
# a=list(map(int,sys.stdin.readline().split()))
# m=int(sys.stdin.readline())
# b=list(map(int,sys.stdin.readline().split()))
# c=[0]*m
# for i in a:
#     if i in b:
#         c[b.index(i)]=1
# for i in range(m):
#     print(c[i],end=' ')