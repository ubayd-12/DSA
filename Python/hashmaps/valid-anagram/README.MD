# LeetCode Problem: Valid Anagram

## Link:

- [LeetCode Problem Link](https://leetcode.com/problems/valid-anagram/)

## Difficulty:

- Easy

## Key Concepts:

1. Hashmaps

## Things Learned:

- Hashmaps map relationships

## Solution Summary:

- Create a defaultdict with ints
- Pass through each array and
  - For the first run (first arr) append onto the dic the num 1 for each val found (even if found again cap at one)
  - For the second run (second arr) append on the dic the num 2 for each val IFF the val already exists as a one in the dic
- Create a res array and loop through the key value pairs of the dic and if a key has the val 2 append it onto the list
