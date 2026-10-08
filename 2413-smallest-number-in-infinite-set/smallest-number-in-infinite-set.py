class SmallestInfiniteSet:

    def __init__(self):
        self.curr=1
        self.pos=set()
    def popSmallest(self) -> int:
        if self.pos:
            smallest=min(self.pos)
            self.pos.remove(smallest)
            return smallest
        else:
            self.curr+=1
            return self.curr-1
    def addBack(self, num: int) -> None:
        if self.curr>num:
            self.pos.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)