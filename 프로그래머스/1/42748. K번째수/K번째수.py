def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c[0], c[1], c[2]
        sortedArray = sorted(array[i-1:j])
        answer.append(sortedArray[k-1])
    
    return answer