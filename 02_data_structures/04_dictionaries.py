# 04_dictionaries.py
# 字典 (Dictionary)
# 类似于 JavaScript 的 Object

# 1. 创建字典
# 使用大括号 {}
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"Person: {person}")

# 2. 访问值
# 键 (Key) 必须是不可变类型 (通常是字符串或数字)
print(f"Name: {person['name']}")
# 如果键不存在，会报错 KeyError
# 使用 get() 方法可以避免报错
print(f"Occupation: {person.get('occupation', 'Unknown')}")  # 如果不存在，返回默认值 'Unknown'

# 3. 修改字典
person['age'] = 31
person['email'] = "alice@example.com"
print(f"Updated person: {person}")

# 4. 删除键值对
del person['city']
# pop() - 删除并返回值
email = person.pop('email', 'N/A')
print(f"Popped email: {email}")

# 5. 遍历字典
# 遍历键 (Keys)
for key in person:
    print(key, person[key])

# 遍历值 (Values)
for value in person.values():
    print(value)

# 遍历键值对 (Items)
for key, value in person.items():
    print(f"{key}: {value}")

# 6. 字典推导式 (Dict Comprehension)
# {key: value for item in iterable if condition}
squares = {x: x**2 for x in range(5)}
print(f"Squares: {squares}")

# 7. 字典合并
# update() - 原地合并
other = {"job": "Engineer", "age": 32}  # 注意 age 会被覆盖
person.update(other)
print(f"Merged person: {person}")

# 8. copy()
# 浅拷贝
new_person = person.copy()

# 9. 字典视图 (View Objects)
# keys(), values(), items() 返回的是视图对象，会动态反映字典的变化
keys = person.keys()
print(f"Keys: {keys}")
person['new_key'] = "new_value"
print(f"Updated keys: {keys}")  # 视图会自动更新
