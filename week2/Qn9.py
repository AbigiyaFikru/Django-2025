def twoSum(nums, target):
    found=False 
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n): 
            if nums[i] + nums[j] == target:
                print([i, j])
                found=True
        
    if found==False:
        print ("not found")
nums1 = [2, 7, 11, 15]
target1 = 20

print(twoSum(nums1, target1))  


