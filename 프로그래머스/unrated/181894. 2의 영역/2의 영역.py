def solution(arr):
    answer = []
    if arr.count(2) == 0 :
        answer = [-1]
    elif arr.count(2) == 1 :
        answer = [2]
    elif arr.count(2) == 2 :
        a,b= ([i for i, value in enumerate(arr) if value == 2])
        answer = arr[a:b+1]
    else :
        a = min([i for i, value in enumerate(arr) if value == 2])
        b = max([i for i, value in enumerate(arr) if value == 2])
        answer = arr[a:b+1]
    return answer