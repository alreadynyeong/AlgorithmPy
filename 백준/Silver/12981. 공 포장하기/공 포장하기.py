cnt = 0

r, g, b = map(int, input().split())

while True:
    if(r==0 and g==0 and b==0):
        break
    elif(r>=1 and g>=1 and b>=1):
        cnt += 1
        r -= 1
        g -= 1
        b -= 1
    elif r>=3:
        cnt += 1
        r -= 3
    elif g>=3:
        cnt += 1
        g -= 3
    elif b>=3:
        cnt += 1
        b -= 3
    elif (r>=1 and g>=1):
        cnt +=1
        r -= 1
        g -= 1 
    elif (g>=1 and b>=1):
        cnt +=1
        g -= 1
        b -= 1 
    elif (r>=1 and b>=1):
        cnt +=1
        r -= 1
        b -= 1 
    elif r>=2:
        cnt += 1
        r -= 2
    elif g>=2:
        cnt += 1
        g -= 2
    elif b>=2:
        cnt += 1
        b -= 2
    elif (r>=1):
        cnt +=1
        r -= 1
    elif (g>=1):
        cnt +=1
        g -= 1
    elif (b>=1):
        cnt +=1
        b -= 1

print(cnt)