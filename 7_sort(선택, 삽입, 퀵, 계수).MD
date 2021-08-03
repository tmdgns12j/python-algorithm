***


# 선택정렬
+ 가장 작은 데이터를 **선택**해 맨 앞에있는 데이터와 바꿔줌

![선택정렬](https://user-images.githubusercontent.com/69194442/127944801-ee39b013-d7c8-48ee-a5c5-f9a878973b88.PNG)

+ 7 5 9 0 3 1 6 2 4 8
+ **_0_** 5 9 **_7_** 3 1 6 2 4 8
+ 0 **_1_** 9 7 3 **_5_** 6 2 4 8
+ 0 1 **_2_** 7 3 5 6 **_9_** 4 8
+ 0 1 2 **_3_** **_7_** 5 6 9 4 8
+ 0 1 2 3 **_4_** 5 6 9 **_7_** 8

+ ...
         
+ 0 1 2 3 4 5 6 7 8 9
```
#선택정렬 O(N^2)
# 1. 가장 앞부터 가장 뒤까지 탐색하면서 가장 작은값의위치(j)를 min_index에 저장
# 2. 가장 앞과 min_index를 교체
# 3. 반복

array=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index=i     #0부터 시작하기 위함
    for j in range(i+1,len(array)):     #1부터 끝까지(0부터 시작했으니까)
        if array[min_index]>array[j]:   #지금까지 작은값보다 탐색한값이 더 작으면
            min_index=j                 #탐색한값을 저장
    array[i], array[min_index] = array[min_index], array[i]     #스왑
print(array)
```
<br>
<br>
<br>

# 삽입정렬
+ 데이터를 하나씩골라 적절한 위치에 **삽입**
+ 첫번째 데이터부터 시작, 그 **다음데이터와 비교**하여 **왼쪽/오른쪽**에 올지 결정하여 삽입

![선택정렬](https://user-images.githubusercontent.com/69194442/127944815-315e25c9-5643-4b03-9283-10b4281a5c3d.PNG)

+ 7 5 9 0 3 1 6 2 4 8
+ **_5_** **_7_** 9 0 3 1 6 2 4 8
+ 5 7 9 0 3 1 6 2 4 8
+ **_0_** 5 7 9 3 1 6 2 4 8
  + 0이 9보다작나? -> 7보다작나? -> 5보다작나? -> 맨앞

+ 0 **_3_** 5 7 9 1 6 2 4 8
+ 0 **_1_** 3 5 7 9 6 2 4 8

+ ...

+ 0 1 2 3 4 5 6 7 8 9

```
#삽입정렬 O(N)~O(N^2)
#정렬이 되어있을수록 줄어드는듯
# 1. n과 n-1을 비교
# 2. n이 더 작으면 n-1과 교체
# 3. 0번지 까지 반복 (5 7 9 0 -> 5 7 0 9 -> 5 0 7 9 -> 0 5 7 9)
# 4. 다음으로 이동
# 5. 반복
array=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):     #0부터 끝까지
    for j in range(i,0,-1):     #n부터 0까지 -1씩 탐색
        if array[j]< array[j-1]:    #n-1이 더 작으면
            array[j], array[j-1] = array[j-1],array[j]  #스왑
        else:   #바꿀필요가없으면 빠져나옴
            break
print(array)
```

<br>
<br>
<br>

# 퀵정렬
![선택정렬](https://user-images.githubusercontent.com/69194442/127944840-b9e82f0a-6e40-436b-8019-ab2e86c5d717.PNG)



```
#퀵정렬 O(NlogN)~O(N^2)
#일반적인 정렬 라이브러리방식
```

<br>
<br>
<br>

# 계수정렬
+ 데이터의 크기범위가 제한되어 정수 형태로 표현할 수 있을때 사용가능
+ 인덱스가 데이터의 값에 해당, 각각의 데이터가 총 몇번씩 등장했는지를 저장
+ 0~n까지 개수에 따라 출력

![계수정렬](https://user-images.githubusercontent.com/69194442/127944844-3cff75cd-4cea-4957-a84c-3c46b831c3aa.PNG)


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

<br><br><br>

![정렬비교](https://user-images.githubusercontent.com/69194442/127944851-bc0beeea-79ae-48a9-9df4-640fd681d562.PNG)

***
