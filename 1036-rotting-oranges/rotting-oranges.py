class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        time=0
        if row==0:
            return -1
        fresh=0
        rotten=deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        while rotten and fresh>0:
            time+=1
            for e in range(len(rotten)):
                x,y=rotten.popleft()
                for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ax,by = x+a,y+b
                    if ax<0 or by<0 or ax==row or by==col:
                        continue
                    if grid[ax][by]==0 or grid[ax][by]==2:
                        continue
                    fresh-=1
                    grid[ax][by]=2
                    rotten.append((ax,by))
        return time if fresh==0 else -1