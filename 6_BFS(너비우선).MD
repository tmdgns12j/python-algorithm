***
![BFS](https://user-images.githubusercontent.com/69194442/126621871-c70e9d17-4760-4e43-93ba-15a29ca2ffe1.PNG)  
1  
(1) 2, 3, 8  
(2) 3, 8, 7  
(3) 8, 7, 4, 5  
(8) 7, 4, 5  
(7) 4, 5, 6  
(4) 5, 6  
(5) 6  
(6)  
1->2->3->8->7->4->5->6

```
#1. 탐색 시작노드를 큐에삽입하고 방문처리
#2. 큐에서 노드를 꺼낸뒤에 해당 노드의 인접노드 중에서 방문하지않은 노드를 모두 큐에삽입하고 방문처리
from collections import deque
def bfs(graph, start, visited) :
    #deque사용
    queue=deque([start])
    visited[start] = True    #현재노드 방문처리

    while queue:    #큐가 빌때까지 계속
        v=queue.popleft()    #큐에서 하나의 원소를 뽑아 출력
        print(v,end=' ')
        for i in graph[v]:      #아직 방문하지 않은 인접한 원소를 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph=[        #n번노드와 연결되어있는 노드번호를 2차원배열로 구성
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
visited = [False]*9  # 각 노드가 방문된 정보를 표현(리스트)
bfs(graph, 1, visited)
```

***
