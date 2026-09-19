class Solution:
    def checkOverlap(self, r: int, xc: int, yc: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x=max(x1,min(xc,x2))
        y=max(y1,min(yc,y2))
        dx=x-xc
        dy=y-yc
        return ((dx*dx)+(dy*dy))<=(r*r)