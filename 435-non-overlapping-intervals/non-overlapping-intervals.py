class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove =0
        intervals.sort(key = lambda x:x[1])
        prev_short = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<prev_short:
                remove+=1
            else:
                prev_short =intervals[i][1]
        return remove