s = int(input())
b = 0

while s>=0:
    if s%5==0:
        print(b+s//5)
        break
    else:
        s -=3
        b +=1
else:
    print(-1)