class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        c1=0
        res=""
        mini=float('inf')
        i=0
        for j in range(len(s)):
            if s[j]=="1":
                c1+=1
            while c1==k:
                while i<j and s[i]=='0':
                    i+=1
                l=(j-i+1)
                if l<mini:
                    res=s[i:j+1]
                    mini=l
                if l==mini:
                    res=min(res,s[i:j+1])
                
                if s[i]=='1':
                    c1-=1
                i+=1
        return res