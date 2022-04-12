n = int(input())
answer = []

for i in range(n):
    answer.append(int(input()))

answer.sort()

print(*answer, sep='\n')