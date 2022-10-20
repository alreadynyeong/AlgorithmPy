n = int(input())

for _ in range(n):
    nList = list(map(int, input().split()))
    even = []
    for i in nList:
        if i%2==0:
            even.append(i)
    print(sum(even), min(even))