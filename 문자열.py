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