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