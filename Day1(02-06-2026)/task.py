leaderboard = [["Alice", 350], ["Bob", 1200], ["Charlie", 350], ["David", 950]]

# sorted() returns a BRAND NEW list object
ordered_list = sorted(leaderboard, key=lambda item: item[1], reverse=True)

print(ordered_list)
# Output: [['Bob', 1200], ['David', 950], ['Alice', 350], ['Charlie', 350]]

leaderboard = [["Alice", 350], ["Bob", 1200], ["Charlie", 350], ["David", 950]]

# Sorts 'leaderboard' directly
leaderboard.sort(key=lambda item: item[1], reverse=True)

print(leaderboard) 
# Output: [['Bob', 1200], ['David', 950], ['Alice', 350], ['Charlie', 350]]
