def solution(my_string, s, e):
    answer = my_string[s:e+1][::-1]
    return my_string.replace(my_string[s:e+1],answer)