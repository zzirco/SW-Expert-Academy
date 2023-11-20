T = int(input())
 
dr = [0,1,0,-1]
dc = [1,0,-1,0]
 
for t in range(1, T + 1):
    N = int(input())
    r,c = 0,0
    dir = 0
    snail = [[0] * N for _ in range(N)]
 
    for i in range(1, N*N+1) :
        snail[r][c] = i
        r += dr[dir]
        c += dc[dir]
 
        if r < 0 or c < 0 or r >= N or c >= N or snail[r][c] != 0 :
            r -= dr[dir]
            c -= dc[dir]
 
            dir = (dir + 1) % 4
            r+= dr[dir]
            c+= dc[dir]
 
    print("#{}".format(t))
    for row in snail :
        print(*row)