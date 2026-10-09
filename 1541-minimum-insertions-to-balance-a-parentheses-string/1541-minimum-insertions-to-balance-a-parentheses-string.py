class Solution:
    def minInsertions(self, s: str) -> int:
        o=0
        c=0
        n=len(s)
        i=0
        while i<n:
            if s[i]=='(':
                o+=1
            else:
                if i+1<n and s[i+1]==')':
                    i+=1
                else:
                    c+=1
                if o>0:
                    o-=1
                else:
                    c+=1
            i+=1
        return c+2*o