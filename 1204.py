t = int(input())
for k in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    check = [0 for _ in range(1001)]
    for j in range(1000):
        check[arr[j]] += 1
    m = max(check)
    max_arr = [i for i, v in enumerate(check) if v == m]
    print(f"#{k + 1} {max(max_arr)}")