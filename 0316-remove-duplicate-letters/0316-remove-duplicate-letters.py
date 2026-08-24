class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d={}
        for i in range(len(s)):
            d[s[i]]=i
        l=[]
        sett=set()
        for i in range(len(s)):
            if s[i] in sett:
                continue
            while len(l)>0 and s[i]<l[-1] and d[l[-1]]>i:
                sett.remove(l.pop())
            l.append(s[i])
            sett.add(s[i])
        res=""
        for i in l:
            res+=i
        return res