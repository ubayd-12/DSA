# LeetCode Problem: N/a (Simply applying BFS on array)

## Link:

- N/a

## Difficulty:

- Easy

## Key Concepts:

1. BFS on array

## Things Learned:

- Visited list
- Boudnaries
  - Less than or equal
    - Up
    - Left
  - Greater than or equal
    - Down
    - Right
- Check if curr is in visited since arrays can have cycles

## Solution Summary:

- Use a deque to use popleft()
- Keep track of visited using a tuple
- Add your start location to queue
  - While your queue is full
    - Deque
    - Check if deuqued value not in visited and if so
      - Add unvisited neighbors
