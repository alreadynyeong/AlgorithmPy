def solution(emergency):
    answer = []
    sortedList = sorted(emergency, reverse=True)
    for e in emergency:
        answer.append(sortedList.index(e)+1)
    return answer