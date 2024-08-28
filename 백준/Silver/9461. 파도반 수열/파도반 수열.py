import sys

input = sys.stdin.readline

n = int(input())
input_arr = [0] * n

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5
dp[9] = 7
dp[10] = 9

for i in range(n):
    input_arr[i] = int(input())

for i in input_arr:
    if i >= 6:
        for j in range(6, i + 1):
            dp[j] = dp[j-1] + dp[j-5]
    print(dp[i])


