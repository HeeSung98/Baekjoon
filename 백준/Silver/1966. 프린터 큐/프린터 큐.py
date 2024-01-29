count = int(input())

result = []

for i in range(count):
    m, n = map(int, input().split())
    q = list(map(int, input().split()))
    target = n
    ord = 1
    for j in range(m):
        while True:
            if q[0] != max(q):
                q.append(q[0])
                q = q[1:]
                if target == 0:
                    target = len(q) - 1
                else:
                    target -= 1
            else:
                if target == 0:
                    result.append(ord)
                q.pop(0)
                ord += 1
                target -= 1
                break

for i in result:
    print(i)
            
                