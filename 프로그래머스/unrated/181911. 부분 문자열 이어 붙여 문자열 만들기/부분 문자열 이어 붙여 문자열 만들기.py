def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        p = parts[i]
        answer += my_strings[i][p[0]:p[1]+1]
    return answer