import sys

def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    T = list(map(int, data[2:2 + n]))

    # 최댓값을 limit 이하로 맞출 수 있는지 판정
    def check(limit):
        lanes = 1   # 사용 중인 레인 수
        cur = 0     # 현재 레인의 누적 시간
        for t in T:
            if cur + t > limit:   # 이 사람을 넣으면 limit 초과
                lanes += 1        # 새 레인 시작
                cur = t           # 현재 사람부터 다시 누적
            else:
                cur += t
        return lanes <= m

    lo, hi = max(T), sum(T)       # 답의 범위
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid              # 가능 → 더 줄여보기
        else:
            lo = mid + 1          # 불가능 → 늘려야 함
    print(lo)

main()