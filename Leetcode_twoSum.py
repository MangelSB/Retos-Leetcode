def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for x in range(0, len(nums)):
        y = x + 1
        for y in range(0, len(nums)):
            if (nums[y] == target - nums[x]) and (x != y):
                lista= [x, y]
                return lista

nums = [10, 5, 2, 0 ,3]

print(twoSum(nums, 12))



