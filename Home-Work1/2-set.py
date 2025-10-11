"""
Python Set Built-in Functions Task File
Includes all built-in functions usable with sets, their basic usage, and examples.
Compact and ready for submission.
"""

# -----------------------------
# Set creation for examples
# -----------------------------
nums = {1, 2, 3, 4, 5}
letters = {'a', 'b', 'c'}

# -----------------------------
# Built-in functions commonly used with sets
# -----------------------------

# len() -> returns number of elements
print(len(nums))  # 5

# sum() -> sum of all numeric elements
print(sum(nums))  # 15

# min() and max()
print(min(nums))  # 1
print(max(nums))  # 5

# sorted() -> returns sorted list (not set)
print(sorted(nums))  # [1,2,3,4,5]

# all() and any()
print(all(nums))  # True (no zero values)
print(any({0, 0, 3}))  # True

# enumerate() -> index-value pairs (after converting to list)
for idx, val in enumerate(nums):
    print(idx, val)

# zip() -> combine with another iterable
ids = {10, 20, 30}
combined = list(zip(nums, ids))
print(combined)

# map() -> apply function to all elements
squared = set(map(lambda x: x ** 2, nums))
print(squared)

# filter() -> keep elements that match condition
filtered = set(filter(lambda x: x > 2, nums))
print(filtered)

# set() -> create a set from iterable
chars = set('hello')  # {'h','e','l','o'}

# range() with set
r = set(range(5))  # {0,1,2,3,4}

# -----------------------------
# Set methods (core functionality)
# -----------------------------

# add() -> add single element
nums.add(6)

# update() -> add multiple elements
nums.update([7, 8])

# remove() -> remove element (KeyError if missing)
nums.remove(3)

# discard() -> remove if exists, ignore otherwise
nums.discard(100)

# pop() -> remove and return random element
removed = nums.pop()

# clear() -> remove all elements
copy_nums = nums.copy()
copy_nums.clear()

# copy() -> shallow copy
copied = nums.copy()

# difference() -> elements in A but not in B
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.difference(b))  # {1,2}

# intersection() -> common elements
print(a.intersection(b))  # {3,4}

# union() -> all unique elements
print(a.union(b))  # {1,2,3,4,5,6}

# symmetric_difference() -> elements not common in both
print(a.symmetric_difference(b))  # {1,2,5,6}

# issubset() and issuperset()
print({1, 2}.issubset(a))  # True
print(a.issuperset({1, 2}))  # True

# isdisjoint() -> True if sets have no elements in common
print(a.isdisjoint({7, 8}))  # True

# -----------------------------
# Built-in usage combinations
# -----------------------------

# combine map and filter
combo = set(map(lambda x: x * 2, filter(lambda n: n % 2 == 0, range(10))))
print(combo)

# using zip with sets
set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}
paired = set(zip(set1, set2))
print(paired)

# all/any on condition
print(all(x < 10 for x in nums))
print(any(x == 2 for x in nums))

# -----------------------------
# Practice functions
# -----------------------------

def set_difference(a: set, b: set) -> set:
    return a - b

print(set_difference({1, 2, 3}, {2, 3}))  # {1}


def set_common(a: set, b: set) -> set:
    return a & b

print(set_common({1, 2, 3}, {2, 4}))  # {2}


def unique_letters(word: str) -> set:
    return set(word)

print(unique_letters('banana'))  # {'b','a','n'}
