from typing import List
from numpy import argsort


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort_idx = argsort(nums)

        l = 0
        r = len(nums) - 1

        result = nums[sort_idx[l]] + nums[sort_idx[r]]

        while result != target:
            if result > target:
                r -= 1
            elif result < target:
                l += 1

            result = nums[sort_idx[l]] + nums[sort_idx[r]]

        return sort_idx[l], sort_idx[r]
