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


# # 백준 10815
# import sys
# n=int(sys.stdin.readline())
# a=list(map(int,sys.stdin.readline().split()))
# m=int(sys.stdin.readline())
# b=list(map(int,sys.stdin.readline().split()))
# c=[0]*m
# for i in a:
#     if i in b:
#         c[b.index(i)]=1
# for i in range(m):
#     print(c[i],end=' ')

#프로그래머스 LV1 실패율

#프로그래머스 LV1 키패드 누르기
from collections import deque
numbers=[1, 2, 2, 4, 5, 6, 7, 8, 9, 0,0]
hand="right"
ln=[           #왼손일경우 연결노드 *=10, #=11
    [8,10,11], #0번
    [2,4],     #1번
    [1,5],
    [],
    [1,5,7],
    [2,4,8],
    [],
    [4,8,10],
    [5,7,0],
    [],         
    [7,0],      #*번
    []          ##번
]
rn=[            #오른손 연결노드
    [8,10,11],
    [],
    [3,5],
    [2,6],
    [],
    [2,6,8],
    [3,5,9],
    [],
    [5,9,0],
    [6,8,11],
    [],
    [0,9]
]
visited=[False]*13  #방문확인
def solution(numbers, hand):
    def bfs(start,node,visited,end):
        if start==end:
            return 0
        visited=[False]*13
        c=0
        result=0
        queue=deque([start])
        visited[start]=True
        while result==0:
            v=queue.popleft()
            c+=1
            for i in node[v]:# 4 8 10
                if not visited[i]:
                    if i==end:
                        result=c
                        return result
                    queue.append(i)
                    visited[i] = True
    
    ls=10
    rs=11
    for i in range(len(numbers)):
        print(numbers[i])
        if numbers[i] in [1,4,7]:
            ls=numbers[i]
            numbers[i]='L'
        elif numbers[i] in [3,6,9]:
            rs=numbers[i]
            numbers[i]='R'
        else : #mid
            if bfs(ls,ln,visited,numbers[i])>bfs(rs,rn,visited,numbers[i]):
                rs=numbers[i]
                numbers[i]='R'
            elif bfs(ls,ln,visited,numbers[i])<bfs(rs,rn,visited,numbers[i]):
                ls=numbers[i]
                numbers[i]='L'
            else:
                if hand=="right":
                    rs=numbers[i]
                    numbers[i]='R'
                else:
                    ls=numbers[i]
                    numbers[i]='L'
    #print(numbers)
    answer=''
    for i in range(len(numbers)):
        answer+=numbers[i]
    return answer

print(solution(numbers,hand))

#프로그래머스 LV2
#124나라의 숫자
#자연수를 1,2,4로만 표현
#1-1 2-2 3-4 4-11 5-12 6-14 7-21 ...
n = 10
def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n = n // 3
    return answer
print(solution(n))

#LV2
#N개의 최소공배수
arr=[2,6,8,14]
def solution(arr):
    m=max(arr)
    while True :
        c=0
        for i in arr:
            if m%i==0:
                c+=1
            else:
                break
        if c==len(arr):
            break
        m+=1
    return m
print(solution(arr))




#Lv1 상호 평가
scores=[[0,0],[0,0]]
def solution(scores):
    arr=[]
    for i in range(len(scores[0])):
        ma=max(scores[i])
        mi=min(scores[i])
        check1=0
        check2=0
        for k in range(len(scores)):
            if scores[k][i]==ma:
                check1+=1
            elif scores[k][i]==mi:
                check2+=1
        if check1>=2:
            pass
        elif check2>=2:
            pass
        elif scores[i][i]==ma:
            scores[i][i]=0
        elif scores[i][i]==mi:
            scores[i][i]=0
        sum=0
        c=0
        for j in range(len(scores)):
            sum+=scores[j][i]
            if scores[j][i]==0:
                c+=1
        if (len(scores)-c)==0:
            arr.append('F')
        else:   
            avg=sum/(len(scores)-c)

            if avg>=90 :
                arr.append('A')
            elif avg>=80 :
                arr.append('B')
            elif avg>=70 : 
                arr.append('C')
            elif avg>=50 :
                arr.append('D')
            else :
                arr.append('F')
    answer="".join(arr)
    return answer
print(solution(scores))


#LV2조이스틱
name="JAAAAN"
def solution(name):
    answer=0
    c=0
    idx=[0,0]
    start="A"*len(name)
    for i in range(len(start)):
        if ord(name[i])-65<90-ord(name[i]):
            answer=answer+ord(name[i])-65
        else:
            answer=answer+91-ord(name[i])
        if i!=len(name)-1:#마지막에는 옆으로 못감
            answer+=1
    return answer
print(solution(name))

# #백준
# from collections import deque
# n=int(input())
# for i in range(n):
#     command=input()
#     command=command.replace('RR','')
#     c=int(input())
#     arr=input()[1:-1].split(',')
#     queue=deque(arr)
#     if c==0:
#         arr=[]
#     for j in command:
#         if j=='R':
#             arr=arr[::-1]
#         else:
#             if len(arr)==0:
#                 print("error")
#                 break
#             else:
#                 arr.pop(0)
#     else:
#         print('['+','.join(arr)+']')