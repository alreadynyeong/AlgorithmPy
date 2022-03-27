import sys

n = int(sys.stdin.readline())
side = []

for i in range(n):
    side.append(int(sys.stdin.readline()))
    
side.sort()


for i in range(len(side)-1, 1, -1):
    if side[i] < side[i-1]+side[i-2]:
        print(side[i]+side[i-1]+side[i-2])
        quit()
print(-1)