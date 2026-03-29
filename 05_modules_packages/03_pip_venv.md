# 03_pip_venv.md
# 包管理与虚拟环境 (Pip & Virtual Environments)
# 类似于 JS 的 npm/yarn 和 node_modules 的概念

## 1. 包管理器 (Pip)
# Pip 是 Python 的包安装程序 (Package Installer for Python)
# 类似于 Node.js 的 npm

### 常用命令
- **安装包**: `pip install package_name`
  - 类似于 `npm install package_name`
- **卸载包**: `pip uninstall package_name`
  - 类似于 `npm uninstall package_name`
- **列出已安装包**: `pip list`
  - 类似于 `npm list`
- **导出依赖**: `pip freeze > requirements.txt`
  - 类似于 `package.json` 中的 dependencies，但这只是一个快照
- **安装所有依赖**: `pip install -r requirements.txt`
  - 类似于 `npm install` (基于 package.json)

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
```

### 激活虚拟环境
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 退出虚拟环境
```bash
deactivate
```

### 为什么要使用虚拟环境?
- **隔离依赖**: 每个项目拥有独立的库版本，互不干扰
- **避免权限问题**: 不需要管理员权限即可安装包
- **保持系统清洁**: 不会污染全局 Python 环境

## 3. 最佳实践
1.  每个项目都创建一个虚拟环境
2.  在 `.gitignore` 中忽略 `venv/` 目录 (就像忽略 `node_modules/` 一样)
3.  使用 `requirements.txt` 管理依赖版本
4.  也可以使用更高级的工具如 `poetry` 或 `pipenv` (类似于 `yarn` 或 `pnpm`，提供更好的锁文件机制 `Pipfile.lock` / `poetry.lock`)
