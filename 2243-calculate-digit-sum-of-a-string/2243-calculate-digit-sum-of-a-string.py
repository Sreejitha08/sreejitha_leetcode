class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            res=""
            i=0
            while i<len(s):
                c=0
                n=min(k,len(s)-i)
                for j in range(i,i+n):
                    c+=int(s[j])
                res+=str(c)
                i+=n
            s=res
            if len(s)<=k:
                return s
            else:
                s=res
        return s