def solution(my_string):
    li= ['a','e','i','o','u']
    for char in li:
        my_string = my_string.replace(char, '')
    return my_string