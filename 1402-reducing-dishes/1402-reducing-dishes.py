class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        res=0
        s=0
        for i in range(len(satisfaction)-1,-1,-1):
            s+=satisfaction[i]
            if s<0:
                return res
            res+=s
        return res