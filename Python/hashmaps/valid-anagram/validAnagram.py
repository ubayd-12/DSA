from collections import defaultdict
def isAnagram(s, t):
        sD = defaultdict(int)
        for letter in s:
            sD[letter]+=1
        for letter in t:
            if sD[letter] <= 0:
                return False
            sD[letter]-=1
        for key, val in sD.items():
            if val != 0:
                return False
        return True

print(isAnagram("anagram", "nagaram"))