n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
num = {}
for i, elem in enumerate(arr):
    num[i+1] = elem  

values = list(num.values())
print(' '.join(str(values.count(x)) for x in nums))
