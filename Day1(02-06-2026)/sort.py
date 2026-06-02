data = [5, 2, 9, 1]

# Method 1: New copy
new_data = sorted(data)  # data is still [5, 2, 9, 1]; new_data is [1, 2, 5, 9]

# Method 2: In-place
data.sort()              # data is now [1, 2, 5, 9]


# A list of coordinate pairs: (x, y)
points = [(4, 2), (1, 10), (5, 1), (1, 5)]

# Scenario A: Sort strictly by the FIRST element (x)
points.sort(key=lambda item: item[0])
# Result: [(1, 10), (1, 5), (4, 2), (5, 1)] 
# Notice that (1, 10) stayed before (1, 5) because Timsort is stable.

# Scenario B: Sort strictly by the SECOND element (y)
points.sort(key=lambda item: item[1])
# Result: [(5, 1), (4, 2), (1, 5), (1, 10)]