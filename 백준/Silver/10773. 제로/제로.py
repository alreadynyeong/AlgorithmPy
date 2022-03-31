k = int(input())
kList = []
for _ in range(k):
    n = int(input())
    if n == 0:
        kList.pop()
    else:
        kList.append(n)
print(sum(kList))