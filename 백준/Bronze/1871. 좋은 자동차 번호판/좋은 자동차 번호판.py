n = int(input())
for _ in range(n):
    sunn = 0
    eng, num = input().split('-')
    
    for i in range(3):
        sunn += (ord(eng[i])-65)*26**(2-i)
    answer = sunn-int(num)
    print("nice" if answer<=100 and answer >=-100 else "not nice")