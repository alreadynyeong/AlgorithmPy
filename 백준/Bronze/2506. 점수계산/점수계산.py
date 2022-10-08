n = int(input())
li = input().split('0')
ans = 0
for s in li:
    cnt = s.count('1')
    if cnt > 0:
        ans += cnt*(cnt+1) // 2
print(ans)