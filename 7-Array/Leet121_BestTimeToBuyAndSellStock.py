'''

    2021.05.02, Lee Sun Hong

    Python LeetCode Problem 121.
    (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
    
    -
    -       Best Time to Buy and Sell Stock
    -
    
'''


# sys.maxsize, min, max함수를 이용.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mn = sys.maxsize
        
        for price in prices:
            mn = min(mn, price)
            ans = max(ans, price - mn)
        
        return ans
        
        
