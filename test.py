# from collections import deque
# a=int(input())#컴퓨터
# b=int(input())#쌍
# n=[list(map(int, input().split())) for i in range(b)]#링크 초기화
# m=[[] for i in range(a+1)]# 노드 재정렬할 배열->컴퓨터+1
# print('n= ',n)
# print('m= ',m)

# ch =[0]*(a+1)#감염체크->컴퓨터+1
# print(ch)
# for i in range(b): # 노드 재정렬
#     x,y=n[i]
#     m[x].append(y)
#     m[y].append(x)
# s=1

# def bfs(s):
#     c=0
#     dq=deque()
#     dq.append(s)
#     ch[s]=1
#     while len(dq)!=0:
#         d=dq.popleft()
#         c+=1
#         for i in m[d]:
#             if ch[i]!=1:
#                 ch[i]=1
#                 dq.append(i)
#     print(c-1)

# bfs(s)
