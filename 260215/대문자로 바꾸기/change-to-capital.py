for _ in range(5):
    arr = list(map(str, input().split()))
    upper_arr = [str.upper() for str in arr]
    print(' '.join(upper_arr))