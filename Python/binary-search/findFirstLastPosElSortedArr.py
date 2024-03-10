def searchRange(nums, target):
        def searchStart():
            l, r = 0, len(nums)-1
            index = -1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] == target:
                    index = mid
                    r = mid - 1
            return index
        def searchEnd():
            l, r = 0, len(nums)-1
            index = -1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] == target:
                    index = mid
                    l = mid + 1
            return index
        return [searchStart(), searchEnd()]

print(searchRange([5,7,7,8,8,10], 8))