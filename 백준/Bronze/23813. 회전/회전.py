n = list(input())
sunn = 0
    
for i in range(len(n)):
    n.insert(0, n[-1])
    del n[-1]
    sunn += int("".join(n))
    
print(sunn)