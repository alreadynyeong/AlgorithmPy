n = int(input())
li = [2**i for i in range(31)]

if n in li:
    print(1)
else:
    print(0)