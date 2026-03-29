# 01_classes_objects.py
# 类与对象 (Class & Object)
# 类似于 JS 的 class (ES6)

# 1. 定义类
# 使用 class 关键字，首字母大写 (PascalCase)
class Dog:
    """
    这是一个 Dog 类
    """
    # 类属性 (Class Attribute)
    # 所有实例共享的属性 (类似于 JS 的 static 属性，但其实更像 prototype 上的属性)
    species = "Canis familiaris"

    # 初始化方法 (Constructor)
    # 类似于 JS 的 constructor()
    def __init__(self, name, age):
        # 实例属性 (Instance Attribute)
        # 每个实例独有的属性
        # self 相当于 JS 的 this
        self.name = name
        self.age = age

    # 实例方法 (Instance Method)
    # 必须包含 self 参数作为第一个参数
    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# 2. 创建对象 (实例化)
# 不需要 new 关键字
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

# 3. 访问属性和方法
print(f"Buddy's name: {buddy.name}")
print(f"Buddy's age: {buddy.age}")
print(f"Buddy's species: {buddy.species}")

print(buddy.description())
print(buddy.speak("Woof Woof"))

# 4. 修改属性
buddy.age = 10
print(f"Buddy is now {buddy.age}")

# 5. 动态添加属性
# Python 允许动态添加属性 (不推荐，但可行)
buddy.color = "Golden"
print(f"Buddy is {buddy.color}")
# miles.color  # 报错: AttributeError

# 6. self 参数
# self 代表实例本身
# 当调用 buddy.speak("Woof") 时，Python 实际上调用的是 Dog.speak(buddy, "Woof")
# 所以 self 会自动传入
