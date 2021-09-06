#2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
n=int(input())
first=0
second=1
hap=0
for i in range(n):
    if n==0 or n==1:
        print(1)
        break
    else :
        hap=first+second
        second=first
        first=hap
if n!=0 and n!=1:
    print(hap%1234567)

#str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
#예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
def solution(s):
    s=s.replace('"','')
    arr=list(map(int,s.split()))
    answer = str(min(arr))+' '+str(max(arr))
    return answer




#-----------------------------------------------------LV3

# I 숫자 -> 큐에 숫자를 삽입함
# D 1 -> 큐에서 최대값 삭제
# D -1 -> 큐에서 최소값 삭제
# 큐가 비어있으면 [0,0], 비어있지않으면[최대값,최소값] 출력
#원소는 “명령어 데이터” 형식으로 주어집니다. 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
#빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.
operations=["I 7","D -1","D 1","I 5"]
queue=[]
answer=[0,0]
for i in range(len(operations)):
    c,n=operations[i].split()
    if c=='I':
        n=int(n)
        queue.append(n)
    elif c=='D':
        if len(queue)==0:
            continue
        n=int(n)
        if n==1:
            queue.remove(max(queue))
        if n==-1:
            queue.remove(min(queue))

if len(queue)==0:
    print(answer)
else:
    answer[0]=max(queue)
    answer[1]=min(queue)
    print(answer)