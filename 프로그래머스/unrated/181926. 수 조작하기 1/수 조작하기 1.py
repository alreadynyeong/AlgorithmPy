def solution(n, control):
    for c in control:
        n += 1 if c=='w' else -1 if c=='s' else 10 if c=='d' else -10 if c=='a' else 0
    return n