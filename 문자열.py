#백준 10809
answer=''
# test='baekjoon'
test=input()
alpha='abcdefghijklmnopqrstuvwxyz'
count=dict()
for i in range(len(alpha)):
    count[alpha[i]]=-1

for i in range(len(test)):
    if count[test[i]]==-1:
        count[test[i]]=i

for i in alpha:
    answer+=str(count[i])+' '
print(answer)


#백준 1157
#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳출력
#한개가아닐시 ?출력
#set()중복제거, 중복불가자료형
#Counter
from typing import Counter
# s='Mississsiiiisipi'
s=input().lower()
alpha=list(set(s))
a=Counter(s)

max=0
for i in alpha:
    if a[i]>max:
        max=a[i]
c=0
for i in alpha:
    if a[i]==max:
        temp=i
        c+=1
if c==1:
    print(temp.upper())
else:
    print("?")