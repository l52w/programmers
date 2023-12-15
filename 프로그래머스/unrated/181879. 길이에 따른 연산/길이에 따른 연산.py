def solution(num_list):
    answer = 0
    from math import prod
    if len(num_list) >= 11 :
        return sum(num_list)
    elif len(num_list) <= 10 :
        return prod(num_list)