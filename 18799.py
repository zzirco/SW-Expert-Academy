import sys
from itertools import combinations
input = sys.stdin.readline

t = int(input())
arr_n = []
arr = []
for i in range(t):
    arr_n.append(int(input()))
    arr.append(list(map(int, input().split())))

subsets = []
for i in range(t):
    result = []
    for j in range(1, len(arr[i]) + 1):
        result += list(combinations(arr[i], j))
    subsets.append(result)

avg = []
for i in range(t):
    total = 0
    cnt = 0
    for j in range(len(subsets[i])):
        total += sum(subsets[i][j])
        cnt += len(subsets[i][j])
    avg.append(total/cnt)

for i in range(len(avg)):
    integer = int(avg[i])
    f = avg[i] - integer
    if f == 0:
        print("#" + str(i + 1), "{:g}".format(round(avg[i], 20)))
    else:
        print("#" + str(i + 1), round(avg[i], 20))