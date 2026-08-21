class MyHashMap:
    l=[]
    def __init__(self):
        self.l=[]

    def put(self, key: int, value: int) -> None:
        b=True
        for i in self.l:
            if key==i[0]:
                i[1]=value
                b=False
                break
        if b:
            self.l.append([key,value])

    def get(self, key: int) -> int:
        for i in self.l:
            if key==i[0]:
                return i[1]
        return -1
    def remove(self, key: int) -> None:
        for i in range(len(self.l)):
            if self.l[i][0]==key:
                self.l.pop(i)
                break

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)