n = int(input())

result = 0
for i in range(n):
    string = str(i)
    tmp = 0
    for token in string:
        tmp += int(token)
    if tmp + i == n:
        result = i
        break

print(result)