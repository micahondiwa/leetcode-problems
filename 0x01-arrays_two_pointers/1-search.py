def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
            
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

# Examples
nums1 = [-1,0,3,5,9,12]
print(search(nums=nums1, target=9))
print(search(nums=nums1, target=2))
