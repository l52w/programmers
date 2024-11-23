num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string, N = list(input().split())
string = string[::-1]
answer = 0
for i in range(len(string)):
    answer += (num.index(string[i])) * (int(N) ** i)
print(answer)