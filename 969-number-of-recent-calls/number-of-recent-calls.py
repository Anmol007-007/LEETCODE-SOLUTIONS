class RecentCounter:

    def __init__(self):
        self.record=[]
        self.st=0

    def ping(self, t: int) -> int:
        self.record.append(t)
        while self.record[self.st]<t-3000:
            self.st+=1
        return len(self.record)-self.st

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)