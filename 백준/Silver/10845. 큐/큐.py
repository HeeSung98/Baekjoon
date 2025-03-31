import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
queue = []
result = []
front_index = 0  # pop을 최적화하기 위한 front 포인터

for i in range(1, n + 1):
    command = data[i]
    
    if command.startswith("push"):
        _, value = command.split()
        queue.append(value)
    elif command == "pop":
        if front_index < len(queue):
            result.append(queue[front_index])
            front_index += 1
        else:
            result.append(-1)
    elif command == "size":
        result.append(len(queue) - front_index)
    elif command == "empty":
        result.append(1 if front_index >= len(queue) else 0)
    elif command == "front":
        result.append(queue[front_index] if front_index < len(queue) else -1)
    elif command == "back":
        result.append(queue[-1] if front_index < len(queue) else -1)

sys.stdout.write("\n".join(map(str, result)) + "\n")