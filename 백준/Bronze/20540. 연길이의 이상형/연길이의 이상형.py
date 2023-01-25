s = input()
li = ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']
for i in s:
    li.remove(i)
ans = ''.join(li)
print(ans)