n = int(input())
li = [input() for _ in range(n)]
k = int(input())
 
if k == 1:    # 원본 출력
    print(*li, sep='\n')
elif k == 2:    # 좌우 반전
    print(*[i[::-1] for i in li], sep='\n')
else:    # 상하 반전
    print(*li[::-1], sep='\n')