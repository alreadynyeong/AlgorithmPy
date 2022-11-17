a, b, c, d = map(int, input().split())
li = list(map(int, input().split()))
for n in li:
    att = 0
    if 0 < n % (a+b) <= a:
        att += 1
    if 0 < n % (c+d) <= c:
        att += 1
    print(att)