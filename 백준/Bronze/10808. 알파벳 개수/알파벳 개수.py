s = input()
alp = [0 for i in range(26)]
for i in s:
    alp[ord(i)-97] += 1
print(*alp)