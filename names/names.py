import time
from bst import BinarySearchTree
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

b = BinarySearchTree(names_1[0])
## 2 for loops I would guess is technically O(2n) which boils back down to O(n)?
duplicates = []
for x in names_1:
    b.insert(x)

for y in names_2:
    if b.contains(y):
        duplicates.append(y)
    


#this one bad. o(n^2) with a bunchhhh of inputs as well. 
# For each value of names_1 it loops through the entire array of names_2 
# with 1000 names its 1000^2

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
