n = int(input())
li = list(map(int, input().split()))
s = len(list(set(li)))
print(n-s)