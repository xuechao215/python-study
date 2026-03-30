# 03_pip_venv.md
# 包管理与虚拟环境 (Pip & Virtual Environments)
# 类似于 JS 的 npm/yarn 和 node_modules 的概念

## 1. 包管理器 (Pip)
# Pip 是 Python 的包安装程序 (Package Installer for Python)
# 类似于 Node.js 的 npm

### 常用命令
- **安装包**: `pip install package_name`
  - 类似于 `npm install package_name`
  - 安装特定版本: `pip install package_name==1.2.3`
  - 安装最新版本: `pip install package_name --upgrade`
- **卸载包**: `pip uninstall package_name`
  - 类似于 `npm uninstall package_name`
- **列出已安装包**: `pip list`
  - 类似于 `npm list`
  - 显示过时的包: `pip list --outdated`
- **导出依赖**: `pip freeze > requirements.txt`
  - 类似于 `package.json` 中的 dependencies，但这只是一个快照
  - 只导出项目依赖: `pip freeze --local > requirements.txt`
- **安装所有依赖**: `pip install -r requirements.txt`
  - 类似于 `npm install` (基于 package.json)
- **搜索包**: `pip search package_name`
  - 类似于 `npm search package_name`
- **显示包信息**: `pip show package_name`
  - 显示包的详细信息，包括版本、位置、依赖等

### Pip 高级用法
- **从 requirements.txt 安装**: `pip install -r requirements.txt`
- **从本地目录安装**: `pip install ./local_package/`
- **从 Git 仓库安装**: `pip install git+https://github.com/user/repo.git`
- **从特定分支安装**: `pip install git+https://github.com/user/repo.git@branch_name`
- **安装开发依赖**: `pip install -e .` (可编辑模式，适合本地开发)
- **缓存管理**:
  - 查看缓存: `pip cache dir`
  - 清理缓存: `pip cache purge`
- **配置镜像源** (国内加速):
  ```bash
  # 临时使用
  pip install package_name -i https://pypi.tuna.tsinghua.edu.cn/simple

  # 永久配置
  pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
  ```

## 2. 虚拟环境 (Virtual Environments)
# 在 Python 中，默认情况下包是安装在全局环境中的
# 这会导致不同项目之间的依赖冲突 (例如 Project A 需要 Django 2.0，Project B 需要 Django 3.0)
# 为了解决这个问题，Python 使用虚拟环境 (venv)

# 类似于 Node.js 的 node_modules 目录 (每个项目都有独立的依赖)
# 但 Python 需要显式激活虚拟环境

### 创建虚拟环境
```bash
# 在项目根目录下运行
python -m venv venv
# 这会创建一个名为 venv 的目录 (类似于 node_modules)

# 指定 Python 版本 (如果系统有多个 Python 版本)
python3.9 -m venv venv

# 创建纯净环境 (不包含 pip 等工具)
python -m venv venv --without-pip

# 创建包含系统站点包的虚拟环境
python -m venv venv --system-site-packages
```

### 激活虚拟环境
- **Windows**:
  ```bash
  venv\Scripts\activate
  # 或使用 PowerShell
  venv\Scripts\Activate.ps1
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 退出虚拟环境
```bash
deactivate
```

### 检查虚拟环境状态
```bash
# 查看当前 Python 解释器路径
which python
# 或
where python (Windows)

# 查看 pip 路径
which pip
# 或
where pip (Windows)

