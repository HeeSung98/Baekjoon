n = int(input())

start = 1
range = 1
while True:
    if n <= start:
        result = range
        break
    start += 6 * range
    range += 1

print(range)