***
![DFS](https://github.com/tmdgns12j/python-algorithm/blob/master/img/DFS%EB%8F%99%EC%9E%91.PNG)

1  
1->2  
1->2->7  
1->2->7->6  
1->2->7->8  
1->3  
1->3->4  
1->3->5


```
#스택구조
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
```

***
