a, b, c = 0, 0, 0
T = int(input())

while(T>=300):
    a = a+1
    T = T-300
    
while(T>=60):
    b = b+1
    T = T-60  
    
while(T>=10):
    c = c+1
    T = T-10

if(T==0):
    print(a, b, c)
else:
    print(-1)