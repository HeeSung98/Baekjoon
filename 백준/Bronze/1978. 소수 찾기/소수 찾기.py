n = int(input())

result = 0
input_list = map(int, input().split())
    
for i in input_list:
    flag = 0
    if i > 1:
        for j in range(2, i//2 + 1):
            if i % j == 0:
                flag = 1
        if flag == 0:
            result += 1
            
print(result)
                