# 02_tuples.py
# 元组 (Tuple)
# 类似于列表，但是不可变 (Immutable)
# 类似于 JS 的 const 数组 (但更严格，因为内容也不能改)

# 1. 创建元组
# 使用圆括号 ()
my_tuple = (1, 2, 3)
print(f"Tuple: {my_tuple}")

# 如果只有一个元素，需要在末尾加逗号
single_tuple = (1,)  # 注意逗号 (JS 没有这种要求)
print(f"Single tuple type: {type(single_tuple)}")

# 2. 访问元素
# 像列表一样使用索引
print(f"First element: {my_tuple[0]}")
# 切片也一样
print(f"Slice: {my_tuple[1:]}")

# 3. 不可变性 (Immutability)
# 尝试修改会报错
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error: {e}")  # 'tuple' object does not support item assignment

# 4. 元组解包 (Tuple Unpacking)
# 类似于 JS 的数组解构
a, b, c = my_tuple
print(f"a: {a}, b: {b}, c: {c}")

# 使用 * 获取剩余元素 (类似于 JS 的 ...rest)
a, *b, c = (1, 2, 3, 4, 5)
print(f"a: {a}, b: {b}, c: {c}")  # b 会变成列表 [2, 3, 4]

# 5. 为什么使用元组?
# - 性能更好 (稍微快一点)
# - 数据保护 (确保数据不会被意外修改)
# - 可以作为字典的键 (列表不行，因为列表是可变的)
my_dict = {(1, 2): "Coordinate (1, 2)"}
print(f"Dict access: {my_dict[(1, 2)]}")

# 6. count() 和 index()
# count() - 统计元素出现的次数
# index() - 返回元素第一次出现的索引
t = (1, 2, 3, 1, 1, 4)
print(f"Count of 1: {t.count(1)}")
print(f"Index of 2: {t.index(2)}")
