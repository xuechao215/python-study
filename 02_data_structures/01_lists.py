# 01_lists.py
# 列表 (List)
# 类似于 JavaScript 的 Array

# 1. 创建列表
# 使用方括号 []
fruits = ["apple", "banana", "cherry"]
print(f"Initial list: {fruits}")

# 2. 访问元素
# 索引从 0 开始
print(f"First element: {fruits[0]}")
# 负索引 (Negative Indexing) - 从末尾倒数
print(f"Last element: {fruits[-1]}")  # -1 表示最后一个元素
print(f"Second to last: {fruits[-2]}")

# 3. 切片 (Slicing) - 获取子列表
# list[start:end:step]
# start: 默认 0
# end: 不包含
# step: 默认 1
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Slice [2:5]: {numbers[2:5]}")  # [2, 3, 4]
print(f"Slice [:5]: {numbers[:5]}")    # [0, 1, 2, 3, 4]
print(f"Slice [5:]: {numbers[5:]}")    # [5, 6, 7, 8, 9]
print(f"Slice [::2]: {numbers[::2]}")  # [0, 2, 4, 6, 8] (偶数索引)
print(f"Slice [::-1]: {numbers[::-1]}") # [9, 8, ..., 0] (反转列表)

# 4. 修改列表
# 列表是可变的 (Mutable)
fruits[1] = "blueberry"
print(f"Modified list: {fruits}")

# 5. 添加元素
# append() - 在末尾添加 (类似于 JS 的 push)
fruits.append("orange")
# insert() - 在指定位置插入
fruits.insert(1, "grape")
# extend() - 合并列表 (类似于 JS 的 concat 或 spread operator [...a, ...b])
fruits.extend(["kiwi", "melon"])
print(f"Extended list: {fruits}")

# 6. 删除元素
# remove() - 删除指定值 (如果不存在会报错)
fruits.remove("banana") if "banana" in fruits else print("banana not found")
# pop() - 删除指定索引并返回 (类似于 JS 的 pop，但 JS pop 只能删除最后一个)
last_fruit = fruits.pop()  # 默认删除最后一个
first_fruit = fruits.pop(0) # 删除第一个
# del - 删除变量或索引
del fruits[0]
# clear() - 清空列表
# fruits.clear()

# 7. 排序
# sort() - 原地排序 (改变原列表)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(f"Sorted numbers: {numbers}")
# reverse() - 原地反转
numbers.reverse()
print(f"Reversed numbers: {numbers}")

# sorted() - 返回新列表 (不改变原列表)
original = [3, 1, 2]
new_sorted = sorted(original)
print(f"Original: {original}, New Sorted: {new_sorted}")

# 8. 列表推导式 (List Comprehension) - 非常强大的特性
# [expression for item in iterable if condition]
# 类似于 JS 的 map 和 filter 的结合
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

# 9. 复制列表
# 注意: list2 = list1 只是复制引用 (浅拷贝)
# 使用 copy() 或切片 [:] 来创建新列表 (浅拷贝)
original = [1, 2, 3]
copy1 = original.copy()
copy2 = original[:]
import copy
deep_copy = copy.deepcopy(original) # 深拷贝 (如果包含嵌套列表)
