n = int(input())
arr = [0 for _ in range(101)]

l = 0
r = 100000000000
mid = 0

# print(arr)

while l <= r:
    # print(l,r)
    mid = (l + r) // 2

    # 숫자의 개수를 구하는 함수
    cnt = 0

    three = mid // 3
    five = mid // 5
    fifteen = mid // 15

    cnt = mid - three - five + fifteen
    # print("cnt",cnt)

    if cnt < n:
        l = mid + 1
    elif cnt > n:
        r = mid - 1
    else:
        if mid%3 == 0 or mid%5 == 0:
            r= mid-1
        else:
            ans = mid
            break
print(ans)
