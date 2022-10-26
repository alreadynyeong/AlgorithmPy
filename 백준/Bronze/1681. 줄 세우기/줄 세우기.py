import sys
n, l = sys.stdin.readline().split()
n = int(n)
cnt = 0
a = 0
while cnt != n:
    a += 1
    if l in str(a):
        continue
    cnt += 1
print(a)