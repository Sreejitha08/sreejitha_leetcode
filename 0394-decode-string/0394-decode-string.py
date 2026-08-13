class Solution:
    def decodeString(self, s: str) -> str:
        dl=[]
        al=[]
        res=""
        n=0
        for i in s:
            if i.isalpha():
                res+=i
            elif i.isdigit():
                n=(n*10)+int(i)
            elif i=='[':
                al.append(res)
                dl.append(n)
                res=""
                n=0
            else:
                res=(al.pop()+(res*dl.pop()))
        return res