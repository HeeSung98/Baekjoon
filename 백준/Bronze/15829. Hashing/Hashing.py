n = int(input())
input_text = input()

result = 0
count = 0
for token in input_text:
    result += (int(ord(token)) - 96) * 31 ** count
    count += 1

print(result)
