def dfs(count):
    global answer
 
    if not count:
        temp = int(''.join(numbers))
        if answer < temp:
            answer = temp
        return
 
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            temp_key = int(''.join(numbers))
            print(f"temp_key:{temp_key}")
            if visited.get((temp_key, count - 1), 1):
                visited[(temp_key, count - 1)] = 0
                print(f"visited:{visited}")
                dfs(count - 1)
            numbers[i], numbers[j] = numbers[j], numbers[i]
 
T = int(input())
for t in range(T):
    numbers, num_count = input().split()
    numbers = list(numbers)
    num_count = int(num_count)
    answer = -1
    visited = {}
    dfs(num_count)
    print("#{} {}".format(t + 1, answer))