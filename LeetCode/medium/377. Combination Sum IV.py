from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        permut = [0]*(target + 1) # dynamic programming answer array
        permut[0] = 1 # base case, reach 0 in only one way

        for i in range(1, target+1):
            for e in nums:
                if i - e >= 0: #if it can be filled by e
                    permut[i] += permut[i - e] # fill it with the number of ways it can be filed by e.
        
        return permut[-1]