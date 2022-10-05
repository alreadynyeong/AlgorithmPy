n = []
people = 0

for _ in range(4):
    a, b = map(int, input().split())
    people += b
    people -= a
    n.append(people)

print(max(n))