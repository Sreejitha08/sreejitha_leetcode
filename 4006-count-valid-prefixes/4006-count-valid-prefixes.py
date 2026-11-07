class Solution:
    def countValidPrefixes(self, s: str) -> int:
        z=0
        o=0
        c=0
        for i in s:
            if i=='1':
                o+=1
            else:
                z+=1
            if z==o or abs(z-o)==1:
                c+=1
        return c