class Solution:
    def minOperations(self, s: str) -> int:
        l=list(s)
        l.sort()
        mn=min(s)
        mx=max(s)
        if s==''.join(l):
            return 0
        if len(s)==2:
            return -1
        if s[0]==mn or s[-1]==mx:
            return 1
        for i in range(1,len(s)-1):
            if s[i]==mn or s[i]==mx:
                return 2
        return 3