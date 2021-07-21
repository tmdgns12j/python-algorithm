def dfs(graph, v, visited) :
    visited[v]=True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i] :
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