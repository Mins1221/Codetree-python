K, N = map(int, input().split())
answer = []
# Please write your code here.
def print_answer():
    for elem in answer:
        print(elem,end=" ")
    print()

def c(num):
    if num == N+1:
        print_answer()
        return

    for select in range(1,K+1):
        answer.append(select)
        c(num+1)
        answer.pop()

    return

c(1)
print_answer()