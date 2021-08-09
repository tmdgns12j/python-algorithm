#이진탐색
#정렬되어있는 리스트에서 탐색범위를 절반씩 좁혀가며 데이터를 탐색
#시작점, 끝점, 중간점을 이용하여 탐색범위를 설정한다

#재귀
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid]== target:
        return mid
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

#반복(while)
def binary_search_while(array, target, start, end):
    while start<= end:
        mid = (start + end)//2
        if array[mid]== target:
            return mid
        elif array[mid]>target:
            end = mid-1
        else:
            start = mid +1
    return None

n, target = list(map(int,input().split()))
array = list(map(int,input().split()))
result = binary_search(array, target, 0, n-1)
result_while = binary_search_while(array, target, 0, n-1)
if result == None:
    print("원소가없어")
else:
    print(result+1)





#이진탐색 라이브러리
#결과 2 4
from bisect import bisect_left, bisect_right
a=[1,2,4,4,8]
x=4
bisect_left(a, x) #정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
bisect_right(a, x)  #정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환

#값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right
def count_by_range(a, left_value, right_value):
    right_index=bisect_right(a, right_value)
    left_index=bisect_left(a, left_value)
    return right_index - left_index

a=[1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))

#파라메트릭 서치(Parametric Search)
#예제 : 떡의 개수 구하기
n , m= list(map(int,input().split(' ')))
array= list(map(int,input().split()))

start = 0
end = max(array)
result = 0
while(start <=end):
    total = 0
    mid = (start + end)//2
    for x in array:
        if x>mid:
            total += x-mid
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid+1
print(result)



#백준 1920 정렬,이분탐색
#n개의 정수와 m개의 정수가 주어진다
#m의 정수가 n에 존재하는지 알아내자
#존재하면 1 존재하지않으면 0으로 출력
# 1. n입력
# 2. n개의 정수 입력
# 3. m입력
# 4. m개의 정수입력
# 5. 1 or 0출력
#풀이 : 이분탐색을하기위해서는 정렬이 필수 따라서 n을 정렬해줌
#n을 이분탐색해 m과 같으면 1을출력 없으면 0을출력
import sys
def b_search(i,arrn,start,end):
    if start>end:
        return 0;
    mid=(start+end)//2
    if i == arrn[mid]:
        return 1
    elif i > arrn[mid]:
        return b_search(i,arrn,mid+1,end)
    else :
        return b_search(i,arrn,start,mid-1)
# def b_search(i,arrn,start,end):   #반복문
#     while start<=end:
#         mid = (start+end)//2
#         if start>end:
#             return 0
#         if arrn[mid]==i:
#             return 1
#         elif arrn[mid]>i :
#             end=mid-1
#         else :
#             start=mid+1
n=int(sys.stdin.readline().rstrip())
arrn=sorted(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline().rstrip())
arrm=list(map(int,sys.stdin.readline().split()))
#print(arrn)
#print(arrm)
for i in arrm:
    start=0
    end=n-1
    print(b_search(i,arrn,start,end))



#백준 2805
#적어도M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하자
# 1. 나무의수N 가져갈 나무의길이M 입력
# 2. 나무의 높이 입력
# 3. 적어도 M미터의 나무를 가져가기 위해서 설정할 수 있는 높이의 최댓값을 출력
#풀이 : 이분탐색 약간의 응용
#'적어도' M미터의 나무를 가져가는것이 중요한 풀이다
import sys
n, m=map(int,sys.stdin.readline().split())
tree=list(map(int,sys.stdin.readline().split()))
#print(tree)
start=0
h=0
end=max(tree)
while start<=end :
    sum=0
    mid=(start+end)//2
    for i in tree:
        if mid >= i:
            sum+=0
        else :
            sum+=i-mid
    #print(sum)
    if sum<m : 
        end=mid-1
    else :          #이부분의 적어도의 부분
        h=mid
        start=mid+1
print(h)
# import sys
# n, m=map(int,sys.stdin.readline().split())
# tree=list(map(int,sys.stdin.readline().split()))
# #print(tree)
# start=0

# end=max(tree)
# while start<=end :
#     sum=0
#     mid=(start+end)//2
#     for i in tree:
#         if mid >= i:
#             sum+=0
#         else :
#             sum+=i-mid
#     #print(sum)
#     if sum<m : 
#         end=mid-1
#     elif sum>m : 
#         start=mid+1
#     elif sum==m : 
#         print(mid)
#         break


#백준 1564
#K개의 랜선으로 모두 N개의 같은 길이의 랜선으로 만들자
#N의 최대길이는?
# 1. 이미 가지고있는 랜선 K개수 입력, 필요한 랜선개수N입력
# 2. K의 길이 입력
# N 출력
#풀이 : 떡볶이, 나무토막 문제와 비슷함
#다른점은 랜선의 최대길이
import sys, math
k, n = map(int,sys.stdin.readline().split())
arr=[]
for i in range(k):
    arr.append(int(sys.stdin.readline().rstrip()))
#print(arr)
result=0
start=0
end=max(arr)
while start<=end:
    sum=0
    mid=math.ceil((start+end)/2)###
    for i in arr:
        if i>=mid:      #i>mid => i>=mid
            sum+=i//mid
    if sum<n:
        end=mid-1
    else : 
        result=mid
        start=mid+1
print(result)