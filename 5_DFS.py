#1.DFS기초
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