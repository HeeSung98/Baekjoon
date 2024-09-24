def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생이 도난당한 경우를 먼저 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    # 체육복 빌려주기
    for i in sorted(lost_set):
        if i - 1 in reserve_set:
            reserve_set.remove(i - 1)
        elif i + 1 in reserve_set:
            reserve_set.remove(i + 1)
        else:
            n -= 1  # 체육복을 빌리지 못한 경우, 체육 수업을 들을 수 없는 학생 수 감소

    return n