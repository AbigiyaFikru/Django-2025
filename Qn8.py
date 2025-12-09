def moveZeroes(nums):
    last_non_zero = 0  

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1

    for i in range(last_non_zero, len(nums)):
        nums[i] = 0

nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(nums1)
