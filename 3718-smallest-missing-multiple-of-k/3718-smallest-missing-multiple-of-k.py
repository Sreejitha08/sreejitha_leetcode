class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1
        t=True
        while t:
            if k*i not in nums:
                return k*i
            else:
                i+=1
            