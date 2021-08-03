#이진탐색
#정렬되어있는 리스트에서 탐색범위를 절반씩 좁혀가며 데이터를 탐색
#시작점, 끝점, 중간점을 이용하여 탐색범위를 설정한다
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

n, target = list(map(int,input().split()))
array = list(map(int,input().split()))
result = binary_search(array, target, 0, n-1)
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




