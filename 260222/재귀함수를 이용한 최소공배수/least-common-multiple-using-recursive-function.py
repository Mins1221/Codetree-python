n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gcd(a, b):          # 최대공약수 (재귀)
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):          # 최소공배수
    return a * b // gcd(a, b)

def lcm_list(arr, index=0):   # 리스트 전체 LCM (재귀)
    if index == len(arr) - 1:
        return arr[index]
    return lcm(arr[index], lcm_list(arr, index + 1))

print(lcm_list(arr, index=0))


