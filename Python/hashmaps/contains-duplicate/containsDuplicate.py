from collections import defaultdict
def containsDuplicate(nums):
    d = set()
    for n in nums:
        if n in d:
            return True
        d.add(n)
    return False

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))