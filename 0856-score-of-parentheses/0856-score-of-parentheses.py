class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        l=[0]
        for i in s:
            if i=='(':
                l.append(0)
            else:
                c=l.pop()
                if c==0:
                    c=1
                else:
                    c*=2
                l[-1]+=c
        return l[0]