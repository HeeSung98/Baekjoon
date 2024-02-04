import sys
input = sys.stdin.readline

n = int(input())
num_list = []

for i in range(n):
    num_list.append(int(input()))

num_list = set(num_list)
num_list = sorted(num_list)

for i in num_list:
    print(i)
