def solution(price) :
    if price >= 500000 :
        return int(price*0.8)
    elif price >= 300000 :
        return int(price*0.9)
    elif price >= 100000 :
        return int(price*0.95)
    else :
        return price
    
#     다른 사람의 풀이
#     def solution(price):
#     if price>=500000:
#         price = price *0.8
#     elif price>=300000:
#         price = price *0.9
#     elif price>=100000:
#         price = price * 0.95
#     return int(price)
