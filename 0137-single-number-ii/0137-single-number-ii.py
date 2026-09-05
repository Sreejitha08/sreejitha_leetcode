class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(32):
            c=0
            for j in nums:
                if j&(1<<i):
                    c+=1
            if c%3!=0:
                res|=(1<<i)
        if res>=2**31:
            res-=(2**32)
        return res