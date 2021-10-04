#오픈채팅방 dict()
#들어오고 나간 사람을 바뀐이름으로 화면에 출력
record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(record):
    answer=[]
    db=dict()
    for i in range(len(record)):
        record[i]=record[i].split()
        if record[i][0]=="Leave":
            continue
        db[record[i][1]]=record[i][2]
    for i in range(len(record)):
        if record[i][0]=="Enter":
            answer.append("%s님이 들어왔습니다." %db[record[i][1]])
        elif record[i][0]=="Leave":
            answer.append("%s님이 나갔습니다." %db[record[i][1]])
    return answer
print(solution(record))