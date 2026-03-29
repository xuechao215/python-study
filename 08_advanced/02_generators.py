# 02_generators.py
# 生成器 (Generators)
# 类似于 JS 的 function* 和 yield

# 1. 简单的生成器函数
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(f"First value: {next(gen)}")
print(f"Second value: {next(gen)}")
print(f"Third value: {next(gen)}")
# print(f"Fourth value: {next(gen)}") # StopIteration Error

# 2. 为什么使用生成器?
# 节省内存: 每次只产生一个值，而不是一次性生成所有值
# 处理大量数据流 (如读取大文件)
# 无限序列 (如斐波那契数列)

# 3. 斐波那契数列生成器
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("\nFibonacci under 100:")
for num in fibonacci(100):
    print(num, end=" ")
print()

# 4. 生成器表达式 (Generator Expressions)
# 类似于列表推导式，但是使用圆括号 ()
# 更加内存友好
squares = (x**2 for x in range(1000000))  # 此时还没有计算任何值

# 只有在迭代时才会计算
print(f"\nGenerator object: {squares}")
print(f"First square: {next(squares)}")
print(f"Second square: {next(squares)}")

# 5. yield from (Python 3.3+)
# 委托给子生成器
def sub_gen():
    yield 'A'
    yield 'B'

def main_gen():
    yield 1
    yield from sub_gen()
    yield 2

for item in main_gen():
    print(item, end=" ")
print()
