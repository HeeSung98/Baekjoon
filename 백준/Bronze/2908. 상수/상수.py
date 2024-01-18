a, b = input().split(' ')
sangsu_a, sangsu_b = "", ""

for i in range(len(a)):
    sangsu_a = sangsu_a + a[len(a) - i - 1]

for i in range(len(b)):
    sangsu_b = sangsu_b + b[len(b) - i - 1]

map(int, sangsu_a, sangsu_b)

if sangsu_a > sangsu_b:
    print(sangsu_a)
else:
    print(sangsu_b)