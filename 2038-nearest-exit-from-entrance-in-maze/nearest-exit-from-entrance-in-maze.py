class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        cells=deque([[entrance[0],entrance[1],0]])
        maze[entrance[0]][entrance[1]]="+"
        m,n=len(maze),len(maze[0])
        while cells:
            i,j,k=cells.popleft()
            blocks=[[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
            for a,b in blocks:
                if a>=0 and b>=0 and a<m and b<n and maze[a][b]==".":
                    if a==0 or b==0 or a==m-1 or b==n-1:
                        return k+1
                    cells.append([a,b,k+1])
                    maze[a][b]="+"
        return -1