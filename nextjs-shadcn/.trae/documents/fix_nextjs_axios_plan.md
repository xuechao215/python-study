# 修复 Next.js 运行问题并集成 Axios 计划

## 1. 修复环境配置问题

用户反馈 Next.js 运行失败，经排查主要原因为：

* `package.json` 设置了 `"type": "module"`，导致 `.js` 配置文件被视为 ESM，而 `postcss.config.js`使用了 CommonJS 语法。

* Google Fonts (`Inter`) 下载超时导致网络错误。

* `tailwind.config.ts` 使用了 `require` 语法，建议改为 `import` 以符合 ESM 规范。

### 步骤

* [ ] 修改 `postcss.config.js` 为 ESM 语法 (`export default`)。

* [ ] 修改 `tailwind.config.ts`，将 `require('tailwindcss-animate')` 改为 `import` 导入。

* [ ] 修改 `src/app/layout.tsx`，移除 Google Fonts 引用，避免网络超时。

## 2. 集成 Axios

用户请求使用 axios 替代 fetch 进行网络请求。

### 步骤

* [ ] 安装 `axios` 依赖。

* [ ] 创建 `src/lib/request.ts` 封装 axios 实例（设置 baseURL, 超时时间, 拦截器）。

* [ ] 修改 `src/app/page.tsx`，添加一个使用封装后的 axios 获取数据的示例（例如获取 JSONPlaceholder 的数据）。

## 3. 验证

* [ ] 重新启动开发服务器 `npm run dev`。

* [ ] 验证页面加载是否正常，无控制台报错。

* [ ] 验证 axios 请求是否成功。

