import sys

input = sys.stdin.readline

n, m = map(int, input().split())

no_see = set()
no_hear = set()

for i in range(n):
    no_see.add(input().rstrip())

for i in range(m):
    no_hear.add(input().rstrip())

no_see_hear = no_see & no_hear

print(len(no_see_hear))

no_see_hear = sorted(no_see_hear)
for i in no_see_hear:
    print(i)