from collections import defaultdict
# 49. Anagrams
# https://leetcode.com/problems/group-anagrams/
# Use a hashmap to group common anagrams
# key - string containing anagram sorted
# val - all anagrams that match the key
# sort anagrams to compare
def groupAnagrams(strs):
        my_dict = defaultdict(list)
        for i in range(len(strs)):
            # you can sort words and compare them sorted to see if they are anagrams
            s = ''.join(sorted(strs[i]))
            # since we have defaultdict with lists we can just append
            my_dict[s].append(strs[i])
        # return all values in an array where each val is an array
        return my_dict.values()

# Tests
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))