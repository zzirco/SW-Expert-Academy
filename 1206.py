for k in range(10):
    n = int(input())
    arr = [[0] * n for _ in range(255)]
    height = list(map(int, input().split()))
    for i in range(n):
        for j in range(height[i]):
            arr[254 - j][i] = 1

    cnt = 0
    for i in range(2, n - 2):
        for j in range(height[i]):
            current = arr[254 - j][i]
            if current == 1:
                l1 = arr[254 - j][i - 1]
                l2 = arr[254 - j][i - 2]
                r1 = arr[254 - j][i + 1]
                r2 = arr[254 - j][i + 2]
                if l1 == 0 and l2 == 0 and r1 == 0 and r2 == 0:
                    cnt += 1
            else:
                continue

    print("#" + str(k + 1), cnt)