class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        s2="}])"
        for i in range(len(s)):
            if len(l)==0 and s[i] in s2:
                return False
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                l.append(s[i])
            elif (l[-1]=='(' and s[i]==')') or (l[-1]=='{' and s[i]=='}') or (l[-1]=='[' and s[i]==']'):
                l.pop()
            else:
                return False
        if len(l)==0:
            return True
        return False