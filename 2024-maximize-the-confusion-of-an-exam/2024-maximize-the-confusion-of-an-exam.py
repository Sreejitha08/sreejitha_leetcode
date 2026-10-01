class Solution:
    def maxConsecutiveAnswers(self, ak: str, k: int) -> int:
        c=0
        i=0
        maxi=float('-inf')
        for j in range(len(ak)):
            if ak[j]!="T":
                c+=1
            while c>k:
                if ak[i]=="F":
                    c-=1
                i+=1
            maxi=max(maxi,j-i+1)
        i=0
        c=0
        for j in range(len(ak)):
            if ak[j]!="F":
                c+=1
            while c>k:
                if ak[i]=="T":
                    c-=1
                i+=1
            maxi=max(maxi,j-i+1)
        return maxi