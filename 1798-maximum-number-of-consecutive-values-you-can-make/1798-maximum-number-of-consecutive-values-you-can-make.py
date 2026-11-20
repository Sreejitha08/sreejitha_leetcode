class Solution:
    def getMaximumConsecutive(self, c: list[int]) -> int:
        c.sort()
        res=1
        for i in c:
            if i<=res:
                res+=i
            else:
                break
        return res