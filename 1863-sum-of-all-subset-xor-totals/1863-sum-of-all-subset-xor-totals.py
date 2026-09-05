class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        for i in range(1<<n):
            xor=0
            for j in range(n):
                if i&(1<<j):
                    xor^=nums[j]
            c+=xor
        return c