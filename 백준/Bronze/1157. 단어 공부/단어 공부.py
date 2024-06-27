a = input().upper()
a_list = list(set(a)) # 중복 값 제거 정렬
cnt = []

for i in a_list :
    cnt.append(a.count(i))
if cnt.count(max(cnt)) > 1 :
    print("?")
else :
    print(a_list[cnt.index(max(cnt))])