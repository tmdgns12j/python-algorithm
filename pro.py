from collections import Counter
arr=[3, 3, 3, 3, 3, 3]

def solution(arr):
    temp=[]
    answer=[0]*3
    for i in range(1,4):
        temp.append(arr.count(i))
    print('temp=',temp)
    for i in range(3):
        answer[i]=max(temp)-temp[i]
    return answer
print(solution(arr))



log=["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]
def solution(log):
    time=[]
    sum=0
    answer=[0]*2
    for i in range(len(log)):
        temp=log[i].split(':')
        a=int(temp[0])
        b=int(temp[1])
        time.append(a*60+b)
    for i in range(0,len(time),2):
        if time[i+1]-time[i]>=5:
            if time[i+1]-time[i]>105:
                sum+=105
            else:
                sum+=(time[i+1]-time[i])
    answer[0]=sum//60
    answer[1]=str(sum%60)
    answer[0]="0"+str(answer[0])
    answer=answer[0]+":"+answer[1]
    return answer
print(solution(log))


ings=["r 10", "a 23", "t 124", "k 9"]
menu=["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]
sell=["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]
def solution(ings, menu, sell):
    final=dict()
    price=[]
    for i in range(len(ings)):
        ings[i]=ings[i].split()
    db=dict()
    for i in range(len(menu)):
        menu[i]=menu[i].split()
    # print(menu) 
    for i in range(len(ings)):
        db[ings[i][0]]=ings[i][1]
    # print(db)
    # print(menu[0][1])
    for i in range(len(menu)):
        sum=0
        temp=menu[i][1]
        # print('temp = ',temp)
        for i in temp:
            sum+=int(db[i])
        price.append(sum)
    #print(price)
    
    for i in range(len(menu)):
        final[menu[i][0]]=int(menu[i][2])-price[i]
    #print(final)
    for i in range(len(sell)):
        sell[i]=sell[i].split()
    #print(sell)
    sum=0
    for i in range(len(sell)):
        sum+=final[sell[i][0]]*int(sell[i][1])
    return sum

    # print(menu)
print(solution(ings, menu, sell))




rows=3
columns=3
c=1
def solution(rows, columns):
    def dfs1(x,y):
        global c
        if 0 in visited:
            if visited[x*columns+y]==0:
                visited[x*columns+y]=1
            arr[x][y]=c
            if c%2==1:
                c+=1
                if y+1==columns:
                    dfs1(x,0)
                dfs1(x,y+1)
            else:
                c+=1
                if x+1==rows:
                    dfs1(0,y)
                dfs1(x+1,y)
        else:
            return arr
    
    def dfs2(x,y):
        global c
        if c!=rows*2+1:
            if visited[x*columns+y]==0:
                visited[x*columns+y]=1
            arr[x][y]=c
            if c%2==1:
                c+=1
                if y+1==columns:
                    dfs2(x,0)
                dfs2(x,y+1)
            else:
                c+=1
                if x+1==rows:
                    dfs2(0,y)
                dfs2(x+1,y)
        else:
            return arr

    arr = [[0 for i in range(columns)] for i in range (rows)]
    visited=[0]*(columns*rows)

    x=0
    y=0
    arr[0][0]=1
    if columns!=rows:
        dfs1(x,y)
    else :
        dfs2(x,y)
    return arr
print(solution(rows, columns))


s="aaabbaaa"
def solution(s):
    count=[]
    c=1
    temp=0
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            c+=1
        else:
            count.append(c)
            c=1
        if i==len(s)-1:
            count.append(c)
    if s[0]==s[-1]:
        temp=count[0]+count[-1]
        count.pop()
        count[0]=temp
    count.sort()
    return count
print(solution(s))