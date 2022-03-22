rgb = list(map(int, input().split()))
cnt = 0

for i in range(min(rgb)):
    for j in range(3):
        rgb[j] -= 1
        cnt += 1
    
for i in range(3):
    while rgb[i] >= 3:
        rgb[i] -= 3
        cnt += 1

for i in range(3):
    if rgb[i] == 2:
        rgb[i] -= 2
        cnt += 1

if max(rgb)==1:
    cnt += 1

print(cnt)
