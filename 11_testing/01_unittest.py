# 01_unittest.py
# 单元测试 (Unit Testing)
# 使用 Python 标准库 unittest (类似于 Jest, Mocha)

import unittest

# 被测试的函数
def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# 测试类 (Test Case)
# 必须继承自 unittest.TestCase
class TestMathOperations(unittest.TestCase):
    
    # 钩子方法: 在每个测试方法前运行 (类似 beforeEach)
    def setUp(self):
        print("Setting up...")

    # 钩子方法: 在每个测试方法后运行 (类似 afterEach)
    def tearDown(self):
        print("Tearing down...")

    # 测试方法必须以 test_ 开头
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(10, 3), 3.3333333, places=7)

    def test_divide_by_zero(self):
        # 测试异常 (类似 expect(() => ...).toThrow())
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    # 运行所有测试
    unittest.main()
