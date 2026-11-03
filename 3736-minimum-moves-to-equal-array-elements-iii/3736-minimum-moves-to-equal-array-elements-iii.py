class Solution:
    def minMoves(self, nums: List[int]) -> int:
        c=0
        maxi=max(nums)
        for i in nums:
            c+=(maxi-i)
        return c