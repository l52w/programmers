def solution(arr, queries):
    for i,j in queries :
        for i in range(i,j+1):
            arr[i] += 1
    return arr