# LeetCode Problem: Has Path Sum

## Link:

- [LeetCode Problem Link](https://leetcode.com/problems/path-sum/)

## Difficulty:

- Easy

## Key Concepts:

1. DFS
2. Recursion

## Solution Summary:

- Helper
  - Root, accumilated sum thus far (passed down tree dfs style)
  - If root doesn't exisit
    - Return false
  - Otherwise if leaf node pass sum == targetSum back up the tree
    - If this is true this will return all the way up the call stack as we are using OR operator when returning left and right sub-trees
  - Recursively call helper on left and right subtrees with new accumilated sum
