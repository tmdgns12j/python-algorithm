s='happy'
temp=''
alpha='abcdefghijklmnopqrstuvwxyz'
visited=dict()
c=0
for i in alpha:
    visited[i]=-1
print(visited)
for i in range(len(s)):
    if temp==s[i]:
        continue
    temp=s[i]
    if visited[s[i]]!=-1:
        break
    