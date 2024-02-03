import sys
input = sys.stdin.readline

n = int(input())

input_list = []
for i in range(n):
    input_list.append(int(input()))

input_list.sort()

count_dict = dict()
for i in input_list:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

max_count_dict_value = max(count_dict.values())
max_count_dict_value_list = []

for i in count_dict:
    if count_dict[i] == max_count_dict_value:
        max_count_dict_value_list.append(i)
    
print(round(sum(input_list) / n))
print(input_list[n // 2])

if len(max_count_dict_value_list) > 1:
    print(max_count_dict_value_list[1])
else:
    print(max_count_dict_value_list[0])

print(max(input_list) - min(input_list))