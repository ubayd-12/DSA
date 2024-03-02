# LeetCode Problem: Sorted Squares

## Link:

- [LeetCode Problem Link](https://leetcode.com/problems/squares-of-a-sorted-array/)

## Difficulty:

- Easy

## Key Concepts:

1. Two Pointer

## Things Learned:

- Use to your advantage the characteristics of the array
  - In this case the array is sorted in non-decreasing (i.e increasing) order
  - This means the magnitudes of those arrays on the far left and right are the greatest

## Solution Summary:

- Two pointers set on opposite sides of the array
- Based on the largest element between the left and right pointers and the respective element's square to a resulting array
  - Inc both arrays up one and down one respectively
- At the end you will have an array in decrasing order
