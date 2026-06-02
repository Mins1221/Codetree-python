m = int(input())
a, b = map(int, input().split())

def count_turns(target, M):
    L, R = 1, M
    turn = 0
    while True:
        mid = (L + R) // 2
        turn += 1
        if mid == target:
            return turn
        elif target < mid:
            R = mid - 1
        else:
            L = mid + 1

min_turns = float('inf')
max_turns = 0

for x in range(a, b+1):
    t = count_turns(x, m)
    min_turns = min(min_turns, t)
    max_turns = max(max_turns, t)

print(min_turns, max_turns)