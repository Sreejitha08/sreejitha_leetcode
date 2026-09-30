class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        c=-1
        res=[]
        for i in seq:
            if i=='(':
                c+=1
                res.append(c%2)
            else:
                res.append(c%2)
                c-=1
        return res