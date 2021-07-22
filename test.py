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

