class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        def bt(s,o,c):
            if len(s)==2*n:
                res.append(s)
                return
            if o<n:
                bt(s+"(",o+1,c)
            if o>c:
                bt(s+")",o,c+1)
        bt("",0,0)
        return res