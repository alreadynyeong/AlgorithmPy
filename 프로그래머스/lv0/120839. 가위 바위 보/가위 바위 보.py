def solution(rsp):
    answer = ''
    for c in rsp:
        answer += '0' if c=='2' else '2' if c=='5' else '5'
    return answer