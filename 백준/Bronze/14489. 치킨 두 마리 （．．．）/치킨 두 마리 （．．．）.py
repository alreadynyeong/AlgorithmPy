a, b = map(int, input().split())

chicken = int(input())

if chicken*2 <= a+b:
    print(a+b-chicken*2)
else:
    print(a+b)