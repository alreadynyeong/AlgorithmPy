n = int(input())
answer = []
for i in range(n):
    a = int(input())
    answer.append(a)
    
answer.sort()
print(*answer, sep='\n')