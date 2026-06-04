"""
Write a script that takes a string of text (e.g., "leetcode arrays hashing") and
builds a dictionary tracking the exact frequency of each character. Then, extract
all characters that appeared only once.


"""

s = "leetcode arrays hashing"
count_s = {}

# You can loop over the characters directly!
for char in s:
    count_s[char] = count_s.get(char, 0) + 1 

print(count_s)

unique_list = [key for key, value in count_s.items() if value == 1]
print(unique_list)


