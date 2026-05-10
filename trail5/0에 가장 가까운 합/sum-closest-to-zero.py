import sys
n = int(input())
a = [0] + list(map(int, input().split()))

INT_MAX = sys.maxsize
a =  sorted(a)


ans = INT_MAX
j = n -1
for i in range(n):
    if i < j :
        ans = min(ans,abs(a[i]+a[j]))
    while i < j -1 and a[i] + a[j] > 0:
        j -=1
        ans = min(ans,abs(a[i] + a[j]))

print(ans)
