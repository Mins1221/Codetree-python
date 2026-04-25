n = int(input())

s= set()
for _ in range(n):
    cmd, val = input().split()
    if cmd =="add":
        s.add(val)
    if cmd =="remove":
        s.remove(val)
    if cmd =="find":
        if val in s:
            print("true")
        else:
            print("false")

# Please write your code here.
