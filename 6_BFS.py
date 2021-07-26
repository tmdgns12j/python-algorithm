#너비우선탐색
#가까운 노드부터 우선적으로 탐색
#큐를 이용
#1. 탐색 시작노드를 큐에삽입하고 방문처리
#2. 큐에서 노드를 꺼낸뒤에 해당 노드의 인접노드 중에서 방문하지않은 노드를 모두 큐에삽입하고 방문처리
from collections import deque
def bfs(graph, start, visited) :
    #deque사용
    queue=deque([start])
    #현재노드 방문처리
    visited[start] = True
    #큐가 빌때까지 계속
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v=queue.popleft()
        print(v,end=' ')
        #아직 방문하지 않은 인접한 원소를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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
bfs(graph, 1, visited)



#미로탈출 최단거리
from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue: #큐가 빌때까지 반복
        x, y= queue.popleft()
        for i in range(4):   #현재 위치에서 4가지 방향으로 확인
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: #범위넘을시 무시
                continue
            if graph[nx][ny] ==0: #벽인경우 무시
                continue
            if graph[nx][ny] ==1:  #해당노드 처음방문시 최단거리 기록
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]   #가장 오른쪽아래까지의 최단거리 반환
n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
#  상 하 좌 우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
print(bfs(0,0))


#백준1388
#나무판자 갯수구하기(모양따라 갯수정해짐)
# -|-- ->3개필요

#-|--
#-||-  ->6개 필요
#1. n,m주어짐(행렬)
#2. -갯수구하기
#3. |갯수구하기
#4. 출력
n,m=map(int, input().split())
board=[]
count=int(0)
for i in range(n) :  #나무판자 모양 입력
    board.append(list(input()))
for i in range(n):   #'-'라 가로 검색
    pre='_'
    for j in range(m):
        if board[i][j]!=pre:
            pre=board[i][j]
            if board[i][j]=='-':
                count+=1
for i in range(m):  #'|' 세로 검색
    pre='_'
    for j in range(n):
        if board[j][i]!=pre:
            pre=board[j][i]
            if board[j][i]=='|':
                count+=1
print(count)


#백준 2606
#1번컴퓨터를통해 바이러스에 감염된 컴퓨터 수 구하기
# 1. 컴퓨터 수 입력
# 2. 연결된 링크(쌍)  수 입력
# 3. 링크 입력,   1 2 -> 1번컴 2번컴 연결
# 4. 출력
#풀이 : 딱 basic한 bfs문제 기초잡기좋음
#연결되어있는 링크들을 n번노드에 연결되어있는 노드배열로 바꾸는게 핵심
#나머지는 bfs알고리즘과 동일

from collections import deque
com=int(input())#컴퓨터수
n=int(input())#링크수
arr=[]#링크 들어갈 배열
for i in range(n): # 링크 입력(초기화)
    arr.append(list(map(int,input().split())))
re=[[]for i in range(com+1)]# n번노드에 인접한 노드묶음으로 재배치할 배열
                            # 1번노드부터 시작하기위해 컴퓨터수+1 해줌

visited=[False]*(com+1) #방문처리할 배열
for i in range(n):    #n번노드에 인접한노드를 배열로 재생성
    x,y=arr[i]
    re[x].append(y)
    re[y].append(x)
#print('re= ',re)

def bfs(visited,v,re) :
    queue=deque([v])
    count=int(0)
    visited[v]=True
    while queue :
        v=queue.popleft()
        for i in re[v] :
            if not visited[i]:
                visited[i]=True
                count+=1
                queue.append(i)
    return count
print(bfs(visited,1,re))


#백준 1012
#배추가 1로 표현되어있는 배추농장에 해충방지 배추흰지렁이를 놓자
#배추 흰지렁이는 인접한 배추로 옮겨갈수있다
#유기농을위한 배추흰지렁이의 최소개수를 구하자
# 1. 테스트케이스 횟수입력
# 2. 행 열 배추의개수 입력
# 3. 배추의 위치 입력
# 4. 출력
#풀이 : 배열선언후 배추위치를 1로 초기화
#해당 노드의 상하좌우를 탐색하고 1이있으면 큐에 저장
#인접한노드 전부 탐색했으면 지렁이+1 
#모든요소(행렬)에대해서 bfs수행 반복 
from collections import deque
def bfs(x,y) :
    queue=deque()
    queue.append((x,y))
    global count
    count+=1
    while queue:
        x,y=queue.popleft()
        for i in range(4) : #상하좌우 탐색
            n_x=x+dx[i]
            n_y=y+dy[i]
            if n_x<0 or n_x>=n or n_y<0 or n_y>=m: #범위넘을시 무시
                continue
            if arr[n_x][n_y]==1:    #상하좌우탐색한 노드가 1이면 0으로 변환후 큐에 추가
                arr[n_x][n_y]=0
                queue.append((n_x,n_y))
        

t=int(input())  #테스트케이스 횟수
dx=[-1,1,0,0]   #상,하,좌,우
dy=[0,0,-1,1]
for k in range(t) :
    count=int(0)    #지렁이 초기화 
    m,n,c=map(int,input().split())  #열, 행, 배추개수
    arr=[[0]*m for i in range(n)]   #2차원배열생성
    #print(arr)
    for i in range(c):  #배추위치 1로초기화
        x,y=map(int,input().split())
        arr[y][x]=1
    #print(arr)

    for i in range(n):  #모든 요소에대해서 bfs수행
        for j in range(m):
            if arr[i][j]==1:
                arr[i][j]=0
                bfs(i,j)
    print(count)


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