#Create a list 

nums = []

#append 
nums.append(10)    #O(1)
nums.append(20)    #O(1)
nums.append(30)    #O(1)

#Remove 

nums.pop()         #O(1) --> it pops 30 
nums.pop(1)        #O(N) 
nums.insert(0,5)   #O(N)

print(nums)