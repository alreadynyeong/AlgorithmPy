def solution(order):
    answer = list(str(order))
    return answer.count('3')+answer.count('6')+answer.count('9')