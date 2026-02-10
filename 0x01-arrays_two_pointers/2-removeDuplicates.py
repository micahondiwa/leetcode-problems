def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 1

        while fast <= len(nums) - 1:
            if nums[slow] != nums[fast]:
                slow += 1
                fast += 1
            else:
                del nums[fast]
        return len(nums)
