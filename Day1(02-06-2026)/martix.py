# DO NOT DO THIS
grid = [[0] * 3] * 3

grid[0][0] = 99
print(grid) # Output: [[99, 0, 0], [99, 0, 0], [99, 0, 0]]

#It creates shallow copy 


rows  , cols = 3 , 3 
grid = [[0] * cols for _ in range(rows)]

grid[0][0] = 99 
print(grid)