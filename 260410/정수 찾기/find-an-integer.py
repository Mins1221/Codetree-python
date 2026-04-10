import sys
n = int(input())

a = list(map(int, sys.stdin.readline().split()))  # 대용량 입력에 더 안정적)

m = int(input())
b = list(map(int, sys.stdin.readline().split()))

# Please write your code here.
s1 = set(a)
s2 = set(b)

for eleml in b:
    if eleml in s1:
        print(1)
    else:
        print(0)  