# 检查是否在虚拟环境中 (查看 Python 路径是否包含 venv)
python -c "import sys; print(sys.prefix)"
```

### 为什么要使用虚拟环境?
- **隔离依赖**: 每个项目拥有独立的库版本，互不干扰
- **避免权限问题**: 不需要管理员权限即可安装包
- **保持系统清洁**: 不会污染全局 Python 环境
- **可重复性**: 确保项目在不同机器上运行一致
- **多版本支持**: 同时支持不同 Python 版本的项目
- **测试环境**: 为测试创建独立的环境

### 虚拟环境的其他类型
除了内置的 `venv`，还有其他虚拟环境工具：

1. **virtualenv** (第三方，功能更强大):
   ```bash
   pip install virtualenv
   virtualenv myenv
   ```

2. **conda** (Anaconda 发行版):
   ```bash
   # 创建环境
   conda create --name myenv python=3.9

   # 激活环境
   conda activate myenv

   # 退出环境
   conda deactivate
   ```

3. **pipenv** (结合了 pip 和 virtualenv):
   ```bash
   pip install pipenv
   pipenv install package_name
   pipenv shell  # 进入虚拟环境
   ```

4. **poetry** (现代依赖管理工具):
   ```bash
   pip install poetry
   poetry new project_name
   poetry add package_name
   poetry shell  # 进入虚拟环境
   ```

## 3. 依赖管理文件格式

### requirements.txt 格式
```txt
# 基本格式
package_name==1.2.3

# 版本范围
package_name>=1.2.0,<2.0.0

# Git 仓库
git+https://github.com/user/repo.git@branch_name

# 本地文件
./local_package/

# 注释
# 这是开发依赖
pytest==6.2.5

# 环境标记
requests==2.25.1 ; python_version >= "3.6"
```

### 分离开发和生产依赖
```txt
# requirements.txt (生产依赖)
Flask==2.0.1
requests==2.26.0

# requirements-dev.txt (开发依赖)
-r requirements.txt  # 包含生产依赖
pytest==6.2.5
black==21.9b0
flake8==4.0.1
```

### setup.py 和 setup.cfg
用于打包和分发 Python 包，类似于 `package.json`:
```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "flask>=2.0.0",
    ],
    extras_require={
        "dev": ["pytest", "black"],
        "test": ["pytest", "coverage"],
    },
)
```

### pyproject.toml (现代标准)
```toml
# pyproject.toml (poetry 使用)
[tool.poetry]
name = "my-project"
version = "0.1.0"

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.26.0"

[tool.poetry.dev-dependencies]
pytest = "^6.2.5"
black = "^21.9b0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

## 4. 最佳实践

### 项目结构示例
```
my_project/
├── .gitignore          # 忽略 venv/, __pycache__/, *.pyc 等
├── README.md
├── requirements.txt    # 生产依赖
├── requirements-dev.txt # 开发依赖
├── src/               # 源代码
│   └── my_module.py
├── tests/             # 测试代码
│   └── test_my_module.py
└── venv/              # 虚拟环境 (被 .gitignore 忽略)
```

### 工作流程
1. **创建项目**:
   ```bash
   mkdir my_project
   cd my_project
   python -m venv venv
   ```

2. **激活虚拟环境**:
   ```bash
   # macOS/Linux
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

3. **安装依赖**:
   ```bash
   pip install flask requests
   pip install pytest black --dev  # 开发依赖
   ```

4. **导出依赖**:
   ```bash
   pip freeze > requirements.txt
   # 或只导出项目依赖
   pip freeze --local > requirements.txt
   ```

5. **共享项目**:
   - 将 `requirements.txt` 加入版本控制
   - 在 `.gitignore` 中添加 `venv/`
   - 其他开发者: `pip install -r requirements.txt`

### 高级技巧
1. **使用 pip-tools 管理精确版本**:
   ```bash
   pip install pip-tools
   # 创建 requirements.in (声明依赖)
   echo "flask>=2.0.0" > requirements.in
   echo "requests>=2.25.0" >> requirements.in

   # 编译为 requirements.txt (锁定版本)
   pip-compile requirements.in

   # 同步环境
   pip-sync requirements.txt
   ```

2. **环境变量配置**:
   ```bash
   # 设置 pip 镜像源
   export PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

   # 设置 pip 缓存目录
   export PIP_CACHE_DIR=~/.cache/pip
   ```

3. **Docker 集成**:
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   # 复制依赖文件
   COPY requirements.txt .

   # 安装依赖
   RUN pip install --no-cache-dir -r requirements.txt

   # 复制应用代码
   COPY . .

   CMD ["python", "app.py"]
   ```

