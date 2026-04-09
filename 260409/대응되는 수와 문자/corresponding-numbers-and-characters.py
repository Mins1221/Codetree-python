n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.
d = {}
for i,elem in enumerate(words):
    d[i+1] = elem

num_to_word = {}
word_to_num = {}
for i, elem in enumerate(words):
    num_to_word[i+1] = elem
    word_to_num[elem] = i+1

for q in queries:
    if q.isdigit():
        print(num_to_word[int(q)])
    else:
        print(word_to_num[q])
