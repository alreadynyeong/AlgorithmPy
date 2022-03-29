t = int(input())
cnt = 0
for i in range(t):
    cnt = 0
    n , m = map(int, input().split())
    for i in range(n, m+1):
        cnt += str(i).count('0')
    print(cnt)