class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        res=""
        c=s.count(y)
        res+=(y*c)
        for i in s:
            if i!=y:
                res+=i
        return res