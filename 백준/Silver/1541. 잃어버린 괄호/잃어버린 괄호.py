import sys

# 입력 받기
input = sys.stdin.readline
expression = input().strip()

# '-'로 먼저 분리
sub_expressions = expression.split('-')

# 첫 번째 부분은 무조건 더해줌
result = sum(map(int, sub_expressions[0].split('+')))

# 두 번째 부분부터는 전부 더한 후 빼줌
for sub_expr in sub_expressions[1:]:
    result -= sum(map(int, sub_expr.split('+')))

print(result)