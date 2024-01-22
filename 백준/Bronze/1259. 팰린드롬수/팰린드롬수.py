input_list = []

while True:
    n = input()
    if n == '0':
        break
    else:
         input_list.append(n)

for j in range(len(input_list)):
    result = "yes"
    for i in range(len(input_list[j]) // 2):
            if input_list[j][i] != input_list[j][len(input_list[j]) - i - 1]:
                result = "no"
                break
    print(result)       
    