def binary_search(t, d):
    s = 0
    e = len(d)-1
    r = -1
    
    while s<=e:
        mid = (s+e)//2
        if d[mid] < t:
            r = mid
            s = mid + 1
        else:
            e = mid -1
    return r


n = int(input())


for _ in range(n):
    cnt = 0
    
    a, b = map(int, input().split())
    aList = sorted(list(map(int, input().split())))
    bList = sorted(list(map(int, input().split())))
    
    for i in aList:
        cnt += binary_search(i, bList)+1
        
    print(cnt)