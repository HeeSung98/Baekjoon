import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pw_dict = {}

for _ in range(n):
    site, pw = input().split()
    pw_dict[site] = pw

site_list = [0] * m
for i in range(m):
    site_list[i] = input().rstrip()

for i in site_list:
    print(pw_dict[i])