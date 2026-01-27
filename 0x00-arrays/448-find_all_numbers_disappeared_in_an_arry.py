class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sets = set(nums)
        dis = []
        for i in set(i for i in range(1, n + 1)):
            if i not in sets:
                dis.append(i)
        return dis
        