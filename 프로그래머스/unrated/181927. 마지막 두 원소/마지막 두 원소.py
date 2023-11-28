def solution(num_list):
    a = int(num_list[-1])
    b = int(num_list[-2])
    if a > b :
        num_list.append(a - b)
    else:
        num_list.append(2*a)
    return num_list