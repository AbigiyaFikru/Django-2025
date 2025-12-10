def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n): 
            if nums[i] + nums[j] == target:
                return [i, j]


nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1))  


