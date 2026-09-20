class Solution:
    def reverseDegree(self, s: str) -> int:
        c=0
        dict={}
        for i in range(122,96,-1):
            dict[chr(i)]=123-i
        for i in range(len(s)):
            c=c+(dict[s[i]]*(i+1))
        return c