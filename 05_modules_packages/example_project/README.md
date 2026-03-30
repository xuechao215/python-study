# Python 虚拟环境示例项目

这个示例项目展示了如何使用虚拟环境和 pip 管理 Python 依赖。

## 项目结构
```
example_project/
├── .gitignore          # 忽略虚拟环境和缓存文件
├── README.md           # 项目说明
├── requirements.txt    # 生产依赖
├── requirements-dev.txt # 开发依赖
├── src/               # 源代码目录
│   └── app.py         # 主应用文件
└── tests/             # 测试目录
    └── test_app.py    # 测试文件
```

## 快速开始

### 1. 创建虚拟环境
```bash
python -m venv venv
```

### 2. 激活虚拟环境
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. 安装依赖
```bash
# 安装生产依赖
pip install -r requirements.txt

# 安装开发依赖
pip install -r requirements-dev.txt
```

### 4. 运行应用
```bash
python src/app.py
```

### 5. 运行测试
```bash
pytest tests/
```

## 依赖管理

### 导出当前依赖
```bash
# 导出生产依赖
pip freeze > requirements.txt

# 导出开发依赖
pip freeze --local | grep -E "(pytest|black|flake8)" > requirements-dev.txt
```

### 更新依赖
```bash
# 更新所有包
pip install --upgrade -r requirements.txt

# 更新特定包
pip install --upgrade package_name
```

## 常用命令

### 虚拟环境管理
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 退出虚拟环境
deactivate

# 检查是否在虚拟环境中
which python  # 应该显示 venv/bin/python
```

### 包管理
```bash
# 安装包
pip install package_name

# 安装特定版本
pip install package_name==1.2.3

# 卸载包
pip uninstall package_name

# 列出已安装包
pip list

# 查看包信息
pip show package_name
```

### 开发工具
```bash
# 代码格式化
black src/ tests/

# 代码检查
flake8 src/ tests/

# 运行测试
pytest tests/

# 测试覆盖率
pytest --cov=src tests/
```

## 最佳实践

1. **每个项目使用独立的虚拟环境**
2. **将 `venv/` 添加到 `.gitignore`**
3. **使用 `requirements.txt` 管理依赖版本**
4. **分离生产和开发依赖**
5. **定期更新依赖版本**
6. **在 CI/CD 中自动化测试和代码检查**

## 故障排除

### 常见问题
1. **权限错误**: 不要使用 `sudo pip install`，使用虚拟环境
2. **版本冲突**: 确保虚拟环境激活，检查 `requirements.txt`
3. **下载慢**: 使用国内镜像源
   ```bash
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name
   ```

### 环境检查
```bash
# 检查 Python 版本
python --version

# 检查 pip 版本
pip --version

# 检查虚拟环境
echo $VIRTUAL_ENV  # macOS/Linux
echo %VIRTUAL_ENV% # Windows
```