import sys

input = sys.stdin.readline

n = int(input())
input_arr = [0] * n

for i in range(n):
    input_arr[i] = int(input())

dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in input_arr:
    if i >= 4:
        for j in range(4, i + 1):
            dp[j] = dp[j-3] + dp[j-2] + dp[j-1]
    print(dp[i])



