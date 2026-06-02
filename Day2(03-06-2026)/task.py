"""
## 🎯 The Mission

You need to create a single Python script that executes three distinct structural operations on a grid, processing them sequentially.

### Step 1: Initialization

Initialize a $4 \times 4$ 2D array (matrix) where every single cell starts as `0`.

* **Constraint:** You must use a list comprehension so that each row is completely independent in memory.
* *Expected State:*
```python
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]

```

### Step 2: Modify the Diagonal

Change the elements along the **primary diagonal** (from the top-left corner to the bottom-right corner) from `0` to `1`.

* **Constraint:** Do not hardcode the coordinates manually (e.g., don't write `grid[0][0] = 1`, `grid[1][1] = 1`, etc.). Use a loop that dynamically scales.
* *Expected State:*
```python
[[1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1]]

```

### Step 3: Reverse the Rows In-Place

Flip the matrix vertically so that the first row becomes the last row, the second row becomes the third row, and so on.

* **Strict Constraints:** * ❌ Do **not** use built-in methods like `matrix.reverse()`.
* ❌ Do **not** use the built-in function `reversed(matrix)`.
* ❌ Do **not** use the slicing trick `matrix[::-1]`.


* **Hint:** Use the **Two-Pointer technique** with a `while` loop. Set a pointer at the first row (`top = 0`) and a pointer at the last row (`bottom = len(matrix) - 1`), then swap the entire row arrays in-place while moving the pointers toward each other.
* *Final Expected State:*
```python
[[0, 0, 0, 1],
 [0, 0, 1, 0],
 [0, 1, 0, 0],
 [1, 0, 0, 0]]

"""

#step1 - initialization 

matrix = []
rows, cols = 4 , 4 
matrix = [[0] * cols for _ in range(rows)]

#step 2 - Modify the diagonal 

for i in range(len(matrix)):
    matrix[i][i] = 1 

print(matrix)

# 3. Reverse the rows using the Two-Pointer swap technique

l = 0 
r = len(matrix) - 1 

while l < r : 
    matrix[l],matrix[r] = matrix[r], matrix[l]

    l += 1
    r -= 1

for row in matrix: 
    print(row ) 



