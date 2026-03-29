# Python开发环境配置指南

## 🖥️ 系统要求

### 支持的平台
- **macOS** 10.15+
- **Windows** 10/11
- **Linux** Ubuntu 20.04+, CentOS 7+

### 硬件要求
- 内存：4GB RAM（推荐8GB+）
- 存储：至少2GB可用空间
- 处理器：现代双核处理器

---

## 📦 Python安装

### 1. 检查是否已安装Python
```bash
# 检查Python版本
python --version
python3 --version

# 检查pip版本
pip --version
pip3 --version
```

### 2. 安装Python

#### macOS
```bash
# 使用Homebrew安装
brew install python

# 或从官网下载
# https://www.python.org/downloads/macos/
```

#### Windows
1. 访问 [Python官网](https://www.python.org/downloads/windows/)
2. 下载Python 3.10+安装程序
3. 安装时勾选"Add Python to PATH"

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

#### Linux (CentOS/RHEL)
```bash
sudo yum install python3 python3-pip
```

### 3. 验证安装
```bash
# 验证Python安装
python --version  # 应该显示 Python 3.x.x

# 验证pip安装
pip --version

# 运行Python交互式环境
python
>>> print("Hello, Python!")
>>> exit()
```

---

## 🔧 开发工具配置

### 1. 代码编辑器推荐

#### Visual Studio Code（推荐）
1. 下载安装 [VS Code](https://code.visualstudio.com/)
2. 安装Python扩展：
   - 打开VS Code
   - 按 `Ctrl+Shift+X` (Windows/Linux) 或 `Cmd+Shift+X` (macOS)
   - 搜索 "Python"
   - 安装Microsoft官方的Python扩展

#### PyCharm（专业版）
- 下载 [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/)
- 专业功能：代码分析、调试、测试工具

### 2. 终端配置

#### macOS/Linux
- 使用系统自带的终端或安装iTerm2
- 配置zsh或bash

#### Windows
- 使用 [Windows Terminal](https://aka.ms/terminal)
- 或使用Git Bash（包含在Git安装中）

### 3. 版本控制
```bash
# 安装Git
# macOS
brew install git

# Windows
# 从 https://git-scm.com/download/win 下载

# Linux
sudo apt install git

# 配置Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 🐍 Python虚拟环境

### 为什么需要虚拟环境？
- 隔离项目依赖
- 避免版本冲突
- 便于部署和分享

### 创建虚拟环境

#### 使用venv（Python内置）
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

# 验证激活
# 命令行前应该显示 (venv)
```

#### 使用pipenv（推荐）
```bash
# 安装pipenv
pip install pipenv

# 创建虚拟环境并安装依赖
pipenv install

# 激活虚拟环境
pipenv shell

# 安装包
pipenv install package_name

# 生成requirements.txt
pipenv lock -r > requirements.txt
```

#### 使用conda（数据科学）
```bash
# 安装Miniconda
# https://docs.conda.io/en/latest/miniconda.html

# 创建环境
conda create -n myenv python=3.10

# 激活环境
conda activate myenv
```

---

## 📁 项目结构设置

### 标准Python项目结构
```
my_project/
├── .gitignore          # Git忽略文件
├── README.md           # 项目说明
├── requirements.txt    # 依赖列表
├── setup.py           # 安装配置（可选）
├── src/               # 源代码
│   ├── __init__.py
│   └── main.py
├── tests/             # 测试代码
│   ├── __init__.py
│   └── test_main.py
├── docs/              # 文档
└── data/              # 数据文件（可选）
```

### 本学习项目的结构
```
python-study/
├── 01_basics/         # Python基础
├── 02_data_structures/# 数据结构
├── 03_functions/      # 函数
├── ...               # 其他章节
├── python-project-demo/ # FastAPI项目
├── react-frontend-demo/ # React前端
└── nextjs-shadcn/     # Next.js项目
```

---

## 📚 学习环境准备

### 1. 克隆项目
```bash
# 克隆项目到本地
git clone https://github.com/your-username/python-study.git
cd python-study
```

### 2. 创建虚拟环境
```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. 安装基础依赖
```bash
# 升级pip
pip install --upgrade pip

# 安装常用开发工具
pip install black flake8 mypy pytest

# 安装项目特定依赖（如果需要）
pip install -r python-project-demo/requirements.txt
```

### 4. 配置VS Code
创建 `.vscode/settings.json`：
```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "python.testing.pytestEnabled": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```

---

## 🛠️ 常用开发工具

### 代码格式化
```bash
# 安装black
pip install black

# 格式化代码
black .  # 格式化所有文件
black path/to/file.py  # 格式化单个文件
```

### 代码检查
```bash
# 安装flake8
pip install flake8

# 检查代码
flake8 .  # 检查所有文件
```

### 类型检查
```bash
# 安装mypy
pip install mypy

# 类型检查
mypy .  # 检查所有文件
```

### 测试框架
```bash
# 安装pytest
pip install pytest

# 运行测试
pytest  # 运行所有测试
pytest path/to/test_file.py  # 运行特定测试
```

### 依赖管理
```bash
# 生成requirements.txt
pip freeze > requirements.txt

# 从requirements.txt安装
pip install -r requirements.txt
```

---

## 🔍 调试配置

### 使用pdb（Python调试器）
```python
# 在代码中插入断点
import pdb; pdb.set_trace()

# 常用命令：
# n(ext) - 执行下一行
# s(tep) - 进入函数
# c(ontinue) - 继续执行
# l(ist) - 显示代码
# p(rint) - 打印变量
# q(uit) - 退出调试器
```

### VS Code调试配置
创建 `.vscode/launch.json`：
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}
```

---

## 🚀 快速开始脚本

创建 `setup.sh`（macOS/Linux）或 `setup.bat`（Windows）：

### macOS/Linux (setup.sh)
```bash
#!/bin/bash

echo "Setting up Python learning environment..."

# 检查Python版本
python --version

# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
source .venv/bin/activate

# 升级pip
pip install --upgrade pip

# 安装开发工具
pip install black flake8 mypy pytest

# 安装项目依赖
pip install -r python-project-demo/requirements.txt

echo "Setup complete! Activate virtual environment with: source .venv/bin/activate"
```

### Windows (setup.bat)
```batch
@echo off
echo Setting up Python learning environment...

REM 检查Python版本
python --version

REM 创建虚拟环境
python -m venv .venv

REM 激活虚拟环境
call .venv\Scripts\activate

REM 升级pip
pip install --upgrade pip

REM 安装开发工具
pip install black flake8 mypy pytest

REM 安装项目依赖
pip install -r python-project-demo\requirements.txt

echo Setup complete! Activate virtual environment with: .venv\Scripts\activate
```

---

## ❓ 常见问题

### Q: 安装Python时遇到权限问题？
A: 使用管理员权限或添加`--user`标志：
```bash
pip install --user package_name
```

### Q: 虚拟环境激活失败？
A: 检查系统策略（Windows）：
```powershell
# 以管理员身份运行PowerShell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Q: 包安装太慢？
A: 使用国内镜像源：
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name
```

### Q: 如何卸载Python？
A:
- **macOS**: `brew uninstall python`
- **Windows**: 控制面板 -> 程序和功能
- **Linux**: `sudo apt remove python3`

---

## 📞 获取帮助

### 官方资源
- [Python官方文档](https://docs.python.org/3/)
- [Python社区](https://www.python.org/community/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)

### 学习资源
- [Real Python](https://realpython.com/)
- [Python Crash Course](https://nostarch.com/pythoncrashcourse2e)
- [Automate the Boring Stuff](https://automatetheboringstuff.com/)

### 问题反馈
如果在配置过程中遇到问题：
1. 检查错误信息
2. 搜索相关错误
3. 查看项目Issue
4. 联系维护者

---

**环境配置完成！现在可以开始你的Python学习之旅了。从[01_basics](../01_basics/)开始学习吧！**