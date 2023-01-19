n = int(input())
li = list(map(int, input().split())) + [0] 

ans = []
tmp = []
for i in range(n) :
    tmp.append(li[i])
    if (li[i+1] - li[i]) != 1 :
        ans.append(tmp)
        tmp = []

score = 0
for j in ans :
    score += j[0]

print(score)