for i in range(10):
    cnt = int(input())
    arr = list(map(int, input().split()))
    while cnt > 0:
        if max(arr) - min(arr) <= 1:
            break
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
        cnt -= 1
    answer = max(arr) - min(arr)
    print(f"#{i + 1} {answer}")