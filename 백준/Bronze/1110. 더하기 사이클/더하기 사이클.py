n = int(input())
newN = n
cnt = 0

while True:
    f = newN // 10
    s = newN % 10
    
    newN = 10*s + (f+s)%10
    
    cnt += 1
    if n == newN:
        break
    
print(cnt)
