import sys

n,m=map(int, sys.stdin.readline().split())
tmp=list(map(int, sys.stdin.readline().split()))

answer=[0]*(m+1)
for i in tmp:
    answer[i]+=1
print(max(answer))