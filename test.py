#백준 4963
from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue :
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            

w,h=map(int,input().split())
land=[]
count=int(0)
#  상 하 좌 우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(h):
    land.append(list(map(int,input().split())))
#print(land)
for i in range(h):
    for j in range(w):
        bfs(0,0)