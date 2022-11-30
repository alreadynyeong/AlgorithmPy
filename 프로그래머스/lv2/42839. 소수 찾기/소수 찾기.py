from itertools import permutations

def is_prime(x):
    if x < 2:
        return False
    
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
        
    return True    

def solution(numbers):
    li = list(numbers)
    temp = []
    answer = []

    for i in range(1, len(li) + 1):
        temp += list(permutations(li, i))
    num = [int(''.join(t)) for t in temp]

    for i in num:
        if is_prime(i):
            answer.append(i)
    return len(set(answer))