4. **CI/CD 集成**:
   ```yaml
   # GitHub Actions 示例
   name: Python CI

   on: [push]

   jobs:
     test:
       runs-on: ubuntu-latest

       steps:
       - uses: actions/checkout@v2

       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.9'

       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install -r requirements.txt
           pip install -r requirements-dev.txt

       - name: Run tests
         run: |
           pytest
   ```

### 常见问题解决
1. **权限错误**: 使用虚拟环境避免 `sudo pip install`
2. **版本冲突**: 使用虚拟环境隔离不同项目的依赖
3. **依赖解析失败**: 尝试 `pip install --upgrade pip setuptools wheel`
4. **下载慢**: 使用国内镜像源
5. **环境不一致**: 使用 `pip freeze` 确保版本一致

### 工具比较
| 工具 | 优点 | 缺点 | 类似 JS 工具 |
|------|------|------|-------------|
| **pip + venv** | 内置，简单 | 需要手动管理 | npm + node_modules |
| **pipenv** | 自动管理虚拟环境 | 性能问题 | yarn |
| **poetry** | 现代，功能全面 | 学习曲线 | pnpm |
| **conda** | 科学计算友好 | 体积大 | - |

### 总结
- **简单项目**: 使用 `pip + venv + requirements.txt`
- **中型项目**: 考虑 `poetry` 或 `pipenv`
- **科学计算**: 使用 `conda`
- **团队协作**: 确保依赖版本锁定，使用 CI/CD 自动化测试

## 5. 示例项目

为了帮助理解这些概念，我们创建了一个完整的示例项目：

### 项目结构
```
05_modules_packages/example_project/
├── .gitignore          # 忽略虚拟环境和缓存文件
├── README.md           # 项目说明
├── USAGE.md           # 详细使用说明
├── requirements.txt    # 生产依赖
├── requirements-dev.txt # 开发依赖
├── src/               # 源代码
│   └── app.py         # Flask 示例应用
└── tests/             # 测试代码
    └── test_app.py    # 测试文件
```

### 快速体验
```bash
# 进入示例项目目录
cd 05_modules_packages/example_project

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 运行应用
python src/app.py

# 运行测试
pytest tests/
```

### 示例应用功能
1. **虚拟环境检测**: 检查是否在虚拟环境中运行
2. **依赖验证**: 验证所有必要依赖是否安装
3. **API 端点**: 提供 RESTful API 示例
4. **外部 API 调用**: 演示 requests 库的使用
5. **配置管理**: 使用环境变量和 .env 文件
6. **日志记录**: 使用 loguru 进行结构化日志记录

### 学习要点
通过这个示例项目，你可以学习到：
1. 如何正确设置虚拟环境
2. 如何管理生产和开发依赖
3. 如何组织项目结构
4. 如何编写可测试的代码
5. 如何使用现代 Python 开发工具
6. 如何部署 Python 应用

## 6. 进一步学习资源

### 官方文档
- [Python Packaging User Guide](https://packaging.python.org/)
- [pip Documentation](https://pip.pypa.io/)
- [venv Documentation](https://docs.python.org/3/library/venv.html)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Pipenv Documentation](https://pipenv.pypa.io/)

### 中文资源
- [Python 打包用户指南 (中文)](https://packaging.python.org/zh_CN/)
- [pip 中文文档](https://pip.pypa.io/zh_CN/)
- [Python 虚拟环境教程](https://docs.python.org/zh-cn/3/tutorial/venv.html)

### 视频教程
- [Python 虚拟环境全面指南](https://www.youtube.com/watch?v=KxvKCSwlUv8)
- [Poetry 入门教程](https://www.youtube.com/watch?v=0f3moPe_bhk)
- [Python 依赖管理最佳实践](https://www.youtube.com/watch?v=GIF3LaRqgXo)

### 书籍推荐
- 《Python 编程：从入门到实践》
- 《流畅的 Python》
- 《Effective Python》

记住：掌握虚拟环境和依赖管理是成为专业 Python 开发者的关键一步。从简单的 `pip + venv` 开始，随着项目复杂度增加，逐步学习更高级的工具。
