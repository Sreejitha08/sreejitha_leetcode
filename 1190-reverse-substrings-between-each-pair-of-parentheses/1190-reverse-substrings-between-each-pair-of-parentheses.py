class Solution:
    def reverseParentheses(self, s: str) -> str:
        res=""
        l=[]
        for i in s:
            if i=='(':
                l.append(res)
                res=""
            elif i==")":
                res=res[::-1]
                res=l.pop()+res
            else:
                res+=i
        return res
