from collections import deque

def solution(number, k):
    arr = deque()
    
    for num in number:
        while k > 0 and arr and arr[-1] < num:
            arr.pop()
            k -= 1
        arr.append(num)
    
    # 남은 k가 0보다 큰 경우, 뒤에서부터 남은 k개만큼 제거
    for _ in range(k):
        arr.pop()
    
    answer = ''.join(arr)
    
    return answer