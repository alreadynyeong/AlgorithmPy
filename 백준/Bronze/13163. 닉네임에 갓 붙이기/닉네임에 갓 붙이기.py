n = int(input())

for _ in range(n):
    god = list(map(str, input().split()))
    print('god', end='')
    for i in range(1, len(god)):
        print(god[i], end='')
    print()