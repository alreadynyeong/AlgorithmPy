def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        answer.append(strArr[i].lower() if i%2==0 else strArr[i].upper())
    return answer