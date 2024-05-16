from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lstdgt = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[lstdgt] = nums[i]
                lstdgt += 1
        return lstdgt