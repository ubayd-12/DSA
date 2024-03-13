# LeetCode Problem: Convert Sorted Array to Binary Search Tree

## Link:

- [LeetCode Problem Link](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

## Difficulty:

- Easy

## Key Concepts:

1. BST

## Things Learned:

- The most 'avg' el is in the center of a sorted array
- Everything less than that el should be left of root
- Everything greater than that el should be right of root
- Recurisvely call left and right hand partion of the array on either half, setting the midpoint to said trees root as you recurse

## Solution Summary:

- Base case returns None (i.e an empty array is Null)
- Find midpoint and create a TreeNode using said val
  - Set the left chi
