n = list(input())
n.sort(reverse=True)
sunn = 0

if "0" not in n:
    print(-1)
else:
    for i in n:
        sunn += int(i)
    if sunn%3==0:
        print("".join(n))
    else:
        print(-1)