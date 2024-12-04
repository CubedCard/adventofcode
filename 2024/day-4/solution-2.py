def count_mas_crosses(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (grid[i][j] == 'A' and grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S' and grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M'):
                count += 1
            elif (grid[i][j] == 'A' and grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M' and grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S'):
                count += 1
            elif (grid[i][j] == 'A' and grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M' and grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M'):
                count += 1
            elif (grid[i][j] == 'A' and grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S' and grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S'):
                count += 1

    return count

grid = [line.strip() for line in open('data.txt')]

print(f"Part 2: {count_mas_crosses(grid)}")