n = int(input())
s = input()

if n <=25:
    print(s)
elif '.' not in s[11:-12]:
    print(s[:11]+'.'*3+s[-11:])
else:
    print(s[:9]+'.'*6+s[-10:])