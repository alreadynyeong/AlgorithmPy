import sys
a = [2**i for i in range(32)]

for i in range(int(sys.stdin.readline())):
    print(1 if int(sys.stdin.readline()) in a else 0)