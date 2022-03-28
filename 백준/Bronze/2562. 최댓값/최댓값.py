n = []

for i in range(9):
    n.append(int(input()))

print(max(n))

for i in range(9):
    if max(n)==n[i]:
        print(i+1)