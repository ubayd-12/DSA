# LeetCode Problem: Same Tree (BFS Sol)

## Link:

- [LeetCode Problem Link](https://leetcode.com/problems/same-tree/)

## Difficulty:

- Easy

## Key Concepts:

1. BFS

## Things Learned:

- BFS on a tree
- How to flatten a tree into an array
  - Add each node (whether it exists or not) to the queue
  - When visting a node check if it exisits (If it exisits...)
    - Add val to visited
  - If doesn't exisit
    - Add blank space to tree
- NOTE:
  - Since binary trees do not contain cycles no need to check if curr is already in visited, this is necessary for graphs

## Solution Summary:

- Create a helper BFS
- The BFS will return the falttened tree
- Compare the two falttened trees and if they match, same tree
