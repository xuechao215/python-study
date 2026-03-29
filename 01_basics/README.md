# 01_basics - Python基础语法

## 🎯 学习目标
- 掌握Python的基本语法结构
- 理解Python与JavaScript的语法差异
- 能够编写简单的Python程序
- 熟悉Python的开发环境

## 📚 内容概览

### 01_hello_world.py
- Python的Hello World程序
- 打印输出：`print()`函数
- 注释语法：单行注释(`#`)和多行注释(`""" """`)
- 字符串格式化：f-string（类似JS的模板字符串）

### 02_variables.py
- 变量声明：无需关键字，直接赋值
- 数据类型：int, float, str, bool, None
- 类型检查：`type()`函数
- 类型转换：`int()`, `float()`, `str()`
- 多变量赋值和交换

### 03_operators.py
- 算术运算符：`+`, `-`, `*`, `/`, `//`, `%`, `**`
- 赋值运算符：`+=`, `-=`, `*=`, `/=`
- 比较运算符：`==`, `!=`, `>`, `<`, `>=`, `<=`
- 逻辑运算符：`and`, `or`, `not`（对应JS的`&&`, `||`, `!`）
- 身份运算符：`is`, `is not`（检查对象引用）
- 成员运算符：`in`, `not in`（检查序列成员）

### 04_control_flow.py
- 条件语句：`if`, `elif`, `else`
- 循环语句：`for`, `while`
- 循环控制：`break`, `continue`, `pass`
- 范围函数：`range(start, stop, step)`
- Python特有的for-else/while-else结构

## 🔑 关键概念

### Python与JavaScript的主要差异
1. **语法结构**：Python使用缩进而不是花括号`{}`
2. **变量声明**：无需`var`, `let`, `const`关键字
3. **布尔值**：`True`/`False`（首字母大写）
4. **空值**：`None`（对应JS的`null`/`undefined`）
5. **逻辑运算符**：使用英文单词`and`, `or`, `not`
6. **相等比较**：`==`检查值相等（类似JS的`===`）

### 重要提示
- **缩进非常重要**：Python使用缩进来定义代码块
- **冒号`:`**：在`if`, `for`, `while`, `def`, `class`等语句后需要冒号
- **动态类型**：Python是动态类型语言，类似JavaScript
- **命名规范**：推荐使用snake_case（蛇形命名法）

## 💻 实践练习

### 基础练习
1. 编写一个程序，计算并打印1到100的和
2. 创建一个温度转换器：摄氏转华氏，华氏转摄氏
3. 编写一个简单的计算器，支持加、减、乘、除

### 进阶挑战
1. 实现一个猜数字游戏
2. 创建一个简单的用户登录系统
3. 编写一个程序，统计一段文本中的单词频率

## 📖 学习建议

1. **动手实践**：每个示例都自己运行一遍
2. **对比学习**：思考每个概念在JavaScript中如何实现
3. **修改实验**：尝试修改代码，观察结果变化
4. **查阅文档**：遇到不理解的函数，使用`help()`函数或查阅官方文档

## 🔗 相关资源
- [Python官方教程](https://docs.python.org/3/tutorial/)
- [Python与JavaScript对比指南](./../06_frontend_comparison/01_comparison.md)
- [Python标准库文档](https://docs.python.org/3/library/)

## 🚀 下一步
完成本章学习后，可以继续学习：
- [02_data_structures](../02_data_structures/) - Python数据结构
- [03_functions](../03_functions/) - 函数定义和使用
- [EXERCISES.md](../EXERCISES.md) - 练习题