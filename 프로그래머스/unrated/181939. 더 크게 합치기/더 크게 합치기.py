def solution(a, b):
    fa = int(str(a)+str(b))
    fb = int(str(b)+str(a))
    return fa if fa>fb else fb