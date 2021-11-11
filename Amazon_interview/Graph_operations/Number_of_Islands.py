'''Time: O(rows+cols), space: O(1)'''
class Solution(object):
    def dfs(self, grid, row, col):
        num_rows = len(grid)
        num_cols = len(grid[0])
        grid[row][col] = '0'
        if row-1>=0 and grid[row-1][col] == '1': self.dfs(grid, row-1, col)
        if row+1<num_rows and grid[row+1][col] == '1': self.dfs(grid, row+1, col)
        if col-1>=0 and grid[row][col-1] == '1': self.dfs(grid, row, col-1)
        if col+1<num_cols and grid[row][col+1] == '1': self.dfs(grid, row, col+1)


    def numIslands(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1': #root node that triggers dfs
                    num_islands = num_islands + 1
                    self.dfs(grid, row, col)
        return num_islands


''' 1's-land 0's-water'''
print(Solution().numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))