#백준 2206 미해결
# from collections import deque
# def bfs(x,y):
#     queue=deque()
#     queue.append((x,y))
#     arr[x][y]=2
#     while queue:
#         x,y=queue.popleft()
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if nx<0 or nx>=n or ny<0 or ny>=m:
#                 continue
#             if arr[nx][ny]==0:
#                 arr[nx][ny]=arr[x][y]+1
#                 queue.append((nx,ny))
            

# n,m=map(int,input().split())    #행 열
# arr=[]
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
# for i in range(n):
#     arr.append(list(map(int,input().strip())))  #strip()
# #print(arr)

# bfs(0,0)
# print(arr)