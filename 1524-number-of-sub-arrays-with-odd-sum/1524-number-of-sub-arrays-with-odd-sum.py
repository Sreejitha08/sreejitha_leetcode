class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        m=(10**9)+7
        c=0
        e=1
        o=0
        res=0
        for i in arr:
            c+=i
            if c%2==0:
                res+=o
                e+=1
            else:
                res+=e
                o+=1
        return res%m