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