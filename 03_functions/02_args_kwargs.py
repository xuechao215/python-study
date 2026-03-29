# 02_args_kwargs.py
# 可变参数 (*args, **kwargs)
# 类似于 JS 的 ...rest

# 1. *args (Arbitrary Arguments)
# 接收任意数量的位置参数，作为元组 (tuple)
def sum_all(*args):
    """
    Args:
        *args: 任意数量的位置参数
    """
    print(f"Args type: {type(args)}")
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum (1, 2, 3): {sum_all(1, 2, 3)}")
print(f"Sum (10): {sum_all(10)}")

# 2. **kwargs (Keyword Arguments)
# 接收任意数量的关键字参数，作为字典 (dict)
def print_info(**kwargs):
    """
    Args:
        **kwargs: 任意数量的关键字参数
    """
    print(f"Kwargs type: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

# 3. 组合使用
# 顺序必须是:
# 1. 位置参数 (Positional Args)
# 2. *args
# 3. 关键字参数 (Keyword Args)
# 4. **kwargs
def combined_example(a, b, *args, name="User", **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"name: {name}")
    print(f"kwargs: {kwargs}")

combined_example(1, 2, 3, 4, name="Bob", extra="Data")

# 4. 解包 (Unpacking)
# 使用 * 将列表解包为位置参数
# 使用 ** 将字典解包为关键字参数
nums = [1, 2, 3]
info = {"name": "Charlie", "age": 25}

# 相当于 sum_all(1, 2, 3)
print(f"Unpacked list sum: {sum_all(*nums)}")

# 相当于 print_info(name="Charlie", age=25)
print_info(**info)
