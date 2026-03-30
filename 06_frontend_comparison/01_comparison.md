# 前端(JS/TS)与Python对比速查表

| 功能 | JavaScript / TypeScript | Python | 说明 |
| :--- | :--- | :--- | :--- |
| **输出** | `console.log("Hello")` | `print("Hello")` | |
| **变量** | `let x = 10; const y = 20;` | `x = 10` `y = 20` | Python没有`const`关键字(约定：大写表示常量) |
| **注释** | `// 单行`, `/* 多行 */` | `# 单行`, `""" 多行 """` | |
| **代码块** | `{ ... }` | 缩进(4个空格) | 关键区别！ |
| **字符串** | `"..."`, `'...'`, `` `...${var}` `` | `"..."`, `'...'`, `f"...{var}"` | Python的f-string类似模板字符串 |
| **布尔值** | `true`, `false` | `True`, `False` | Python中首字母大写 |
| **空值** | `null`, `undefined` | `None` | Python只有`None` |
| **逻辑运算符** | `&&`, `\|\|`, `!` | `and`, `or`, `not` | Python使用英文单词 |
| **比较运算符** | `===`, `!==` | `==`, `!=` | Python的`==`检查值相等(类似深度相等) |
| **自增/自减** | `i++`, `i--` | `i += 1`, `i -= 1` | Python没有`++`或`--`运算符 |
| **循环** | `for (let i of arr)` | `for i in arr:` | |
| **范围循环** | `for (let i=0; i<10; i++)` | `for i in range(10):` | |
| **函数** | `function foo() {}` | `def foo():` | |
| **箭头函数** | `(x) => x * x` | `lambda x: x * x` | Python的lambda仅限于表达式 |
| **类** | `class Dog extends Animal` | `class Dog(Animal):` | |
| **构造函数**| `constructor(name)` | `def __init__(self, name):` | `self`是显式的`this` |
| **上下文** | `this` | `self` | 必须是方法的第一个参数 |
| **模块导入** | `import { x } from './m'` | `from m import x` | |
| **异步编程** | `async/await`, `Promise` | `async/await`, `asyncio` | Python使用`asyncio`进行异步编程 |
| **数组** | `[1, 2, 3]` | `[1, 2, 3]` (列表) | 列表是可变数组 |
| **对象** | `{ key: "value" }` | `{ "key": "value" }` (字典) | 键必须是可哈希的(通常是字符串/数字) |
| **集合** | `new Set([1, 2])` | `{1, 2}` (集合) | |
| **映射** | `new Map()` | `{}` (字典) | Python字典是有序的(自3.7起) |
| **长度** | `arr.length` | `len(arr)` | 全局函数`len()` |
| **类型检查** | `typeof x`, `x instanceof Y` | `type(x)`, `isinstance(x, Y)` | |
| **错误处理**| `try { ... } catch (e) { ... }` | `try: ... except Exception as e: ...` | |
| **抛出错误** | `throw new Error("...")` | `raise Exception("...")` | `raise`关键字 |
| **条件语句** | `if (x > 0) { ... } else if (x < 0) { ... }` | `if x > 0: ... elif x < 0: ...` | Python使用`elif`而不是`else if` |
| **三元运算符** | `x > 0 ? "positive" : "negative"` | `"positive" if x > 0 else "negative"` | 语法不同 |
| **解构赋值** | `const {name, age} = person` | `name, age = person["name"], person["age"]` | Python没有内置解构 |
| **展开运算符** | `[...arr1, ...arr2]` | `[*arr1, *arr2]` | Python使用`*`运算符 |
| **可选链** | `obj?.prop?.nested` | `obj.get("prop", {}).get("nested")` | Python没有内置可选链 |
| **空值合并** | `x ?? "default"` | `x if x is not None else "default"` | Python使用显式检查 |
| **数组方法** | `arr.map(x => x*2)` | `[x*2 for x in arr]` | 列表推导式 |
| **数组方法** | `arr.filter(x => x > 0)` | `[x for x in arr if x > 0]` | 列表推导式 |
| **数组方法** | `arr.reduce((sum, x) => sum + x, 0)` | `sum(arr)` | 内置`sum()`函数 |
| **对象方法** | `Object.keys(obj)` | `list(obj.keys())` | 返回列表而不是数组 |
| **对象方法** | `Object.values(obj)` | `list(obj.values())` | 返回列表而不是数组 |
| **对象方法** | `Object.entries(obj)` | `list(obj.items())` | 返回列表而不是数组 |
| **字符串方法** | `str.includes("sub")` | `"sub" in str` | 使用`in`运算符 |
| **字符串方法** | `str.startsWith("pre")` | `str.startswith("pre")` | 方法名不同 |
| **字符串方法** | `str.endsWith("suf")` | `str.endswith("suf")` | 方法名不同 |
| **字符串方法** | `str.split(",")` | `str.split(",")` | 相同 |
| **字符串方法** | `str.trim()` | `str.strip()` | 方法名不同 |
| **日期处理** | `new Date()` | `import datetime; datetime.datetime.now()` | 需要导入模块 |
| **JSON处理** | `JSON.parse(str)` | `import json; json.loads(str)` | 需要导入模块 |
| **JSON处理** | `JSON.stringify(obj)` | `import json; json.dumps(obj)` | 需要导入模块 |
| **定时器** | `setTimeout(fn, 1000)` | `import time; time.sleep(1)` | 阻塞式睡眠 |
| **定时器** | `setInterval(fn, 1000)` | `import threading; threading.Timer(1, fn)` | 需要线程 |
| **文件操作** | `fs.readFileSync("file.txt")` | `open("file.txt").read()` | 内置函数 |
| **正则表达式** | `/pattern/g` | `import re; re.compile("pattern")` | 需要导入模块 |

