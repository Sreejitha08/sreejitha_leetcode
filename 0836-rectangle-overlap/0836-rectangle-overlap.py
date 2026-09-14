class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x11=rec1[0]
        y11=rec1[1]
        x14=rec1[2]
        y14=rec1[3]
        # x12=rec1[2]
        # y12=rec1[1]
        # x13=rec1[0]
        # y13=rec1[3]
        x21=rec2[0]
        y21=rec2[1]
        x24=rec2[2]
        y24=rec2[3]
        # x22=rec2[2]
        # y22=rec2[1]
        # x23=rec2[0]
        # y23=rec2[3]
        # 
        if x11<x24 and x21<x14 and y11<y24 and y21<y14:
            return True
        return False