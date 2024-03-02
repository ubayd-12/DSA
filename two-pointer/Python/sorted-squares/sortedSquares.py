def sortedSquaresBad(nums):
    for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
    return sorted(nums)

def sortedSquaresEh(nums) :
        l, r = 0, 0
        res = []
        if nums[0] >= 0:
            for i in range(len(nums)):
                nums[i] = nums[i] * nums[i]
            return nums
        elif nums[len(nums)-1] < 0:
            for i in reversed(nums):
                res.append(i * i)
                print(i)
            return res
        else:
            while not (nums[r] >= 0) and r < len(nums) - 1:
                r = r + 1
            l = r - 1
            while r <= len(nums) - 1 and l >= 0:
                if abs(nums[l] * nums[l]) < abs(nums[r] * nums[r]):
                    res.append(nums[l] * nums[l])
                    l = l - 1
                else:
                    res.append(nums[r] * nums[r])
                    r = r + 1
            if r <= len(nums) - 1:
                while r <= len(nums) - 1:
                    res.append(nums[r] * nums[r])
                    r = r + 1
            if l >= 0:
                while l >= 0:
                    res.append(nums[l] * nums[l])
                    l = l - 1
            return res

def sortedSquaresBetter(nums):
        l, r = 0, len(nums) - 1
        res = []
        while l < r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l] * nums[l])
                l+=1
            else:
                res.append(nums[r] * nums[r])
                r-=1
        res.append(nums[l]*nums[l])
        return res[::-1]

arr = [-7,-3,2,3,11]

print(sortedSquaresBad(arr.copy()))
print(sortedSquaresEh(arr.copy()))
print(sortedSquaresBetter(arr.copy()))