import sys

input = sys.stdin.readline

def fibonacci_count(n):
    # dp[i][0]은 피보나치 수열의 i번째 값이 0일 때의 호출 횟수
    # dp[i][1]은 피보나치 수열의 i번째 값이 1일 때의 호출 횟수
    dp = [[0, 0] for _ in range(n + 1)]

    if n == 0:
        print("1 0")
        return
    if n == 1:
        print("0 1")
        return
    
    # 기본 초기화
    dp[0] = [1, 0]  # fib(0)을 호출하면 0은 1번, 1은 0번 호출됨
    dp[1] = [0, 1]  # fib(1)을 호출하면 0은 0번, 1은 1번 호출됨



    # 동적 프로그래밍으로 피보나치 수열 계산 및 호출 횟수 기록
    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]  # fib(i)에서 0 호출 횟수
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]  # fib(i)에서 1 호출 횟수
    
    print(str(dp[n][0]) + " " + str(dp[n][1]))

    # n번째 피보나치 수를 계산했을 때 0과 1의 호출 횟수를 반환
    return

# 테스트 예제
    
n = int(input())

input_arr = []

for _ in range(n):
    input_arr.append(int(input()))

for i in input_arr:
    fibonacci_count(i)
    