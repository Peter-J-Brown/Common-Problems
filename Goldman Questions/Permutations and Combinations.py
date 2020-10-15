from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

# Get all permutations of [1, 2, 3]
perm = permutations([1, 1, 2, 3], 2)

# Print the obtained permutations
print("All possible permutation of", [1, 1, 2, 3])
for i in list(perm):
    print(i)



## if same element can't be used multiple times
comb = combinations([1, 1, 2, 3], 2)
print("All possible combinations of length 2 of", [1, 1, 2, 3], "no reuse of elements")
for i in list(comb):
    print(i)

## if same element can be used multiple times
print("All possible combinations of length 2 of", [1, 1, 2, 3], "with reuse of elements")
comb = combinations_with_replacement([1, 1, 2, 3], 2)
for i in list(comb):
    print(i)