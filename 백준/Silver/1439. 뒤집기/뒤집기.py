s = input()
result = 0

for i in range(1, len(s)):
    if(s[i-1] != s[i]):
        result += 1
                
print((result+1)//2)