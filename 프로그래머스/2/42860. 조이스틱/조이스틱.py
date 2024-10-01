def solution(name):
    # 알파벳 변경 횟수 계산
    token_count = [min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name]
    
    # 알파벳 변경 횟수의 총합
    answer = sum(token_count)
    
    n = len(name)
    
    # 좌우 이동 횟수 계산 (최소 이동 횟수)
    min_move = n - 1  # 일직선으로 끝까지 가는 경우
    
    for i in range(n):
        next_idx = i + 1
        
        # 연속된 'A'를 찾는다
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        # 왼쪽으로 갔다가 다시 오른쪽으로 돌아오는 경우를 고려한 최소 이동 계산
        min_move = min(min_move, i + n - next_idx + min(i, n - next_idx))
    
    # 총 결과는 알파벳 변경 횟수 + 좌우 이동 횟수
    answer += min_move
    
    return answer
