def solution(nums):
    answer = 0
    m = len(nums)/2
    if len(set(nums)) < m:
        answer = len(set(nums))
    else:
        answer = int(m)
    return answer