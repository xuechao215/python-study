# 04_scope.py
# 作用域 (Scope)
# 类似于 JS 的 var, let, const 的作用域

# 1. 局部作用域 (Local Scope)
# 函数内部定义的变量
def my_func():
    x = 10
    print(f"Inside func: {x}")

my_func()
# print(x)  # 报错: NameError: name 'x' is not defined

# 2. 全局作用域 (Global Scope)
# 函数外部定义的变量
y = 20

def my_func_2():
    print(f"Inside func 2: {y}")

my_func_2()
print(f"Outside func 2: {y}")

# 3. 修改全局变量 (global 关键字)
# 类似于 JS 中直接修改 window.y (如果不使用 var/let/const)
# 但 Python 要求显式声明 global
z = 30

def modify_global():
    global z  # 声明 z 是全局变量
    z = 40
    print(f"Inside modify_global: {z}")

modify_global()
print(f"Outside modify_global: {z}")

# 4. 嵌套函数 (Nested Functions)
# 闭包 (Closure)
def outer():
    x = "outer"
    
    def inner():
        nonlocal x  # 声明 x 是外部函数的变量 (不是全局变量)
        x = "inner"
        print(f"Inside inner: {x}")
    
    inner()
    print(f"Inside outer: {x}")

outer()

# 5. 作用域查找顺序 (LEGB)
# Local (局部) -> Enclosing (闭包) -> Global (全局) -> Built-in (内置)
# 如果都找不到，则报错 NameError

# 6. Built-in (内置)
# 例如 print, len, range 等
# 如果定义了同名变量，会覆盖内置函数 (慎用!)
# print = "Oops"
# print("Hello")  # 报错: TypeError: 'str' object is not callable
