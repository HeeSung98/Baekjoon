n = int(input())

arr = [0] * n

for i in range(n):
    a, b = map(int, input().split())
    arr[i] = [a, b]

arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])