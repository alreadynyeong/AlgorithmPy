n = int(input())
star = [[' ' for _ in range(4*n-3)] for _ in range(4*n-3)]

def stars(n, x, y):
    if n == 1:
        star[y][x] = '*'
        return
    
    l = 4*n - 3
    
    for i in range(l):
        star[y][x+i] = '*'
        star[y+i][x] = '*'
        star[y+l-1][x+i] = '*'
        star[y+i][x+l-1] = '*'
        
    stars(n-1, x+2, y+2)
    
stars(n, 0, 0)
for j in star:
    print(''.join(j))