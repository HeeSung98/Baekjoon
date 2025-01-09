import heapq
import sys
input = sys.stdin.read

def main():
    data = input().split()
    N = int(data[0])  # 연산의 개수
    heap = []
    result = []
    
    for i in range(1, N + 1):
        x = int(data[i])
        if x > 0:
            # 자연수 x를 최소 힙에 추가
            heapq.heappush(heap, x)
        elif x == 0:
            if heap:
                # 힙에서 가장 작은 값 출력 및 제거
                result.append(heapq.heappop(heap))
            else:
                # 힙이 비어있으면 0 출력
                result.append(0)
    
    # 결과 출력
    sys.stdout.write('\n'.join(map(str, result)) + '\n')

if __name__ == "__main__":
    main()