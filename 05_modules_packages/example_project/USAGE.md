# 使用说明

这个示例项目展示了 Python 虚拟环境和依赖管理的最佳实践。

## 1. 设置虚拟环境

### 创建虚拟环境
```bash
# 在项目根目录下
python -m venv venv
```

### 激活虚拟环境
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 验证虚拟环境
```bash
# 检查 Python 路径
which python
# 应该显示: /path/to/project/venv/bin/python

# 检查 pip 路径
which pip
# 应该显示: /path/to/project/venv/bin/pip
```

## 2. 安装依赖

### 安装生产依赖
```bash
pip install -r requirements.txt
```

### 安装开发依赖
```bash
pip install -r requirements-dev.txt
```

### 手动安装特定包
```bash
# 安装包
pip install package_name

# 安装特定版本
pip install package_name==1.2.3

# 升级包
pip install --upgrade package_name
```

## 3. 运行应用

### 直接运行
```bash
python src/app.py
```

### 使用环境变量
```bash
# 设置环境变量
export DEBUG=true
export PORT=8080

# 运行应用
python src/app.py
```

### 使用 .env 文件
```bash
# 创建 .env 文件
echo "DEBUG=true" > .env
echo "PORT=8080" >> .env
echo "SECRET_KEY=my-secret-key" >> .env

# 运行应用
python src/app.py
```

## 4. 开发工作流

### 代码格式化
```bash
# 格式化所有 Python 文件
black src/ tests/

# 检查格式化
black --check src/ tests/

# 导入排序
isort src/ tests/
```

### 代码检查
```bash
# 语法和风格检查
flake8 src/ tests/

# 类型检查
mypy src/

# 代码质量检查
pylint src/
```

### 运行测试
```bash
# 运行所有测试
pytest tests/

# 运行特定测试
pytest tests/test_app.py::test_index_endpoint

# 运行测试并显示覆盖率
pytest --cov=src tests/

# 生成覆盖率报告
pytest --cov=src --cov-report=html tests/
```

## 5. 依赖管理

### 更新依赖
```bash
# 更新所有包到最新版本
pip install --upgrade -r requirements.txt

# 更新特定包
pip install --upgrade package_name
```

### 导出当前依赖
```bash
# 导出所有依赖
pip freeze > requirements.txt

# 只导出项目依赖（排除系统包）
pip freeze --local > requirements.txt

# 导出开发依赖
pip freeze --local | grep -E "(pytest|black|flake8|mypy)" > requirements-dev.txt
```

### 使用 pip-tools 管理版本
```bash
# 安装 pip-tools
pip install pip-tools

# 创建 requirements.in (声明依赖)
echo "flask>=2.0.0" > requirements.in
echo "requests>=2.25.0" >> requirements.in

# 编译为 requirements.txt (锁定版本)
pip-compile requirements.in

# 同步环境
pip-sync requirements.txt
```

## 6. 虚拟环境管理

### 常用命令
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 退出虚拟环境
deactivate

# 删除虚拟环境
rm -rf venv/  # macOS/Linux
rmdir /s venv # Windows
```

### 虚拟环境信息
```bash
# 检查是否在虚拟环境中
echo $VIRTUAL_ENV  # macOS/Linux
echo %VIRTUAL_ENV% # Windows

# 查看虚拟环境中的包
pip list

# 查看包详细信息
pip show package_name
```

## 7. 项目部署

### 生产环境设置
```bash
# 1. 创建虚拟环境
python -m venv venv

# 2. 激活虚拟环境
source venv/bin/activate

# 3. 安装生产依赖
pip install -r requirements.txt

# 4. 运行应用
python src/app.py
```

### Docker 部署
```bash
# 构建镜像
docker build -t my-app .

# 运行容器
docker run -p 5000:5000 my-app
```

## 8. 故障排除

### 常见问题

#### 1. 权限错误
```bash
# 错误: Permission denied
# 解决: 不要使用 sudo，使用虚拟环境
python -m venv venv
source venv/bin/activate
pip install package_name
```

#### 2. 版本冲突
```bash
# 错误: Could not find a version that satisfies the requirement
# 解决: 检查 requirements.txt 中的版本要求
# 或使用虚拟环境隔离
```

#### 3. 下载慢
```bash
# 使用国内镜像源
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name

# 永久设置镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 4. 依赖解析失败
```bash
# 更新 pip 和 setuptools
pip install --upgrade pip setuptools wheel

# 清理缓存
pip cache purge
```

### 环境检查脚本
```bash
#!/bin/bash
# check_env.sh

echo "=== 环境检查 ==="
echo "Python 版本: $(python --version)"
echo "Pip 版本: $(pip --version)"
echo "虚拟环境: $VIRTUAL_ENV"
echo "当前目录: $(pwd)"
echo "Python 路径: $(which python)"
echo "Pip 路径: $(which pip)"
echo "================"
```

## 9. 最佳实践总结

1. **始终使用虚拟环境**
2. **每个项目独立的虚拟环境**
3. **使用 requirements.txt 管理依赖**
4. **分离生产和开发依赖**
5. **定期更新依赖版本**
6. **使用代码格式化和检查工具**
7. **编写测试并维护测试覆盖率**
8. **使用版本控制忽略虚拟环境目录**
9. **文档化依赖和安装步骤**
10. **自动化部署流程**

## 10. 进阶工具

### Poetry (现代依赖管理)
```bash
# 安装
pip install poetry

# 初始化项目
poetry new my-project
cd my-project

# 添加依赖
poetry add flask
poetry add --dev pytest

# 进入虚拟环境
poetry shell

# 运行应用
poetry run python app.py
```

### Pipenv (pip + virtualenv)
```bash
# 安装
pip install pipenv

# 创建虚拟环境并安装依赖
pipenv install flask
pipenv install --dev pytest

# 进入虚拟环境
pipenv shell

# 运行应用
pipenv run python app.py
```

### Conda (科学计算)
```bash
# 创建环境
conda create --name myenv python=3.9

# 激活环境
conda activate myenv

# 安装包
conda install numpy pandas

# 退出环境
conda deactivate
```

## 联系与支持

如果在使用过程中遇到问题，请：

1. 检查虚拟环境是否正确激活
2. 确认依赖版本是否兼容
3. 查看错误日志获取详细信息
4. 参考官方文档
5. 在社区寻求帮助

记住：良好的依赖管理是 Python 项目成功的关键！