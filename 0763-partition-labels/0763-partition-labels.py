class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l=set(list(s))
        m=[]
        for i in l:
            n=[]
            n.append(s.index(i))
            n.append(s.index(i))
            for j in range(n[-1],len(s)):
                if s[j]==i:
                    n[-1]=j
            m.append(n)
        m.sort()
        l=[m[0]]
        for i in range(1,len(m)):
            if m[i][0]<=l[-1][-1]:
                l[-1][-1]=max(m[i][-1],l[-1][-1])
            else:
                l.append(m[i])
        l2=[]
        for i in l:
            l2.append(i[1]-i[0]+1)
        return l2