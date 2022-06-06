n = int(input())
name = input()
sunn = 0
for i in name:
    sunn += ord(i)-64
print(sunn)