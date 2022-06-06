n = int(input())
name = []
for _ in range(n):
    name.append(input())

print("뭐야;" if 'anj' in name else "뭐야?")