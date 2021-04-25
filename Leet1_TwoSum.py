'''

    2021.04.25, Lee Sun Hong

    Python LeetCode Problem 1.
    (https://leetcode.com/problems/two-sum/)
    
    -
    -       Two Sum
    -
    
'''

# Brute Force 를 이용한 풀이.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, val1 in enumerate(nums):
            for idx2, val2 in enumerate(nums):
                if idx1 != idx2 and val1+val2 == target:
                    return [idx1, idx2]
