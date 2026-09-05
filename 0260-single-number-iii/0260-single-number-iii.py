class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c=0
        for i in nums:
            c^=i
        d=c&-c
        a=0
        b=0
        for i in nums:
            if d&i:
                a^=i
            else:
                b^=i
        return [a,b]