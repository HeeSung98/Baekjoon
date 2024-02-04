n = int(input())


result = []
for i in range(n):
    a = int(input())
    b = int(input())
    floor_0 = [x for x in range(1, b + 1)]

    for j in range(a):
        for k in range(1, b):
            floor_0[k] += floor_0[k - 1]

    result.append(floor_0[-1])

for i in result:
    print(i)