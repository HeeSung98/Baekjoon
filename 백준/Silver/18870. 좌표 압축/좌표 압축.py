import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

diction = {}
tmp = sorted(set(arr))  # 중복 제거 후 정렬

# 좌표 압축 딕셔너리 생성
for counter, value in enumerate(tmp):
    diction[value] = counter

# 결과 저장을 위한 리스트 사용
result = [str(diction[num]) for num in arr]
print(" ".join(result))
