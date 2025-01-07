import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()  # 입력된 문자열의 공백 제거
result = 0
count = 0

# 문자열 탐색
i = 0
while i < M - 1:
    if S[i:i + 3] == "IOI":  # "IOI" 패턴 확인
        count += 1
        if count == N:  # "IOI" 패턴이 N번 반복되었을 때
            result += 1
            count -= 1  # 겹치는 패턴 처리
        i += 2  # "IOI"는 2칸씩 건너뛰어 탐색
    else:
        count = 0  # 패턴이 끊기면 초기화
        i += 1

print(result)
