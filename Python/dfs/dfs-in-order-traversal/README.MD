# LeetCode Problem: Binary Tree In Order Traversal

## Link:

- [LeetCode Problem Link](https://leetcode.com/problems/binary-tree-inorder-traversal)

## Difficulty:

- Easy

## Key Concepts:

1. DFS
2. Tree Traversals

## Things Learned:

- Differences between how to traverse a binary tree
  - In Order
    - Left
    - Root
    - Right
  - Pre Order
    - Root
    - Left
    - Right
  - Post Order
    - Left
    - Right
    - Root
- The differences between the implementation for each is what you do during each recusive call
  - Do you go immediately go left/right or do you do some sort of action at the current node (i.e root of given binary tree)

## Solution Summary:

- Helper dfs
- Global result instance var
- If current node exisit then:
  - Left
  - Append
  - Right
