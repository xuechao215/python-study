# 01_decorators.py
# 装饰器 (Decorators)
# 类似于 JS 的 HOC (Higher-Order Component) 或 decorators

# 1. 简单装饰器
# 接收一个函数作为参数，并返回一个新的函数
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# 等价于 say_hello = my_decorator(say_hello)
say_hello()

# 2. 带参数的装饰器
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_args
def add(a, b):
    return a + b

print(f"Result: {add(3, 5)}")

# 3. 带参数的装饰器工厂 (Decorator Factory)
# 接收参数并返回一个装饰器
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("World")

# 4. 类装饰器
# 可以用来装饰类，或者像 Flask 中的 @app.route() 那样使用
class Timer:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        import time
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {self.func.__name__} took {end_time - start_time:.4f} seconds")
        return result

@Timer
def slow_function():
    import time
    time.sleep(1)
    print("Function complete")

slow_function()
