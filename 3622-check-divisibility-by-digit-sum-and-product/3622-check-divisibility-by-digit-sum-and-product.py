class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num=n
        s=0
        p=1
        while num>0:
            r=num%10
            s+=r
            p*=r
            num//=10
        if n%(s+p)==0:
            return True
        return False