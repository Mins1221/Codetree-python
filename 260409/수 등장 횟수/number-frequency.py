n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
num_index = {}
for i, elem in enumerate(arr):
    num_index[i+1] = elem  

count_map = {}
for v in num_index.values():
    if v in count_map:
        count_map[v] += 1
    else:
        count_map[v] = 1

print(' '.join(str(count_map.get(x, 0)) for x in nums))