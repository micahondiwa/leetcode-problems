def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        m = len(nums2)
        res = []
        
        for i in range(n):
            if nums1[i] in nums2 and nums1[i] not in res:
                res.append(nums1[i])
        for j in range(m):
            if nums2[j] in nums1 and nums2[j] not in res:
                res.append(nums2[j])
        return res
        
        