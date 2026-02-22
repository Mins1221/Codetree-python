n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def lcm_list(arr, multiple=1):
    # 모든 수로 나누어 떨어지면 최소공배수
    if all(multiple % n == 0 for n in arr):
        return multiple
    return lcm_list(arr, multiple + 1)

result = lcm_list(arr)
print(result)


