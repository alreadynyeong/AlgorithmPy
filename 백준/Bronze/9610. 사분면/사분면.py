import sys
input = sys.stdin.readline

q = [0]*5
for _ in range(int(input())):
    x, y = map(int,input().split())
    if x==0 or y==0:
        q[4] += 1
        continue
    if x > 0:
        if y > 0:
            q[0] += 1
        else:
            q[3] += 1
    else:
        if y > 0:
            q[1] += 1
        else:
            q[2] += 1

print("Q1:", q[0])
print("Q2:", q[1])
print("Q3:", q[2])
print("Q4:", q[3])
print("AXIS:", q[4])