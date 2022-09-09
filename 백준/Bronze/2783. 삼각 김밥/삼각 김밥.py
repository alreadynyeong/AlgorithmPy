x, y = map(int, input().split())
m = x * 1000 / y
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    m = min(m, a * 1000 / b)
print(round(m, 2))