def solution(dot):
    answer = 0
    if (dot[0] < 0)and(dot[1]<0):
        answer = 3
    elif (dot[0]<0)and(dot[1]>0):
        answer = 2
    elif (dot[0]>0)and(dot[1]>0):
        answer = 1
    else :
        answer = 4
    return answer

# 다른 사람의 풀이
# def solution(dot):
#     if dot[0] > 0:
#         if dot[1] > 0:
#             return 1
#         return 4
#     else:
#         if dot[1] > 0:
#             return 2
#         return 3
