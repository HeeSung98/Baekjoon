import sys

input = sys.stdin.readline

n, m = map(int,input().split())

dogam = {}
for i in range(1, n + 1):
    poketmon = input().rstrip()
    dogam[str(i)] = poketmon
    dogam[poketmon] = i

for _ in range(m):
    question = input().rstrip()
    print(dogam[question])