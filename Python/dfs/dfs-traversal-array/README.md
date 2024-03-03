# LeetCode Problem: N/a (Simply applying DFS on array)

## Link:

- N/a

## Difficulty:

- Easy

## Key Concepts:

1. DFS on array

## Things Learned:

- Visited list
- Boudnaries
  - Less than or equal
    - Up
    - Left
  - Greater than or equal
    - Down
    - Right
-

## Solution Summary:

- Create a helper DFS that takes in
  - arr
  - curr node exploting
  - visited list
- Check if neighbor is in bound and not in visited and if so
  - Explore
- Base case occurs when all nodes have been appended to visited for all nodes within arr
