len = int(input())
n = int(input())

result = 0

for i in range(len):
    result = result + n % 10
    n = n // 10
    
print(result)