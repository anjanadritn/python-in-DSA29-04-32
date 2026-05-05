from collections import deque

def rotten(grid):
    r = len(grid)
    c = len(grid[0])
    fresh = 0
    time = 0
    p_r = deque()

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:
                p_r.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1

    d = [(0,1),(0,-1),(1,0),(-1,0)]

    while p_r:
        size = len(p_r)

        for _ in range(size):
            r1, c1 = p_r.popleft()

            for dr, dc in d:
                nr = r1 + dr
                nc = c1 + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    p_r.append((nr, nc))
                    fresh -= 1

        time += 1

    return time - 1 if fresh == 0 else -1


grid = [[2,1,1],[1,0,2],[1,2,0]]
print(rotten(grid))