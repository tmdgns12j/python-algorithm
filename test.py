# #백준 1260 오류 미해결
# from collections import deque
# def dfs(new,v,visited):
#     visited[v]=True
#     print(v,end=" ")
#     for i in new[v]:
#         if not visited[i]:
#             visited[i]=True
#             dfs(new,i,visited)


# def bfs(new,v,visitedd):
#     queue=deque([v])
#     visitedd[v]=True
#     while queue:
#         v=queue.popleft()
#         print(v,end=" ")
#         for i in new[v]:
#             if not visitedd[i]:
#                 visitedd[i]=True
#                 queue.append(i)

# n, m, v=map(int,input().split())
# arr=[]
# visited=[False]*(n+1)
# visitedd=[False]*(n+1)
# new=[[]for i in range(n+1)]
# for i in range(m):
#     arr.append(list(map(int,input().split())))
#     arr.sort()
# #print(arr)
# for i in range(m):
#     x,y=arr[i]
#     new[x].append(y)
#     new[y].append(x)
# #print(new)
# dfs(new,v,visited)
# print()
# bfs(new,v,visitedd)