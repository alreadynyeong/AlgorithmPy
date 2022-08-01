c = int(input())
m = 0

for _ in range(c):
    s = input()
    cnt = 0

    cnt += s.count("for")
    cnt += s.count("while")

    if cnt>m:
        m = cnt

print(m)