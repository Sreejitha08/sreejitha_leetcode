class Solution:
    def titleToNumber(self, ct: str) -> int:
        j=1
        d={}
        for i in range(65,91):
            d[chr(i)]=j
            j+=1
        res=0
        for i in ct:
            res=(res*26)+d[i]
        return res