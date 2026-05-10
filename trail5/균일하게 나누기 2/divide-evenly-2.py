N = int(input())
arr = []
Y = set()
for i in range(N):
    arr.append(tuple(map(int, input().split())))
    Y.add(arr[-1][1])

arr.sort()

ans = N
for y_cut in Y:  # y_cut 이하, 초과로 나눈다
    cnt = [0, 0, 0, 0]
    for x, y in arr:
        if y <= y_cut:
            cnt[3] += 1
        else:
            cnt[1] += 1
    
    ans = min(ans, max(cnt))

    for i in range(len(arr)):
        if arr[i][1] <= y_cut:
            cnt[3] -= 1
            cnt[2] += 1
        else:
            cnt[1] -= 1
            cnt[0] += 1
        
        if i == len(arr) - 1 or arr[i][0] != arr[i + 1][0]:
            ans = min(ans, max(cnt))

print(ans)
