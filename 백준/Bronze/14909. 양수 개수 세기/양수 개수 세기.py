li = list(map(int, input().split()))
result = 0

for i in range(len(li)) :
  if li[i] > 0 :
    result += 1

print(result)