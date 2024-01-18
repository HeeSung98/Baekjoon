word = input()

result = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

for i in range(len(word)):
    idx = ord(word[i]) - 97
    if result[idx] == -1:
        result[idx] = i

for i in range(0, len(result)):
    print(result[i], end = " ")