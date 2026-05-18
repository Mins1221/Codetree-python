import sys
n = int(input())
a =   list(map(int, input().split()))
INT_MIN = -sys.maxsize
ans = INT_MIN
curr_sum = INT_MIN
for i in a:
    curr_sum =max(curr_sum+i ,i)
    if curr_sum > ans :
        ans = max(ans,curr_sum)
print(ans)
