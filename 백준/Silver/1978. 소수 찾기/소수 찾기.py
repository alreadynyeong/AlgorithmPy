n = int(input())
nList = map(int, input().split())
cnt = 0

for x in nList:
    err = 0
    if x>1:
        for i in range(2, x):
            if x%i==0:
                err += 1
        if err == 0:
            cnt += 1

print(cnt)