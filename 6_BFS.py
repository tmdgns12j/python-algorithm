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


#백준 1260
#DFS와 BFS를 수행한 결과를 출력(방문된점 순서를 출력)
# 1. 노드개수 N, 간선개수 M, 시작노드 V
# 2. 출력
#풀이 : 처음풀때는 3 2 3/ 2 3/ 3 1의 경우를 생각못했음 ->[[],[3],[3],[2,1]]
#이럴경우 1이 아닌 2를 먼저 탐색하게되어 틀리게됨
#따라서 배열의 데이터를 정렬해주어야함
#arr :  [[1, 3], [2, 3]] 가장 중요했던과정임
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
    arr[i].sort()# 중요, 입력받은 데이터 정렬
arr.sort() # arr :  [[2, 3], [1, 3]] 이경우를 1,3 2,3 처럼 다시 정렬
#print('arr : ',arr)
for i in range(m):
    x,y=arr[i]
    new[x].append(y)
    new[y].append(x)
#print('new : ',new)
dfs(new,v,visited)
print()
bfs(new,v,visitedd)



#백준 2644
#촌수구하기
# 1. 전체사람수 n 
# 2. 촌수를 계산할 두 사람의 번호
# 3. 부모 자식간의 관계(링크수) m
# 4. 부모 자식 x,y / x는 y의 부모번호
#풀이 : 촌수관계보다는 깊이를 몇번 이동하냐를 구해야함
#while문에 count를 넣어 큐에 등록할때마다 +1해주는 걸로생각했는데
#반례가있었음 
#10
# 7 6
# 9
# 1 2
# 1 3
# 1 4
# 9 1
# 9 10
# 3 5
# 3 6
# 2 7
# 2 8
# 노드를 모두 탐색하면 +1 단 이전노드의 깊이에 +1을 해줘야함
from collections import deque
def bfs(new,v,visited):
    count=int(0)
    queue=deque([v])
    visited[v]=count
    while queue:
        v=queue.popleft()
        #count+=1
        for i in new[v]: 
            if visited[i]==-1:
                visited[i]=visited[v]+1 #중요********
                queue.append(i)

n=int(input())
a,b=map(int,input().split())
m=int(input())
arr=[]
new=[[]for i in range(n+1)]
visited=[-1]*(n+1)
for i in range(m):
    arr.append(list(map(int,input().split())))

for i in range(m):
    x,y=arr[i]
    new[x].append(y)
    new[y].append(x)

bfs(new,a,visited)

if visited[a]==-1 or visited[b]==-1:
    print(int(-1))
else :
    print(int(visited[b]))




#백준 4963
#섬의 개수찾기
#땅은 1 바다는 0
#8방향으로 이동이 가능하다
# 1. 지도의 너비(w) 높이(h) 입력
# 2. 지도 입력
# 3. 너비와 높이가 0 0이면 종료
from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue :
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=h or ny<0 or ny>=w: #범위넘을시 무시
                continue
            if land[nx][ny]==1:
                land[nx][ny]=0
                queue.append((nx,ny))
            
while (1) :
    w,h=map(int,input().split())
    if w==0 or h==0 : break
    land=[]
    count=int(0)
    #  상 하 좌 우 좌상 우상 우하 좌하
    dx=[-1,1,0,0,-1,-1,1,1]
    dy=[0,0,-1,1,-1,1,1,-1]
    for i in range(h):
        land.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if land[i][j]==1:
                land[i][j]=0
                count+=1
                bfs(i,j)
    print(count)



#백준11724
#방향없는 그래프가 주어졌을때 연결요소의 개수구하기
# 1. 정점의개수(n) 간선의개수(m) 입력
# 2. 간선개수만큼 간선입력
# 3. 출력
#풀이 : 그냥 기본적인 bfs임 특별한거없음 
#count해주는 부분만 잘 정해주면 됨
from collections import deque
def bfs(visited,v,new):
    queue=deque([v])
    visited[v]=True
    while queue:
        v=queue.popleft()
        for i in new[v]:
            if visited[i]==False:
                visited[i]=True
                queue.append(i)

n,m=map(int,input().split())#노드 , 간선
arr=[]
new=[[] for i in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    arr.append(list(map(int,input().split())))
    arr[i].sort()
arr.sort()
#print(arr)
for i in range(m):
    x,y=arr[i]
    new[x].append(y)
    new[y].append(x)
#print(new)

count=int(0)
visited[0]=True
for i in range(1,n+1):
    if not visited[i]:
        bfs(visited,i,new)
        count+=1
print(count)


#백준 7576
#토마토 재배하기
#익은토마토(1)이 주어지며
#하루가 지날때마다 익은토마토의 상하좌우의 안익은토마토가 익게된다
#전부 익는데 며칠이 필요할까 / 안익은곳이 한곳이라도 있다면 -1이 출력
# 1. 가로칸(m), 세로칸(n) 입력
# 2. 토마토 판 입력/ 익은건1 익지않은건0 빈곳-1
# 3. 출력
#풀이 : 1이 여러곳이 주어지는 상황을 첫번째로생각해야함
#걸리는 날짜는 탐색했을때 전 노드의 +1값
from collections import deque
def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tomato[nx][ny]==0: #토마토가 익은날짜 계산
                tomato[nx][ny]=tomato[x][y]+1 #전날익은 토마토값에 +1
                queue.append((nx,ny))

m,n=map(int,input().split())#가로칸, 세로칸
tomato=[]
count=int(0)
dx=[-1,1,0,0]#상하좌우
dy=[0,0,-1,1]
for i in range(n):
    tomato.append(list(map(int,input().split())))
queue=deque()

for i in range(n): #1이 여러개 주어질때를 해결하기 위함 
    for j in range(m):
        if tomato[i][j]==1:
            queue.append((i,j))
bfs()
#print(tomato)
for i in range(n):
    for j in range(m):
        if tomato[i][j]>=count:
            count=tomato[i][j]
        if tomato[i][j]==0:
            print(-1)
            exit()
print(count-1)



#백준7562
#나이트가 몇번 움직여야 목표로하는 칸에 갈수있을까
# 1. 테스트케이스(t) 개수 입력
# 2. 체스판 한변의 길이(l)/ 체스판은 l * l
# 3. 나이트가 현재있는칸 입력
# 4. 나이트의 목표칸 입력
from collections import deque
def bfs(a,b):
    queue=deque()
    queue.append((a,b))
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=l or ny<0 or ny>=l:
                continue
            if chess[nx][ny]==0:
                chess[nx][ny]=chess[x][y]+1
                queue.append((nx,ny))


dx=[-2, -2, -1, -1, 1, 1, 2, 2]#나이트가 움직일수 있는 방향
dy=[-1, 1, -2, 2, -2, 2, -1, 1]
t=int(input())  #테스트 케이스
for i in range(t):
    l=int(input())  #체스판 l
    chess=[[0]*l for i in range(l)]
    #print(chess)
    n,m=map(int,input().split())#시작
    x,y=map(int,input().split())#끝
    chess[n][m]=1

    bfs(n,m)
    print(chess[x][y]-1)