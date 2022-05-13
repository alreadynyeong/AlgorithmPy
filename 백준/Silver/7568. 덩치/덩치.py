n = int(input())
arr = []
rank = []

for _ in range(n):
    a, b = map(int, input().split()) 
    arr.append((a, b))

for i in range(n):
    answer = 1
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            answer += 1
    rank.append(answer)
print(*rank, sep='\n')