def solution(n):
    list1 = [i for i in range(1, n+1, 2)]
    list2 = [i*i for i in range(2, n+1, 2)]
    return sum(list1 if n%2==1 else list2)