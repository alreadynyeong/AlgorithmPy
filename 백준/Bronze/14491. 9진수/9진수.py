n = int(input())
ans = ''
t = 0
while 9**t <= n:
    t += 1
for i in range(t-1, -1, -1):
    ans += str(n//(9**i))
    n = n%(9**i)
print(ans)