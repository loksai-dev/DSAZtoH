# 🎛️ Matrix Master Reference (2D Arrays)

## What is a Matrix?

In Python, a matrix is simply a **list of lists**.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Visual Representation:

```text
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
```

* Rows = Horizontal
* Columns = Vertical

---

# 📐 Matrix Dimensions

## Number of Rows

```python
rows = len(matrix)
```

```python
len(matrix)  # 3
```

Python counts elements in the outer list.

---

## Number of Columns

```python
cols = len(matrix[0])
```

```python
len(matrix[0])  # 3
```

Python counts elements inside the first row.

---

# 🎯 Matrix Indexing

## Access Entire Row

```python
matrix[0]
```

Output:

```python
[1, 2, 3]
```

Explanation:

```text
matrix[0]
      ↑
    Row 0
```

---

## Access Single Cell

```python
matrix[1][2]
```

Output:

```python
6
```

Explanation:

```text
matrix[1][2]

Row 1 → [4, 5, 6]
              ↑
          Column 2
```

---

# 🧭 Matrix Traversal

## Traverse Every Cell

```python
rows = len(matrix)
cols = len(matrix[0])

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c])
```

Output:

```text
1 2 3
4 5 6
7 8 9
```

---

## Traverse Row Wise

```python
for row in matrix:
    print(row)
```

Output:

```python
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```

---

## Traverse Column Wise

```python
rows = len(matrix)
cols = len(matrix[0])

for c in range(cols):
    for r in range(rows):
        print(matrix[r][c])
```

Output:

```text
1 4 7
2 5 8
3 6 9
```

---

# 🛠️ Matrix Initialization

## Correct Way

```python
grid = [[0] * 4 for _ in range(4)]
```

Result:

```python
[
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]
]
```

---

## Why Use `_`?

```python
for _ in range(4):
    pass
```

`_` means:

> "I need a variable for the loop, but I don't care about its value."

---

## Wrong Way

```python
grid = [[0] * 4] * 4
```

Problem:

```python
grid[0][0] = 1
```

Output:

```python
[
 [1,0,0,0],
 [1,0,0,0],
 [1,0,0,0],
 [1,0,0,0]
]
```

All rows point to the same object.

---

# 🔄 Swapping Rows

Swap entire rows instantly:

```python
matrix[0], matrix[2] = matrix[2], matrix[0]
```

Before:

```python
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
```

After:

```python
[
 [7,8,9],
 [4,5,6],
 [1,2,3]
]
```

---

# ✏️ Modify Matrix Values

## Change One Cell

```python
matrix[0][0] = 99
```

Result:

```python
[
 [99,2,3],
 [4,5,6],
 [7,8,9]
]
```

---

## Change Entire Row

```python
matrix[1] = [10, 11, 12]
```

Result:

```python
[
 [1,2,3],
 [10,11,12],
 [7,8,9]
]
```

---

# 🔁 Common Matrix Patterns

## Directions Array

Used in BFS, DFS, Grid Problems.

### 4 Directions

```python
directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]
```

Traversal:

```python
for dr, dc in directions:
    nr = row + dr
    nc = col + dc
```

---

### 8 Directions

```python
directions = [
    (-1,0),
    (1,0),
    (0,-1),
    (0,1),
    (-1,-1),
    (-1,1),
    (1,-1),
    (1,1)
]
```

---

# 🎯 Boundary Check Template

Always check bounds before accessing a cell.

```python
rows = len(grid)
cols = len(grid[0])

if 0 <= r < rows and 0 <= c < cols:
    print(grid[r][c])
```

---

# 🚀 Matrix Interview Template

```python
rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        value = grid[r][c]

        # Process value
```


# 🔍 Quick Reference Table

| Expression       | Meaning           | Result          |
| ---------------- | ----------------- | --------------- |
| matrix           | Entire matrix     | `[[1,2],[3,4]]` |
| len(matrix)      | Number of rows    | `2`             |
| len(matrix[0])   | Number of columns | `2`             |
| matrix[0]        | First row         | `[1,2]`         |
| matrix[1]        | Second row        | `[3,4]`         |
| matrix[0][1]     | Row 0, Col 1      | `2`             |
| matrix[r][c]     | Cell at (r,c)     | Value           |
| matrix[r]        | Entire row        | List            |
| matrix[r][c] = x | Update cell       | Modified matrix |

---

# 🧠 Matrix Mental Model

```text
matrix[row][col]

      Columns
        0 1 2

Row 0   1 2 3
Row 1   4 5 6
Row 2   7 8 9
```

Remember:

* First index = Row
* Second index = Column
* `len(matrix)` = Rows
* `len(matrix[0])` = Columns
* `matrix[r]` = Entire row
* `matrix[r][c]` = Single cell
