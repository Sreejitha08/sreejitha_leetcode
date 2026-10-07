class Solution:
    def countCollisions(self, d: str) -> int:
        s=[]
        c=0
        i=0
        n=len(d)
        for i in range(n):
            if len(s)==0:
                s.append(d[i])
            elif d[i]=="L" and s[-1]=="R":
                c+=2
                s.pop()
                while s and s[-1]=="R":
                    c+=1
                    s.pop()
                s.append("S")
            elif d[i]=="L" and s[-1]=="S":
                c+=1
            elif s[-1]=="R" and d[i]=="S":
                while s and s[-1]=="R":
                    c+=1
                    s.pop()
                s.append("S")
            else:
                s.append(d[i])
        return c