s = input()
alp = [-1 for i in range(26)]
for i in s:
    if alp[ord(i)-97] != -1:
        continue
    else:
        alp[ord(i)-97] = s.index(i)
print(*alp)