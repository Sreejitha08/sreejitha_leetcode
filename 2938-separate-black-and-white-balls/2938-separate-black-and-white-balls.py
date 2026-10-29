class Solution:
    def minimumSteps(self, s: str) -> int:
        o=0
        res=0
        for i in s:
            if i=='1':
                o+=1
            else:
                res+=o
        return res