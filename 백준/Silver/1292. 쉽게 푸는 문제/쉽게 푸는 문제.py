a, b = map(int, input().split())
arr = []
for i in range(1, b*2):
    for j in range(i):
        arr.append(i)
print(sum(arr[a-1:b]))