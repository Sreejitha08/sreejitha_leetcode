class Solution:
    def sumGame(self, num: str) -> bool:
        lq=0
        rq=0
        ls=0
        rs=0
        n=len(num)
        for i in range(n//2):
            if num[i]=="?":
                lq+=1
            else:
                ls+=int(num[i])
        for i in range(n//2,n):
            if num[i]=="?":
                rq+=1
            else:
                rs+=int(num[i])
        sd=(ls-rs)
        qd=(lq-rq)
        if qd==0:
            return sd!=0
        if qd%2==1:
            return True
        c=(qd*9)//2
        if c==-sd:
            return False
        return True