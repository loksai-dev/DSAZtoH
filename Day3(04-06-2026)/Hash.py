#1 . Initialization & Insertion  

hero = {}
hero["name"] = "peter parker"
hero["hero_name"] = "Spider-Man"

print(hero)


# 2 . Updating a value 
hero["hero_name"] = "Spidey"

# 3. Checking existence (Fast! O(1))

if "hero_name" in hero: 
    print(f"Identity : {hero['hero_name']}")


#4. Safe retrieval using .get()
#if "gadget" doesn't exist, return "web shooters" insed of crashing 

gadget  = hero.get("gadget", "webshooters")
print(f"Equipped : {gadget}")



from collections import defaultdict, Counter 

nums = [4, 1, 2, 1, 2, 2]

# Approach : Using default dict 
# 'int' tells Python to automatically set missing keys to 0

dynamic_counts = defaultdict(int)
for num in nums: 
    dynamic_counts[num] += 1 

# Approach : using counter 

fast_counts = Counter(nums)

print(fast_counts)
print(fast_counts[2])
print(fast_counts.most_common(1))


# SETS 

#1 . Deduplication 

raw_ids = [101, 102, 101, 103, 102]
unique_ids = set(raw_ids)
print(unique_ids)


#2. Operations 
unique_ids.add(104)


#3. Fast Membership checking O(1)

if 105 not in unique_ids: 
    print("ID 105 is available")


#4 . Set Mathematics (Incerdibly useful for grid/graph problems)

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a & set_b) #Intersection 
print(set_a | set_b) #Union 
print(set_a - set_b) # Difference 



