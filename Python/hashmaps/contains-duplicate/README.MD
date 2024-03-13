# LeetCode Problem: Contains Duplicate

## Link:

- [LeetCode Problem Link](https://leetcode.com/problems/contains-duplicate/)

## Difficulty:

- Easy

## Key Concepts:

1. Hashmap

## Things Learned:

- Hashmaps map relationships
- You can set a value to see if you have en

## Solution Summary:

- Helper
  - Takes: node, lower bound, upper bound
  - Compare each nodes to see if it lies within these bounds
  - When recursing down the left it ensures that the upper bound is set to parent and lower stands
  - When recursing down the right it ensures that the lower bound is set to parent and upper bound stands
- Call helper with root and set bounds infintely maximum and minimum
