def printArrInDFS(arr, start):
    dfs(arr, start, [])

def dfs(arr, start, visited):
    print(arr[start[0]][start[1]])
    visited.append(start)
    if start[0] - 1 >= 0 and (start[0] - 1, start[1]) not in visited:
        # up
        dfs(arr, ((start[0] - 1, start[1])), visited)
    if start[0] + 1 <= len(arr) - 1 and (start[0] + 1, start[1]) not in visited:
        # down
        dfs(arr, ((start[0] + 1, start[1])), visited)
    if start[1] - 1 >= 0 and (start[0], start[1] - 1) not in visited:
        # left
        dfs(arr, ((start[0], start[1] - 1)), visited)
    if start[1] + 1 <= len(arr[start[0]]) - 1 and (start[0], start[1] + 1) not in visited:
        # right
        dfs(arr, ((start[0], start[1] + 1)), visited)

arr = [
        [1, 2, 3, 4, 5, 6],
        [8, 9, 10, 11, 12, 13],
        [14, 15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24, 25]
    ]

printArrInDFS(arr, (1, 2))