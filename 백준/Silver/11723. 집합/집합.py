import sys

input = sys.stdin.readline

S = 0b0

for _ in range(int(input())):
    order = input().strip()
    if " " in order:
        order, value = order.split()
        value = int(value) - 1

    if order == "add":
        S = S | (0b1 << value)

    elif order == "remove":
        S = S & ~(0b1 << value)

    elif order == "check":
        if S & (0b1 << value):
            print("1")
        else:
            print("0")

    elif order == "toggle":
        S = S ^ (0b1 << value)

    elif order == "all":
        S = 0b11111111111111111111

    elif order == "empty":
        S = 0b0