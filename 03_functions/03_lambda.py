# 03_lambda.py
# 匿名函数 (Lambda)
# 类似于 JS 的 Arrow Function (=>)

# 1. 语法
# lambda arguments: expression
# 只能有一行表达式，不需要 return，自动返回
add = lambda x, y: x + y
print(f"Lambda Add: {add(3, 4)}")

# 2. 作为高阶函数的参数
# map(), filter(), reduce(), sort()
numbers = [1, 2, 3, 4, 5]

# map() - 映射
squared = list(map(lambda x: x**2, numbers))
print(f"Squared (Map): {squared}")

# filter() - 过滤
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens (Filter): {evens}")

# sort() - 自定义排序规则
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# 按年龄排序 (JS: people.sort((a, b) => a.age - b.age))
people.sort(key=lambda p: p["age"])
print(f"Sorted by age: {people}")

# 按名字排序 (默认按 ASCII)
people.sort(key=lambda p: p["name"])
print(f"Sorted by name: {people}")

# 3. Reduce (需要导入 functools)
from functools import reduce

# 累加 (JS: numbers.reduce((acc, curr) => acc + curr, 0))
sum_total = reduce(lambda acc, curr: acc + curr, numbers, 0)
print(f"Sum Total (Reduce): {sum_total}")

# 4. IIFE (Immediately Invoked Function Expression)
# Python 中不常用，但可以做到
(lambda x: print(f"Hello {x}"))("World")

# 5. 局限性
# Lambda 只能包含一个表达式，不能包含复杂的语句 (如 if-elif-else 块，只能是三元运算符)
# 只能返回一个值
# 如果逻辑复杂，建议定义普通函数
