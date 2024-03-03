from collections import deque

def bfs (arr, start):
    q = deque([start])
    visited = []
    while q:
        curr = q.popleft()
        if curr not in visited:
            print(arr[curr[0]][curr[1]])
            visited.append(curr)
            #up
            if curr[0] - 1 >= 0 and (curr[0] - 1, curr[1]) not in visited:
                q.append((curr[0] - 1, curr[1]))
            #down
            if curr[0] + 1 <= len(arr) - 1 and (curr[0] + 1, curr[1]) not in visited:
                q.append((curr[0] + 1, curr[1]))
            #left
            if curr[1] - 1 >= 0 and (curr[0], curr[1] - 1) not in visited:
                q.append((curr[0], curr[1] - 1))
            #right
            if curr[1] + 1 <= len(arr[curr[0]]) - 1 and (curr[0], curr[1] + 1) not in visited:
                q.append((curr[0], curr[1] + 1))

arr = [
        [1, 2, 3, 4, 5, 6],
        [8, 9, 10, 11, 12, 13],
        [14, 15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24, 25]
    ]

start = (1, 2)

bfs(arr, start)