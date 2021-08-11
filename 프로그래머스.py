#대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

#예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다
def solution(s):
    s=str(s)
    s=s.lower()
    pcount=int(0)
    ycount=int(0)
    for i in range(len(s)) :
        if s[i]=='p' : pcount+=1
        if s[i]=='y' : ycount+=1
    if pcount==ycount :
        return True
    else :
        return False

#함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

def solution(x, n):
    answer=[0]*n
    i=int(0)
    if x>0 :
        for x in range(x,n*x+1,x) :
            if i==n : break
            answer[i]=x
            i+=1
    else :
        for x in range(x,n*x-1,x) :
            if i==n : break
            answer[i]=x
            i+=1
    return answer

#정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요
def solution(arr):
    answer = 0
    answer = sum(arr)/len(arr)
    return answer

#2016년(윤년)
# 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.
def solution(a, b):
    sum=int(0)
    day=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    date=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1) : 
        sum+=date[i]
    sum=sum+b
    sum=sum%7
    
    return day[sum-1]

#신규 아이디 추천
import re
s=".abcdefghijklmn.p"
s=s.lower()#1
for i in s:     #2
    if not i.isalpha() and not i.isdigit() and i!='_' and i!='.' and i!='-':
        s=s.replace(i,'')
s=re.sub('\.\.*','.',s) #3
for i in range(2):
    s=re.sub('^\.|\.$','',s)    #4
    if len(s)==0:   #5
        s='a'
    if len(s)>=16:  #6
        s=s[:15]
    if len(s)<=2:   #7
        s+=s[len(s)-1]*(3-(len(s)))

#Lv2
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