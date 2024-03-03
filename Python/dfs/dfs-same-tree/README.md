# LeetCode Problem: Same Tree (DFS Sol)

## Link:

- [LeetCode Problem Link](https://leetcode.com/problems/same-tree/)

## Difficulty:

- Easy

## Key Concepts:

1. DFS
2. Simultaneously recurse down the tree given two roots
3. At each level if both nodes do not exisit consider them equal (base case)
4. If one node exists but the other doesn't consider this a structurally different tree
5. Check for vals at each level to be identical
6. Recurse down checking at each node whether

## Solution Summary:

- Create a helper DFS
- The DFS helper will take two roots
- Check for
  - Whether both nodes don't exisit
  - Whether one exists and the other doesn't
  - Whether the vals of nodes match
- Recurse down
