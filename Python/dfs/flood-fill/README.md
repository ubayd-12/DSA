# LeetCode Problem: Flood Fill

## Link:

- [LeetCode Problem Link](https://leetcode.com/problems/flood-fill/)

## Difficulty:

- Easy

## Key Concepts:

1. DFS
2. No need for a visited list
   1. Since you are updating cells with the new color and they won't meet recurssion criteria when updated

## Solution Summary:

- Create a helper DFS
- Change incoming cell to new color
- Recurisively check neighbors, and if they exisit and match the color required to become a new color call them recursively
