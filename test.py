from collections import Counter
lottos=[44, 1, 0, 0, 31, 25]
win_nums=[31, 10, 45, 1, 6, 19]
win_nums.sort()
print(win_nums)
start=0
end=len(lottos)
c=0
answer=[]
max=0
min=0
def binary(start,end,i):
    global c
    mid=(start+end)//2
    if start>end:
        return 0
    if win_nums[mid] == i:
        c+=1
    elif win_nums[mid]>= i:
        binary(start,mid-1,i)
    else:
        binary(mid+1,end,i)
    

for i in lottos:
    binary(start,end,i)
print(c)
N=Counter(lottos)
if N[0]+c==6