# LeetCode Problem: Average Levels of Binary Tree

## Link:

- [LeetCode Problem Link](https://leetcode.com/problems/average-of-levels-in-binary-tree)

## Difficulty:

- Easy

## Key Concepts:

1. DFS
2. Categorizing nodes by level

## Solution Summary:

- Helper
  - Params:
    - Root
    - Level
      - Inc as you go down to keep track of what level you are at
  - For each level you are at add to the list value in the dic representing that level in the binary tree
- After the helper runs you will have a dictionary where all values are all nodes at given level
- Using statistics.mean on a list to return the average of each level
