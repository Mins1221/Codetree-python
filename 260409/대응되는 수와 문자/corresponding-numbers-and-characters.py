n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.
d = {}
for i,elem in enumerate(words):
    d[i+1] = elem

for q in queries:
    if q.isdigit():
        print(d[int(q)])
    else:
        for key, val in d.items():
            if val == q:
                print(key)
                break
