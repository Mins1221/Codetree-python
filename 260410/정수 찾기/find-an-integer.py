n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# Please write your code here.
s1 = set(a)
s2 = set(b)

for eleml in s2:
    if eleml in s1:
        print(1)
    else:
        print(0)  