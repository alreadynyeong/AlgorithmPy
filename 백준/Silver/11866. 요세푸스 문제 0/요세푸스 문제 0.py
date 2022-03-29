from collections import deque

n, k = map(int, input().split())
queue = deque()

for i in range(n):
    queue.append(i+1)
    

print('<', end='')
while queue:
    for i in range(k-1):
        queue.append(queue[0])
        queue.popleft()
    print(queue.popleft(), end='')
    if queue:
        print(', ', end='')
    
print('>')