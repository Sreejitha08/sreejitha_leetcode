class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        j=0
        c0=0
        c1=0
        count=0
        i=0
        a=[0]*len(s)
        while j<len(s):
            if a[j]==0:
                if s[j]=='1':
                    c1+=1
                else:
                    c0+=1
            a[j]=1
            if c0<=k or c1<=k:
                count+=(j-i+1)
                j+=1
            else:
                if s[i]=='0':
                    c0-=1
                else:
                    c1-=1
                i+=1
        return count