def solution(s):
    if s.count('(') != s.count(")"):
        return False
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False

    return True