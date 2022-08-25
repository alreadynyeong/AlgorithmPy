n = int(input())
res = [1, 2] + [i for i in range(3, n)] + [997]
print(n)
print(*res)