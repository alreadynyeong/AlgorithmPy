sunn = 0
for n in list(map(int, input().split())):
    sunn += n**2
print(sunn%10)