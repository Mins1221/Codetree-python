import sys
n = int(input())
a = list(map(int, input().split()))

INT_MAX = sys.maxsize
a = [0] + sorted(a)


ans = INT_MAX
j = n
for i in range(1,n+1):
    if i < j :
        ans = min(ans,abs(a[i]+a[j]))
    while i < j -1 and a[i] + a[j] > 0:
        j -=1
        ans = min(ans,abs(a[i] + a[j]))

print(ans)
