#1.DFS기초
#스택 구조를 주로 이용함
#깊은부분을 우선적으로 탐색

#해당노드방문처리->출력->해당노드와 인접한 노드탐색(graph[i])->visited가 false면 재귀
#방문기준 : 번호가낮은 인접노드
def dfs(graph, v, visited) :
    #현재노드를 방문처리
    visited[v]= True
    print(v, end=" ")
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]: #False면(방문한적이없으면)
            dfs(graph, i, visited)
graph=[ #n번노드와 연결되어있는 노드번호를 2차원배열로 구성
    [],
    [2,3,8], #1번노드
    [1,7],   #2번노드
    [1,4,5], #3번노드
    [3,5],   #4번노드
    [3,4],   #5번노드
    [7],     #6번노드
    [2,6,8], #7번노드
    [1,7]    #8번노드
]
# 각 노드가 방문된 정보를 표현(리스트)
visited = [False]*9
dfs(graph, 1, visited)


#얼음틀이 있을때 생성되는 얼음의 갯수(0의묶음)구하기
# 011
# 010   ->4개
# 101
# 1. 행,열 입력
# 2. 얼음칸 입력(배열입력)
# 3. 0의 묶음갯수 구한후 출력
# 풀이 : 3*3 행렬일때 9번모두에게 함수적용
# 
def dfs(x,y):
    #주어진 범위를 벗어나면 종료
    if x<=-1 or x>=n or y<=-1 or y>=m :
        return False
    #현재 노드를 아직 방문안했다면
    if graph[x][y]== 0 :
        #해당노드 방문처리
        graph[x][y]=1
        dfs(x-1,y)#상
        dfs(x,y-1)#좌
        dfs(x+1,y)#하
        dfs(x,y+1)#우
        return True
    return False#else

n,m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#모든 노드(위치)에 대하여 음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS수행
        if dfs(i,j) == True:
            result+=1
print(result)

#백준 1260 오류 미해결
from collections import deque
def dfs(new,v,visited):
    visited[v]=True
    print(v,end=" ")
    for i in new[v]:
        if not visited[i]:
            visited[i]=True
            dfs(new,i,visited)


def bfs(new,v,visitedd):
    queue=deque([v])
    visitedd[v]=True
    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for i in new[v]:
            if not visitedd[i]:
                visitedd[i]=True
                queue.append(i)

n, m, v=map(int,input().split())
arr=[]
visited=[False]*(n+1)
visitedd=[False]*(n+1)
new=[[]for i in range(n+1)]
for i in range(m):
    arr.append(list(map(int,input().split())))
arr.sort()
#print(arr)
for i in range(m):
    x,y=arr[i]
    new[x].append(y)
    new[y].append(x)
#print(new)
dfs(new,v,visited)
print()
bfs(new,v,visitedd)



#백준 2606
#1번컴퓨터를통해 바이러스에 감염된 컴퓨터 수 구하기
# 1. 컴퓨터 수 입력
# 2. 연결된 링크(쌍)  수 입력
# 3. 링크 입력,   1 2 -> 1번컴 2번컴 연결
# 4. 출력
#풀이 : 기본 dfs문제 기초잡기좋음
#연결되어있는 링크들을 n번노드에 연결되어있는 노드배열로 바꾸는게 핵심
#나머지는 dfs알고리즘과 동일
com=int(input())#컴퓨터수
n=int(input())#링크수
arr=[]#링크 들어갈 배열
for i in range(n): # 링크 입력(초기화)
    arr.append(list(map(int,input().split())))
re=[[]for i in range(com+1)]# n번노드에 인접한 노드묶음으로 재배치할 배열
                            # 1번노드부터 시작하기위해 컴퓨터수+1 해줌
count=int(0)
visited=[False]*(com+1) #방문처리할 배열
for i in range(n):    #n번노드에 인접한노드를 배열로 재생성
    x,y=arr[i]
    re[x].append(y)
    re[y].append(x)
#print('re= ',re)
visited[1]=True

def dfs(visited,v,re):
    global count
    for i in re[v]:
        if not visited[i]:
            visited[i]=True
            count+=1
            dfs(visited,i,re)
dfs(visited,1,re)
print(count)



#LV2 타겟넘버 recursion 재귀, dfs
#숫자들이 주어진다
#이 숫자들을 적절히 더하거나 빼서 타겟넘버를 만들고
#가능한 방법의 수를 출력하라
numbers=[1, 1, 1, 1, 1]
target=3
answer=0
def solution(numbers, target):
    def dfs(i,number,sum):
        global answer
        sum+=number
        if i==len(numbers)-1:
            if sum==target:
                answer+=1
        else:
            dfs(i+1,numbers[i+1],sum)
            dfs(i+1,-numbers[i+1],sum)
    sum=0
    dfs(0,numbers[0],sum)
    dfs(0,-numbers[0],sum)
    return answer
print(solution(numbers, target))