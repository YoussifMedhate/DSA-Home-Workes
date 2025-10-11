"""
Python Dictionary Built-in Functions Task File
"""

# -----------------------------
# Dictionary creation for examples
# -----------------------------
student = {'name': 'Ali', 'age': 20, 'grade': 'A'}
nums = {'one': 1, 'two': 2, 'three': 3}

# from pairs or constructor
pairs = dict([(1, 'a'), (2, 'b')])
letters = dict(a=1, b=2, c=3)

# -----------------------------
# Built-in functions commonly used with dict
# -----------------------------

# len() -> number of key-value pairs
print(len(student))

# sorted() -> sorted list of keys
print(sorted(student))

# all() -> True if all keys are True
print(all(student))

# any() -> True if any key is True
print(any(student))

# sum(), min(), max() on values
print(sum(nums.values()))  # 6
print(min(nums.values()))  # 1
print(max(nums.values()))  # 3

# enumerate() -> index and key
for i, k in enumerate(student):
    print(i, k)

# zip() -> combine two iterables into key-value pairs
keys = ['a', 'b', 'c']
values = [10, 20, 30]
combined = dict(zip(keys, values))
print(combined)

# map() -> apply to values
mapped = dict(zip(nums.keys(), map(lambda x: x * 2, nums.values())))
print(mapped)

# filter() -> filter key-value pairs
filtered = dict(filter(lambda item: item[1] > 1, nums.items()))
print(filtered)

# dict() -> build dictionary from iterable
print(dict([(1, 'x'), (2, 'y')]))

# -----------------------------
# Dictionary methods
# -----------------------------

# get() -> return value or default if not found
print(student.get('age'))
print(student.get('major', 'N/A'))

# keys(), values(), items()
print(student.keys())
print(student.values())
print(student.items())

# update() -> merge another dict
student.update({'age': 21, 'city': 'Cairo'})
print(student)

# pop() -> remove and return value of a key
removed = student.pop('grade')
print(removed)

# popitem() -> remove last key-value pair
last = student.popitem()
print(last)

# setdefault() -> get value if exists, else set and return default
x = student.setdefault('university', 'CU')
print(x)

# copy() -> shallow copy
copy_dict = student.copy()

# clear() -> remove all key-value pairs
temp = {'x': 1, 'y': 2}
temp.clear()
print(temp)

# fromkeys() -> create dict from keys with same value
new_d = dict.fromkeys(['a', 'b', 'c'], 0)
print(new_d)

# -----------------------------
# Advanced operations
# -----------------------------

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)

# Conditional comprehension
filtered_dict = {k: v for k, v in nums.items() if v > 1}
print(filtered_dict)

# Merge two dictionaries
merged = {**nums, **letters}
print(merged)

# Reverse keys and values
reversed_dict = {v: k for k, v in nums.items()}
print(reversed_dict)

# Check membership (keys only)
print('name' in student)
print('Ali' in student.values())

# -----------------------------
# Combined usage examples
# -----------------------------

# enumerate + items
for i, (k, v) in enumerate(nums.items()):
    print(i, k, v)

# all/any with conditions
print(all(v > 0 for v in nums.values()))
print(any(v == 2 for v in nums.values()))

# zip + map combined
d = dict(zip(keys, map(str.upper, ['apple', 'banana', 'cherry'])))
print(d)

# -----------------------------
# Practice functions
# -----------------------------

def invert_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}

print(invert_dict({'a': 1, 'b': 2}))


def merge_and_sum(d1: dict, d2: dict) -> dict:
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result

print(merge_and_sum({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))


def filter_dict(d: dict, condition) -> dict:
    return {k: v for k, v in d.items() if condition(v)}

print(filter_dict({'a': 10, 'b': 5, 'c': 20}, lambda x: x > 10))
