from collections import defaultdict
def intersection(nums1, nums2):
        d = defaultdict(int)
        res = []
        for n in nums1:
            if not d[n]:
                d[n] = 1
        for n in nums2:
            if d[n] == 1:
                res.append(n)
                d[n]-=1
        return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersection(nums1, nums2))