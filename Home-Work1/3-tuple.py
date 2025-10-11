"""
Python Tuple Built-in Functions Task File
"""

# -----------------------------
# Tuple creation for examples
# -----------------------------
nums = (1, 2, 3, 4, 5)
words = ('apple', 'banana', 'cherry')
mixed = (1, 'a', 3.14, (2, 3))

# Single element tuple (needs comma)
one_item = (5,)

# From iterable
chars = tuple('hello')
range_tuple = tuple(range(5))

# -----------------------------
# Built-in functions commonly used with tuples
# -----------------------------

# len() -> number of elements
print(len(nums))  # 5

# sum(), min(), max()
print(sum(nums))  # 15
print(min(nums))  # 1
print(max(nums))  # 5

# sorted() -> returns a sorted list (not tuple)
print(sorted(nums))  # [1,2,3,4,5]

# all() -> True if all elements are True
print(all(nums))  # True

# any() -> True if any element is True
print(any((0, 0, 3)))  # True

# enumerate() -> index-value pairs
for idx, val in enumerate(words):
    print(idx, val)

# zip() -> combine multiple tuples element-wise
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
combined = tuple(zip(t1, t2))
print(combined)  # ((1,'a'),(2,'b'),(3,'c'))

# map() -> apply function to all elements
squared = tuple(map(lambda x: x ** 2, nums))
print(squared)

# filter() -> filter elements
filtered = tuple(filter(lambda x: x > 2, nums))
print(filtered)

# tuple() -> create tuple from iterable
print(tuple(['a', 'b', 'c']))  # ('a','b','c')

# range() + tuple
print(tuple(range(5)))  # (0,1,2,3,4)

# reversed() -> iterator reversed
print(tuple(reversed(nums)))  # (5,4,3,2,1)

# max/min with key
print(max(words, key=len))  # 'banana'
print(min(words, key=lambda x: x[0]))  # 'apple'

# -----------------------------
# Tuple operations
# -----------------------------

# Indexing & slicing
first = nums[0]
last = nums[-1]
part = nums[1:4]

# Concatenation & repetition
combined_tuple = nums + (6, 7)
repeated = ('a', 'b') * 3

# Membership
print(3 in nums)   # True
print('x' not in words)  # True

# Unpacking
a, b, c = (1, 2, 3)

# Nested tuple access
nested = (1, (2, 3), 4)
print(nested[1][1])  # 3

# Count and Index methods
letters = ('a', 'b', 'a', 'c', 'a')
print(letters.count('a'))  # 3
print(letters.index('c'))  # 3

# -----------------------------
# Combined usage examples
# -----------------------------

# map + filter example
numbers = (1, 2, 3, 4, 5)
processed = tuple(map(lambda x: x ** 2, filter(lambda n: n % 2 == 0, numbers)))
print(processed)  # (4,16)

# zip + enumerate example
for i, (num, word) in enumerate(zip(nums, words)):
    print(i, num, word)

# all/any with condition
print(all(x < 10 for x in nums))  # True
print(any(x == 3 for x in nums))  # True

# -----------------------------
# Practice functions
# -----------------------------

def tuple_reverse(t: tuple) -> tuple:
    return t[::-1]

print(tuple_reverse((1, 2, 3)))


def tuple_unique(t: tuple) -> tuple:
    return tuple(dict.fromkeys(t))  # preserves order

print(tuple_unique((1, 2, 1, 3, 2, 4)))


def flatten_tuple(t: tuple) -> tuple:
    out = []
    for i in t:
        if isinstance(i, (list, tuple)):
            out.extend(i)
        else:
            out.append(i)
    return tuple(out)

print(flatten_tuple(((1, 2), (3, 4), 5)))
