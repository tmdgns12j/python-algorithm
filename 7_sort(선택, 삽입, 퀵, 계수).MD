***
```
#O(N^2)
array=[7,5,9,0,3,1]
for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i], array[min_index] = array[min_index], array[i]
print(array)
```


```
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
```


```

#퀵정렬 O(NlogN)~O(N^2)
#일반적인 정렬 라이브러리방식
```


```
#계수정렬 데이터의개수N, 데이터(양수)중 최대값 K일때 O(N+K)
#공간복잡도도 O(N+K)라 공간복잡도가 ㅈㄴ구림
#데이터의 크기 범위가 제한되어 정수형태로 표현할 수 있을때 사용가능
#동일한값의 데이터가 여러번 등장할때 유리
array=[7,5,9,0,3,1]
count = [0]*(max(array)+1)#1부터 시작하기위해 크기+1
for i in range(len(array)):
    count[array[i]]+=1  # count에서 해당하는 배열의 위치 +1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')
```
***