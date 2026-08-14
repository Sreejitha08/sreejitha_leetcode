class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        i=0
        d={}
        maxi=float('-inf')
        for j in range(len(s)):
            if s[j] in d:
                d[s[j]]+=1
            else:
                d[s[j]]=1
            if d[s[j]]>2:
                #i=i+1
                while s[i]!=s[j]:
                    d[s[i]]-=1
                    i+=1
                d[s[i]]-=1
                i+=1
            maxi=max(maxi,j-i+1)
        maxi=max(maxi,j-i+1)
        return maxi  