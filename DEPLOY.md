# 🚀 部署上线指南

**5 分钟完成部署，立即拥有个人网站**

---

## 方式一：GitHub Pages（推荐）⭐⭐⭐⭐⭐

### 前置条件

- 有 GitHub 账号（没有的话访问 https://github.com/signup 注册）
- 已安装 GitHub Desktop 或使用网页上传

### 步骤 1：创建 GitHub 仓库

```
1. 访问：https://github.com/new
2. 仓库名称：portfolio-chunmiao
3. 可见性：公开（Public）
4. 点击 "Create repository"
```

### 步骤 2：上传文件

**方法 A：网页上传（最简单）**

```
1. 进入刚创建的仓库
2. 点击 "uploading an existing file"
3. 打开文件夹：C:\Users\Yoomeng\.openclaw\workspace\projects\portfolio-chunmiao
4. 拖入这 5 个文件：
   - index.html
   - styles.css
   - DESIGN.md
   - README.md
   - videos.md
5. 填写 commit message："Initial commit - Chunmiao portfolio"
6. 点击 "Commit changes"
```

**方法 B：使用 GitHub Desktop**

```
1. 下载 GitHub Desktop: https://desktop.github.com/
2. 安装并登录 GitHub 账号
3. File → Add Local Repository → 选择 portfolio-chunmiao 文件夹
4. 填写 commit message
5. 点击 "Commit to main"
6. 点击 "Publish repository"
```

### 步骤 3：启用 GitHub Pages

```
1. 进入仓库 → Settings → Pages（左侧菜单）
2. Source: 选择 "Deploy from a branch"
3. Branch: 选择 "main"
4. Folder: 选择 "/ (root)"
5. 点击 "Save"
6. 等待 1-2 分钟（页面刷新几次）
7. 看到绿色提示："Your site is live at..."
```

### 步骤 4：访问网站

```
格式：https://你的用户名.github.io/portfolio-chunmiao

例如：https://yoomeng.github.io/portfolio-chunmiao
```

---

## 方式二：Vercel 部署（备选）

### 优点
- 更快的全球 CDN
- 自动 HTTPS
- 支持自定义域名免费

### 步骤

```
1. 访问：https://vercel.com
2. 用 GitHub 账号登录
3. Import Project → 选择 portfolio-chunmiao 仓库
4. 点击 "Deploy"
5. 等待 30 秒
6. 获得链接：https://portfolio-chunmiao.vercel.app
```

---

## 方式三：Netlify 部署（备选）

### 步骤

```
1. 访问：https://www.netlify.com
2. 用 GitHub 账号登录
3. "Add new site" → "Import an existing project"
4. 选择 portfolio-chunmiao 仓库
5. 点击 "Deploy site"
6. 获得链接：https://xxx-xxx-xxx.netlify.app
```

---

## 绑定自定义域名（可选）

### 如果您有自己的域名（如 chunmiao.com）

**GitHub Pages 绑定步骤：**

```
1. 进入仓库 → Settings → Pages
2. Custom domain: 输入您的域名
3. 点击 "Save"
4. 到您的域名服务商处添加 DNS 记录：
   - 类型：CNAME
   - 主机：www
   - 值：你的用户名.github.io
5. 等待 DNS 生效（最多 24 小时，通常几分钟）
```

---

## 验证部署

### 检查清单

- [ ] 网站可以正常访问
- [ ] 所有视频卡片显示正常
- [ ] 手机打开也正常（响应式）
- [ ] 联系邮箱可以点击
- [ ] 导航栏滚动效果正常

### 测试链接

部署完成后，在以下设备测试：
- ✅ 电脑浏览器（Chrome/Safari/Edge）
- ✅ 手机浏览器
- ✅ 平板（如果有）

---

## 常见问题

### Q1: 部署后页面是空白？

**A**: 
- 等待 1-2 分钟，GitHub Pages 需要构建时间
- 刷新页面（Ctrl+F5 强制刷新）
- 检查控制台是否有错误（F12）

### Q2: 样式没加载？

**A**:
- 确认 `styles.css` 文件已上传
- 检查路径是否正确（应该在同一目录）
- 清除浏览器缓存

### Q3: 我想修改内容怎么办？

**A**:
1. 本地修改文件
2. 重新上传到 GitHub（或 git push）
3. 等待 1-2 分钟自动更新

### Q4: 可以删除重建吗？

**A**: 可以！随时删除仓库重新创建。

---

## 部署完成后

### 下一步

1. ✅ 把网站链接发给小喵确认
2. ✅ 开始准备您的真实视频内容
3. ✅ 按 `videos.md` 指南添加作品
4. ✅ 分享给客户/朋友/招聘方

### 分享话术

```
"这是我的个人作品集网站，展示了我在品牌宣传片、
三维动画和 MG 动画方面的作品。欢迎查看！"
```

---

## 需要帮助？

**随时联系小喵** 🐱

- 部署遇到问题
- 不会用 GitHub
- 需要添加视频
- 想要修改样式

---

**最后更新**: 2026-04-12  
**预计部署时间**: 5-10 分钟
