n,k = map(int, input().split())

x = k*(k+1)//2
if x > n:
    print(-1)
elif (n-x)%k == 0:
    print(k-1)
else:
    print(k)