## 前端开发者需要了解的关键差异

### 1. 语法差异
- **缩进很重要**：Python使用缩进来定义代码块，而不是花括号`{}`。这强制了干净的代码格式，但一开始可能会不习惯。
- **`self`是显式的**：在方法中，`self`(相当于`this`)必须是第一个参数。
- **`True/False/None`**：首字母大写。
- **`elif`**：使用`elif`而不是`else if`。
- **变量**：没有声明关键字(`var`, `let`, `const`)。

### 2. 数据结构和操作
- **列表推导式**：创建列表的强大方式(例如`[x*2 for x in nums]`)，通常替代`map`和`filter`。
- **切片**：`arr[1:4]`在Python中非常常见且强大。
- **`len()`函数**：使用`len(arr)`而不是`.length`属性。
- **字典(Dict)**：Python的字典类似于JavaScript的对象，但键必须是可哈希的。
- **集合(Set)**：使用`{1, 2, 3}`语法创建集合。

### 3. 函数和类
- **可变默认参数**：小心！`def foo(l=[])`会在多次调用中共享同一个列表。应该使用`None`代替。
- **lambda函数限制**：Python的lambda仅限于单个表达式，不能包含语句。
- **装饰器**：Python特有的功能，用于修改函数或类的行为。
- **属性访问**：Python使用`obj.attr`而不是`obj["attr"]`，但两者都可以用于字典。

### 4. 异步编程
- **async/await**：语法类似，但Python使用`asyncio`库。
- **事件循环**：Python需要显式管理事件循环。
- **并发模型**：Python有线程、进程和协程三种并发模型。

### 5. 工具和生态系统
- **包管理**：使用`pip`而不是`npm`。
- **虚拟环境**：使用`venv`或`conda`创建隔离的环境。
- **类型提示**：Python有可选的类型提示，类似于TypeScript。
- **测试框架**：`pytest`是主要的测试框架，类似Jest。

### 6. 常见陷阱
- **引用传递**：Python中大多数对象是引用传递，修改可变对象会影响所有引用。
- **整数除法**：Python 3中`/`总是返回浮点数，`//`返回整数。
- **作用域**：Python有函数作用域，没有块级作用域。
- **迭代器**：Python的`for`循环使用迭代器，而不是索引。
- **字符串不可变**：Python字符串不可变，修改会创建新字符串。

## 实用转换示例

### JavaScript → Python
```javascript
// JavaScript
const users = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 30 }
];

const adultNames = users
  .filter(user => user.age >= 18)
  .map(user => user.name);

console.log(adultNames);
```

```python
# Python
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

adult_names = [user["name"] for user in users if user["age"] >= 18]

print(adult_names)
```

### 异步示例
```javascript
// JavaScript
async function fetchData(url) {
  const response = await fetch(url);
  const data = await response.json();
  return data;
}
```

```python
# Python
import aiohttp
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data
```

## 学习建议

1. **从基础语法开始**：先掌握Python的基本语法和数据结构。
2. **理解Pythonic风格**：学习Python的惯用写法，如列表推导式、生成器表达式等。
3. **熟悉标准库**：Python有丰富的标准库，学习常用的模块如`os`、`sys`、`json`、`datetime`等。
4. **练习项目转换**：尝试将小型JavaScript项目转换为Python，加深理解。
5. **关注生态系统**：了解Python在Web开发、数据分析、机器学习等领域的流行框架。

## 资源推荐

- **官方文档**：[Python官方文档](https://docs.python.org/3/)
- **教程**：[Python教程](https://docs.python.org/3/tutorial/)
- **对比文章**：[Python vs JavaScript](https://realpython.com/python-vs-javascript/)
- **练习平台**：[LeetCode](https://leetcode.com/)、[HackerRank](https://www.hackerrank.com/)

记住，从JavaScript/TypeScript转向Python主要是思维方式的转变。Python更强调"显式优于隐式"，代码通常更简洁，但需要更严格的格式要求。随着练习，你会逐渐适应Python的哲学和风格。
