# Frontend (JS/TS) to Python Comparison Cheat Sheet

| Feature | JavaScript / TypeScript | Python | Notes |
| :--- | :--- | :--- | :--- |
| **Output** | `console.log("Hello")` | `print("Hello")` | |
| **Variables** | `let x = 10; const y = 20;` | `x = 10` `y = 20` | Python has no `const` keyword (convention: uppercase for constants) |
| **Comments** | `// Single`, `/* Multi */` | `# Single`, `""" Multi """` | |
| **Blocks** | `{ ... }` | Indentation (4 spaces) | Critical difference! |
| **Strings** | `"..."`, `'...'`, `` `...${var}` `` | `"..."`, `'...'`, `f"...{var}"` | Python f-strings are like template literals |
| **Booleans** | `true`, `false` | `True`, `False` | Capitalized in Python |
| **Null** | `null`, `undefined` | `None` | Only `None` in Python |
| **Operators** | `&&`, `\|\|`, `!` | `and`, `or`, `not` | English words in Python |
| **Comparison** | `===`, `!==` | `==`, `!=` | Python `==` checks value equality (like deep equal) |
| **Increment** | `i++`, `i--` | `i += 1`, `i -= 1` | No `++` or `--` in Python |
| **Loops** | `for (let i of arr)` | `for i in arr:` | |
| **Ranges** | `for (let i=0; i<10; i++)` | `for i in range(10):` | |
| **Functions** | `function foo() {}` | `def foo():` | |
| **Arrow Func** | `(x) => x * x` | `lambda x: x * x` | Python lambdas are limited to expressions |
| **Classes** | `class Dog extends Animal` | `class Dog(Animal):` | |
| **Constructor**| `constructor(name)` | `def __init__(self, name):` | `self` is explicit `this` |
| **Context** | `this` | `self` | Must be first arg in methods |
| **Modules** | `import { x } from './m'` | `from m import x` | |
| **Async** | `async/await`, `Promise` | `async/await`, `asyncio` | Python has `asyncio` for async programming |
| **Array** | `[1, 2, 3]` | `[1, 2, 3]` (List) | Lists are mutable arrays |
| **Object** | `{ key: "value" }` | `{ "key": "value" }` (Dict) | Keys must be hashable (usually strings/numbers) |
| **Set** | `new Set([1, 2])` | `{1, 2}` (Set) | |
| **Map** | `new Map()` | `{}` (Dict) | Python dicts are ordered (since 3.7) |
| **Length** | `arr.length` | `len(arr)` | Global function `len()` |
| **Type Check** | `typeof x`, `x instanceof Y` | `type(x)`, `isinstance(x, Y)` | |
| **Error Handling**| `try { ... } catch (e) { ... }` | `try: ... except Exception as e: ...` | |
| **Throw** | `throw new Error("...")` | `raise Exception("...")` | `raise` keyword |

## Key Differences for Frontend Devs

1.  **Indentation matters**: Python uses indentation to define code blocks, not curly braces `{}`. This enforces clean code formatting but can be tricky initially.
2.  **`self` is explicit**: In methods, `self` (equivalent to `this`) must be the first parameter.
3.  **True/False/None**: Capitalized first letters.
4.  **`elif`**: Used instead of `else if`.
5.  **List Comprehensions**: A powerful way to create lists (e.g., `[x*2 for x in nums]`), often replacing `map` and `filter`.
6.  **`len()` function**: Used instead of `.length` property.
7.  **Slicing**: `arr[1:4]` is very common and powerful in Python.
8.  **Variables**: No declaration keywords (`var`, `let`, `const`).
9.  **Mutable Default Arguments**: Be careful! `def foo(l=[])` shares the same list across calls. Use `None` instead.
