yut = [sum(map(int, input().split())) for _ in range(3)]
 
for i in yut:
    if i == 3:
        print('A')
    elif i == 2:
        print('B')
    elif i == 1:
        print('C')
    elif not i:
        print('D')
    elif i == 4:
        print('E')