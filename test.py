

# # 백준 10815
# import sys
# n=int(sys.stdin.readline())
# a=list(map(int,sys.stdin.readline().split()))
# m=int(sys.stdin.readline())
# b=list(map(int,sys.stdin.readline().split()))
# c=[0]*m
# for i in a:
#     if i in b:
#         c[b.index(i)]=1
# for i in range(m):
#     print(c[i],end=' ')