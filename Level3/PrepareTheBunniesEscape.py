from collections import deque

def solution(map):
    row = len(map)
    col = len(map[0])
    src = bfs(0, 0, map)
    dest = bfs(row - 1, col - 1, map)
    res = 20 * 20 + 1
    for i in range(row):
        for j in range(col):
            if src[i][j] and dest[i][j]:
                res = min(res, src[i][j] + dest[i][j] - 1)
                if res == row + col - 1:
                    return res
    return res

def bfs(row, col, m):
    moveto = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows = len(m)
    cols = len(m[0])
    arr = []
    for i in range(rows):
        arr.append([None] * cols)
    arr[row][col] = 1
    queue = deque()
    queue.append((row, col))

    while queue:
        r, c = queue.popleft()
        for dr, dc in moveto:
            nr, nc = (r + dr, c + dc)
            if 0 <= nr and nr < rows and 0 <= nc and nc < cols and arr[nr][nc] is None:
                arr[nr][nc] = arr[r][c] + 1
                if m[nr][nc] != 1:
                    queue.append((nr, nc))
    return arr
    
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
