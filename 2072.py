t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    total = 0
    for j in range(len(arr)):
        if arr[j] % 2 == 1:
            total += arr[j]
    print("#", end = '')
    print(i + 1, end = ' ')
    print(total)