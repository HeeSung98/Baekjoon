n = int(input())
result = 666
count = 0

while True:
    if "666" in str(result):
        count = count + 1
    if count == n:
        break
    result = result + 1

print(result)