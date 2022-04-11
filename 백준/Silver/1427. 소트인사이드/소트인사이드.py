n = int(input())
nList = list(map(int, str(n)))
nList.sort(reverse=True)
print(*nList, sep='')