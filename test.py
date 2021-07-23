from collections import deque
def bfs(link,n,infected):
    queue=deque([n])
    infected[n]=True
    while queue:
        n=queue.popleft()
        
    pass


computer=int(input())
connect=int(input())
link=[]
for i in range(connect):
    link.append(list(map(int, input().split())))
infected=[False]*7
bfs(link,0,infected)

