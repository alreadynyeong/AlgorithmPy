while True:
    cnt = 0
    s = input()
    if s == '#':
        break
    s = list(s.lower())
    print(s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u'))