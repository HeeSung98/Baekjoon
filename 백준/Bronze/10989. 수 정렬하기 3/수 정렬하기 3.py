import sys
input = sys.stdin.readline

n = int(input())

input_list = [0] * (10000 + 1)

for _ in range(n):
    input_list[int(input())] += 1

for i in range(len(input_list)):
    if input_list[i] != 0:
        for _ in range(input_list[i]):
            print(i)