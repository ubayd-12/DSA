from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = []

    while queue:
        curr = queue.popleft()
        if curr not in visited: # must check due to possibilities of multiple paths to one node
            print(curr, end=" ")
            visited.append(curr)
            for n in graph[curr]:
                if n not in visited:
                    queue.append(n)

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

bfs(graph, 'A')