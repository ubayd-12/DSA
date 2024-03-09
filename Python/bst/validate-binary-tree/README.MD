# LeetCode Problem: Validate Binary Tree

## Link:

- [LeetCode Problem Link](https://leetcode.com/problems/validate-binary-search-tree/)

## Difficulty:

- Medium

## Key Concepts:

1. BST
2. DFS

## Things Learned:

- BST node can be thought of as having bounds:
  - The root node is non bounded (can take any value)
  - Vals to the left of a node are bounded as:
    - Max: Parent
    - Min: Some local lower bound (inherited from ancestors)
  - Vals to the right of a node are bounded as:
    - Max: Some local upper bound (inherited from ancestors)
    - Min: Parent

## Solution Summary:

- Helper
  - Takes: node, lower bound, upper bound
  - Compare each nodes to see if it lies within these bounds
  - When recursing down the left it ensures that the upper bound is set to parent and lower stands
  - When recursing down the right it ensures that the lower bound is set to parent and upper bound stands
- Call helper with root and set bounds infintely maximum and minimum
