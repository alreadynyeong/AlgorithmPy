import sys

n = int(sys.stdin.readline())
cnt = 0

a = sorted(list(map(int, sys.stdin.readline().split())))
b = sorted(list(map(int, sys.stdin.readline().split())))
a.reverse()

for i in a:
    if i >= b[-1]:
        pass
    else:
        cnt += 1
        b.pop()
if cnt > n//2:
    print("YES")
else:
    print("NO")