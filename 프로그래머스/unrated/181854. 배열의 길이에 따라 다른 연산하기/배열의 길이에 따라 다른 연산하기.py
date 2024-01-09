def solution(arr, n):
    answer = []
    if len(arr)%2 == 0 :
        for i in range(1,len(arr)+1,2) :
            answer.insert(i,arr[i] + n)
        for i in range(0,len(arr),2) :
            answer.insert(i,arr[i])
    else :
        for i in range(0,len(arr),2) :
            answer.insert(i,arr[i] + n)
        for i in range(1,len(arr),2) :
            answer.insert(i,arr[i])
    return answer