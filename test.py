name="JAN"
def solution(name):
    answer=0
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
l=0
for i in t:
    if i=='A':
        l+=1
    else:
        break
print(l)
t=t[::-1]
for i in t:
    if i=='A':
        l+=1
    else:
        break
print(l)