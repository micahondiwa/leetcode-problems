def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pointer = 0
        while pointer <= len(nums)-1:
            if nums[pointer] != val:
                pointer += 1
            else:
                del nums[pointer]
        return len(nums)