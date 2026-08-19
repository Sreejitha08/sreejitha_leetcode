class Solution:
    def maxNumberOfFamilies(self, n: int, r: List[List[int]]) -> int:
        # l=[]
        # for i in range(n):
        #     l.append([0]*10)
        # for i,j in r:
        #     l[i-1][j-1]=1
        # c=0
        # for i in l:
        #     if i[1:5]==[0]*4:
        #         i[1:5]=[1]*4
        #         c+=1
        #     if i[3:7]==[0]*4:
        #         i[3:7]=[1]*4
        #         c+=1
        #     if i[5:9]==[0]*4:
        #         i[5:9]=[1]*4
        #         c+=1
        # return c
        l={}
        c=0
        for i,j in r:
            if i not in l:
                l[i]=[0]*10
            l[i][j-1]=1
        c=(n-len(l))*2
        for i in l.values():
            if i[1:5]==[0]*4:
                i[1:5]=[1]*4
                c+=1
            if i[3:7]==[0]*4:
                i[3:7]=[1]*4
                c+=1
            if i[5:9]==[0]*4:
                i[5:9]=[1]*4
                c+=1
        return c