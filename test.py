from typing import Collection


from collections import deque
people=[70, 50, 80, 50]
limit=100
print(people)
people.sort()
print(people)# 5 5 7 8
sum=0
queue=deque(people)
while queue:
    if queue[-1]+queue[0]>limit:
        queue.popleft()
        sum+=1
    else :
        