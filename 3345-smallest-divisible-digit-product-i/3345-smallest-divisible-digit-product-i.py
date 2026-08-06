class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        k=True
        i=n
        while k:
            p=1
            num=n
            while num>0:
                p=p*(num%10)
                num//=10
            if p%t==0:
                k=False
                return n
            else:
                n+=1