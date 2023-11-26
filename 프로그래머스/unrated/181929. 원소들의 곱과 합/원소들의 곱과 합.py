def solution(num_list):
    answer = 0
    a,b,c = 0,0,1

    a = sum(num_list)**2
    for i in range(len(num_list)) :
        b = c*num_list[i]
        c = b
    if a > c :
        return 1
    else :
        return 0