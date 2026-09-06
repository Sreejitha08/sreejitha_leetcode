class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res=0
        for i in range(31,-1,-1):
            pre=set()
            opt=res|1<<i
            target=opt>>i
            for j in nums:
                pre.add(j>>i)
            for j in pre:
                need=j^target
                if need in pre:
                    res=opt
                    break
        return res