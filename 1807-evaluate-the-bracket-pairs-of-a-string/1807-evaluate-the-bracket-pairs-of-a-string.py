class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        res=""
        i=0
        n=len(s)
        d={}
        for j,k in knowledge:
            d[j]=k
        while i<n:
            if s[i]=="(":
                s1=""
                i+=1
                while s[i]!=")":
                    s1+=s[i]
                    i+=1
                if s1 in d:
                    res+=d[s1]
                else:
                    res+="?"
                i+=1
            else:
                res+=s[i]
                i+=1
        return res