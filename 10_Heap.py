#LV2
#더 맵게, 힙 heap() heapq() heapify(), heappush()
#음식의 스코빌지수가 주어진다
#모든 음식의 지수를 K이상으로 만들때 필요한 횟수를 구하여라
#섞은 음식의 지수 = 가장 맵지않은 음식 지수+(두번째로 맵지않은 지수 * 2)
#우선순위큐 가능하지않을까
import heapq
scoville=[1,2]
K=3
def solution(scoville, K):
    heapq.heapify(scoville)#힙으로 변경
    check=0
    answer=0
    for i in scoville:#초기부터 K를 넘을때 처리
        if i>=K:
            check+=1
    if check==len(scoville):
        return 0
    check=0
    while check!=len(scoville):
        c1=heapq.heappop(scoville)#가장 작은값을 빼줌
        c2=heapq.heappop(scoville)
        new=c1+c2*2
        heapq.heappush(scoville, new)
        answer+=1
        for i in scoville:
            if i>=K:
                check+=1
            else:
                check=0
                break
        if check==len(scoville):
            return answer
        elif len(scoville)==1:
            return -1
print(solution(scoville, K))