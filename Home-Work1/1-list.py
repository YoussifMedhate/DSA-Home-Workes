"""
Python List Built-in Functions Task File
"""

# -----------------------------
# List creation for examples
# -----------------------------
nums = [5, 1, 8, 3, 2]
words = ['apple', 'banana', 'cherry']

# -----------------------------
# Built-in functions commonly used with lists
# -----------------------------

# len() -> returns length of list
print(len(nums))  # 5

# sum() -> returns sum of all numeric elements
print(sum(nums))  # 19

# min() -> smallest element
print(min(nums))  # 1

# max() -> largest element
print(max(nums))  # 8

# sorted() -> returns a new sorted list (doesn't modify original)
print(sorted(nums))       # [1,2,3,5,8]
print(sorted(nums, reverse=True))  # descending

# reversed() -> returns iterator (not list)
print(list(reversed(nums)))  # [2,3,8,1,5]

# all() -> True if all elements are True or non-zero
bools = [True, 1, 5]
print(all(bools))  # True
print(all([1, 0, 3]))  # False

# any() -> True if at least one element is True
print(any([0, 0, 3]))  # True
print(any([0, 0, 0]))  # False

# enumerate() -> returns index and value pairs
for idx, val in enumerate(words):
    print(idx, val)

# zip() -> combine multiple lists element-wise
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = list(zip(list1, list2))
print(combined)  # [(1,'a'),(2,'b'),(3,'c')]

# map() -> applies a function to all elements
nums_squared = list(map(lambda x: x ** 2, nums))
print(nums_squared)

# filter() -> filters elements based on condition
filtered = list(filter(lambda x: x > 3, nums))
print(filtered)  # [5,8]

# list() -> converts iterable to list
print(list('hello'))  # ['h','e','l','l','o']

# range() -> often used to generate lists of numbers
print(list(range(5)))  # [0,1,2,3,4]

# reversed + sorted combination
rev_sorted = list(reversed(sorted(nums)))
print(rev_sorted)

# max/min with key
print(max(words, key=len))  # 'banana'
print(min(words, key=lambda x: x[0]))  # 'apple'

# -----------------------------
# Extra examples for practice
# -----------------------------
# using map and filter together
numbers = [1, 2, 3, 4, 5]
processed = list(map(lambda x: x ** 2, filter(lambda n: n % 2 == 0, numbers)))
print(processed)  # [4,16]

# zip and enumerate combined
for i, (num, word) in enumerate(zip(nums, words)):
    print(i, num, word)

# all/any with conditions
print(all(x < 10 for x in nums))  # True
print(any(x > 5 for x in nums))   # True
