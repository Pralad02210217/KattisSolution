from collections import deque

def findPosition(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'P':
                return (i, j)
    return None

def is_Trap(row, col, grid):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 'T':
            return True
    return False

def countGold(grid, start):
    queue = deque([start])
    gold = 0
    visited=[]
    for i in range(len(grid)):
        visited.append([])
        for j in range(len(grid[0])):
            visited[i].append(False)
    visited[start[0]][start[1]] = True
    
   
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while queue:
        row, col = queue.popleft()
        
        if grid[row][col] == 'G':
            gold += 1
            
        if is_Trap(row, col, grid):
            continue
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and not visited[new_row][new_col]:
                if grid[new_row][new_col] != '#':
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))
    
    print(gold)

def main():
    col, row = map(int, input().split())
    
    grid= []
    for _ in range(row):
        line= input().strip()#
        grid.append(list(line))
    
    start = findPosition(grid)
    countGold(grid, start)
if __name__=='__main__':
    main()
    





