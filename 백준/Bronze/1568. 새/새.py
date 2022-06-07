n = int(input())
time = 0

while n > 0:
    i = 1
    while n - i >= 0:
        n -= i
        i += 1
        time += 1
        
print(time)