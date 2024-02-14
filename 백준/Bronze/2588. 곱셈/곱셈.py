a = int(input())
b = int(input())
b_list = list(map(int, str(b)))

print(a*b_list[2])
print(a*b_list[1])
print(a*b_list[0])
print(a*b)