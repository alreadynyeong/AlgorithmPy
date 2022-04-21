import math, sys
input = sys.stdin.readline

n, m = map(int,input().split())
gem = []
for _ in range(m):
	gem.append(int(input()))
 
def binary_search(low, high):
	a = 999999999
	while low <= high:
		tmp = 0
		mid = (low + high) // 2
		for i in gem:
			tmp += math.ceil(i / mid)
		
		if tmp > n:
			low = mid + 1
		else:
			high = mid - 1
			a = min(a, mid)
	return a
 
print(binary_search(1, max(gem)))