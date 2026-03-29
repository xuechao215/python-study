# 02_inheritance.py
# 继承 (Inheritance)
# 类似于 JS 的 extends

# 1. 父类 (Parent Class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def __str__(self):
        return f"{self.name} is a {self.species}"

# 2. 子类 (Child Class)
# 括号中指定父类
class Dog(Animal):
    def __init__(self, name, breed):
        # 使用 super() 调用父类方法 (JS 也是 super())
        super().__init__(name, species="Dog")
        self.breed = breed
    
    # 重写方法 (Overriding)
    def make_sound(self):
        print(f"{self.name} barks.")
    
    def fetch(self):
        print(f"{self.name} fetches the ball.")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="Cat")
    
    def make_sound(self):
        print(f"{self.name} meows.")

# 3. 多重继承 (Multiple Inheritance)
# Python 支持多重继承 (JS 不支持)
class Flyer:
    def fly(self):
        print("I can fly!")

class Swimmer:
    def swim(self):
        print("I can swim!")

class Duck(Animal, Flyer, Swimmer):
    def __init__(self, name):
        super().__init__(name, species="Duck")
    
    def make_sound(self):
        print("Quack!")

# 4. 测试
buddy = Dog("Buddy", "Golden Retriever")
whiskers = Cat("Whiskers")
donald = Duck("Donald")

print(buddy)
buddy.make_sound()
buddy.fetch()

print(whiskers)
whiskers.make_sound()

print(donald)
donald.make_sound()
donald.fly()
donald.swim()

# 5. isinstance() 和 issubclass()
# 检查实例类型
print(f"Is buddy a Dog? {isinstance(buddy, Dog)}")
print(f"Is buddy an Animal? {isinstance(buddy, Animal)}")

# 检查子类关系
print(f"Is Dog subclass of Animal? {issubclass(Dog, Animal)}")
