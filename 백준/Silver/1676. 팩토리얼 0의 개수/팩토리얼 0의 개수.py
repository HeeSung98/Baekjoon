n = int(input())
result = 0

def f(num):
    if num > 1:
        return num * f(num - 1)
    else:
        return 1
        
fact = f(n)

while fact > 0:
    if fact % 10 == 0:
        result = result + 1
    else:
        break
    fact = fact // 10

print(result)