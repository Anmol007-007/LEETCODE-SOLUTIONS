class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n=len(grid)
        count=0
        for a in range(n):
            row=grid[a]
            for b in range(n):
                col=[grid[i][b] for i in range(n)]
                if row==col:
                    count+=1
        return count