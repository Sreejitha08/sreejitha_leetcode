class Solution:
    def executeInstructions(self, n: int, sp: List[int], s: str) -> List[int]:
        res=[0]*len(s)
        for i in range(len(s)):
            x,y=sp
            for j in range(i,len(s)):
                if s[j]=="R":
                    y+=1
                elif s[j]=="D":
                    x+=1
                elif s[j]=="U":
                    x-=1
                elif s[j]=="L":
                    y-=1
                if (x>=0 and x<=n-1 ) and (y>=0 and y<=n-1):
                    res[i]+=1
                else:
                    break
        return res