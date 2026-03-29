# 04_control_flow.py
# 流程控制 (Control Flow)

# 1. 条件语句 (If/Elif/Else)
# 注意:
# - 使用 elif 而不是 else if
# - 使用 : 而不是 {}
# - 缩进 (Indentation) 非常重要
age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# 2. 循环 (For Loops)
# Python 的 for 循环通常用于遍历序列 (列表, 字符串, range())
# 类似于 JS 的 for...of

# range(start, stop, step)
# start: 默认 0
# stop: 不包含
# step: 默认 1
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Index: {i}")

for char in "Python":
    print(char, end=" ")  # 默认 print 换行，end=" " 让它不换行
print()

# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 3. 循环 (While Loops)
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# 4. Break 和 Continue
# break: 终止循环
# continue: 跳过本次循环
for i in range(10):
    if i == 5:
        break  # 遇到 5 停止
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i)  # 只打印 1, 3

# 5. Pass 语句
# 占位符，什么也不做 (类似于 JS 的空代码块 {})
def my_function():
    pass  # 还没想好怎么写，先占个位

# 6. For-Else / While-Else
# Python 特有: 循环正常结束时执行 else (没有被 break 打断)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
