import sys
input = sys.stdin.readline

def count(x):
    return x - x//3 - x//5 + x//15

def solve():
    N = int(input())
    lo, hi = 1, N * 2  
    while lo < hi:
        mid = (lo + hi) // 2
        if count(mid) >= N:
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)

solve()


