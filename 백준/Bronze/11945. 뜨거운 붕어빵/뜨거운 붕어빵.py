n, m = map(int, input().split())
fish = ['0' for i in range(n)]
for i in range(n):
    fish[i] = input()
    fish[i] = (fish[i])[::-1]
for i in range(n):
    print(fish[i])