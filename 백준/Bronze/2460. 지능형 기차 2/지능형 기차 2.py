p = max_p = 0
for _ in range(10):
    a, b = map(int, input().split())
    if max_p < p-a+b:
        max_p = p-a+b
    p = p-a+b
print(max_p)