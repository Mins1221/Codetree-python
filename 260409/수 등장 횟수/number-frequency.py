n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
cnt = {}

for elem in arr:
    if elem not in cnt:
        cnt[elem] = 1
    else:
        cnt[elem] +=1

for num in nums:
    if num not in cnt:
        print(0, end=" ")
    else:
        print(cnt[num], end = " ")