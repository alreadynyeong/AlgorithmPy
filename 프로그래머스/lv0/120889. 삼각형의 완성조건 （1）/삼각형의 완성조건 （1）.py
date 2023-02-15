def solution(sides):
    sides.sort()
    return int(sides[2]>=sides[0]+sides[1])+1