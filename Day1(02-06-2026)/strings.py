#Shallow copy 

import copy 

# A nested list 
original = [[1,2,3],[4,5,6]]

#Create a shallow copy 
shallow_copied = copy.copy(original)

# print(original)  #Output :  [[1, 2, 3], [4, 5, 6]]
# print(shallow_copied) # [[1, 2, 3], [4, 5, 6]]

#scenario 1 -> Modifying the outer container(independent)

shallow_copied.append([7,8,9])

print(original) #[[1, 2, 3], [4, 5, 6]]
print(shallow_copied) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


#Scenario 2 -> Modifying an inner element (shared)

shallow_copied[0][0] = "BOOM"

print(original) #[['BOOM', 2, 3], [4, 5, 6]]
print(shallow_copied) #[['BOOM', 2, 3], [4, 5, 6], [7, 8, 9]]


#string  --> shallow copy 

original_list = [10, 20, [30, 40]]

# This creates a shallow copy using slicing
copied_list = original_list[:] 

# Proof it's a shallow copy:
copied_list[2][0] = "CHANGED"
print(original_list)  # Output: [10, 20, ['CHANGED', 40]] -> It affected the original!



arr = [10, 20, 30, 40, 50, 60]

# Extract elements from index 1 up to (but excluding) 4
print(arr[1:4])

# Grab everything from index 3 to the end
print(arr[3:])

# Grab every second element across the entire list
print(arr[::2])


# Trick: Reverse a list completely using a negative step
print(arr[::-1])



