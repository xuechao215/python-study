# 03_sets.py
# 集合 (Set)
# 类似于 JS 的 Set

# 1. 创建集合
# 使用大括号 {}
my_set = {1, 2, 3}
print(f"Set: {my_set}")

# 如果使用 {} 创建空字典，而不是空集合
# 使用 set() 创建空集合
empty_set = set()
print(f"Empty set type: {type(empty_set)}")

# 2. 唯一性 (Uniqueness)
# 自动去重
my_set.add(1)
my_set.add(4)
print(f"Updated set: {my_set}")  # 1 不会重复出现

# 3. 成员操作 (Membership)
# in, not in (效率非常高，O(1))
print(f"1 in set: {1 in my_set}")

# 4. 删除元素
# remove() - 必须存在，否则报错
# discard() - 如果不存在，不报错
my_set.discard(5)
# pop() - 随机删除并返回一个元素 (无序)
# clear() - 清空

# 5. 集合运算 (Set Operations)
# - 并集 (Union): |
# - 交集 (Intersection): &
# - 差集 (Difference): -
# - 对称差集 (Symmetric Difference): ^

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"Union (a | b): {a | b}")       # {1, 2, 3, 4, 5, 6}
print(f"Intersection (a & b): {a & b}") # {3, 4}
print(f"Difference (a - b): {a - b}")   # {1, 2}
print(f"Symmetric Difference (a ^ b): {a ^ b}") # {1, 2, 5, 6}

# 6. 不可变集合 (frozenset)
# 不可变的集合，可以作为字典的键
fs = frozenset([1, 2, 3])
# fs.add(4)  # 会报错
