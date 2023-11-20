t = int(input())

for i in range(t):
    n = int(input())
    sell = list(map(int , input().split()))
    tot = 0

    while len(sell) != 0:
        max_index = max(sell)
        now = sell.index(max_index)

        front = sell[:now]
        sell = sell[now+1:]


        for j in range(len(front)):
            tot += abs(front[j] - max_index)
    print(f"#{i + 1} {tot}")