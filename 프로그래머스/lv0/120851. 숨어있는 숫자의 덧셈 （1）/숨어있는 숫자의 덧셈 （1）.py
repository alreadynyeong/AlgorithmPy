def solution(my_string):
    answer = sum([int(word) for word in list(my_string) if word.isdigit()])
    
    return answer