class Solution:
    def countDaysTogether(self, aa: str, al: str, ab: str, bl: str) -> int:
        c={0:0,1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        for i in range(1,13):
            c[i]=c[i]+c[i-1]
        aa=c[int(aa[:2])-1]+int(aa[3:])
        al=c[int(al[:2])-1]+int(al[3:])
        ab=c[int(ab[:2])-1]+int(ab[3:])
        bl=c[int(bl[:2])-1]+int(bl[3:])
        s=max(aa,ab)
        e=min(al,bl)
        if s>e:
            return 0
        return (e-s+1)