def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [list(intervals[0])]
    for s, e in intervals[1:]:
        if s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return merged

def is_covered(covered, x1, x2):
    """[x1,x2]가 covered의 합집합에 완전히 포함되는지 확인"""
    remaining = [(x1, x2)]
    for a, b in covered:
        new_remaining = []
        for rs, re in remaining:
            if b <= rs or a >= re:          # 겹침 없음
                new_remaining.append((rs, re))
            else:
                if a > rs:                  # 왼쪽 잔여
                    new_remaining.append((rs, a))
                if b < re:                  # 오른쪽 잔여
                    new_remaining.append((b, re))
        remaining = new_remaining
    return len(remaining) == 0              # 잔여 없으면 완전히 덮힘

n = int(input())
segments = []
for _ in range(n):
    y, x1, x2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    segments.append((y, x1, x2))

segments.sort(key=lambda s: s[0])  # y 기준 정렬

covered = []
count = 0
i = 0

while i < len(segments):
    # 같은 y값인 선분들을 묶음
    same_y, y_val = [], segments[i][0]
    while i < len(segments) and segments[i][0] == y_val:
        same_y.append(segments[i])
        i += 1

    # 가시성 판단 (같은 y끼리는 서로 기준에서 제외)
    for y, x1, x2 in same_y:
        if not is_covered(covered, x1, x2):
            count += 1

    # 이후 선분들을 위해 covered에 일괄 추가
    for y, x1, x2 in same_y:
        covered.append([x1, x2])
    covered = merge_intervals(covered)

print(count)