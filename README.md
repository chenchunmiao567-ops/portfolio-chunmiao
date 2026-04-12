# Chunmiao Portfolio - 个人作品集网站

Apple 风格极简设计，专注展示视频作品。

---

## 📁 文件结构

```
portfolio-chunmiao/
├── index.html          # 主页面
├── styles.css          # 样式文件
├── DESIGN.md           # 设计规范文档
├── README.md           # 本文件
└── videos.md           # 视频添加指南（待创建）
```

---

## 🚀 快速部署到 GitHub Pages

### 步骤 1：创建 GitHub 仓库

1. 访问 https://github.com/new
2. 仓库名：`portfolio-chunmiao`（或 `chenchunmiao.github.io`）
3. 可见性：**公开**（GitHub Pages 免费）
4. 点击 "Create repository"

### 步骤 2：上传文件

**方法 A：网页上传（推荐新手）**
```
1. 进入刚创建的仓库
2. 点击 "uploading an existing file"
3. 拖入这 4 个文件：index.html, styles.css, DESIGN.md, README.md
4. 填写 commit message："Initial commit"
5. 点击 "Commit changes"
```

**方法 B：Git 命令（如果会用）**
```bash
cd portfolio-chunmiao
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/portfolio-chunmiao.git
git push -u origin main
```

### 步骤 3：启用 GitHub Pages

```
1. 进入仓库 → Settings → Pages
2. Source: 选择 "Deploy from a branch"
3. Branch: 选择 "main" 或 "master"
4. Folder: 选择 "/ (root)"
5. 点击 "Save"
6. 等待 1-2 分钟
7. 访问：https://YOUR_USERNAME.github.io/portfolio-chunmiao
```

---

## 🎬 如何添加新视频

### 简单方式：联系小喵

1. 复制下方模板
2. 填写视频信息
3. 发送给小喵（飞书/微信）
4. 小喵帮您更新网站

### 模板

```markdown
## 新视频信息

**分类**：品牌宣传片 / 三维产品动画 / MG 动画

**视频标题**：《xxx》

**B 站链接**：https://b23.tv/BVxxxxx 或 https://www.bilibili.com/video/BVxxxxx

**简介**：1-3 句话，说明视频内容和你的贡献

**你的贡献标签**：策划 / 拍摄 / 剪辑 / 动画 / 特效 / 导演 / 后期 / 调色 / 建模 / 灯光 / 脚本 / 设计

**发布时间**：2026-xx-xx
```

### 小喵会自动帮您

- ✅ 提取 B 站视频封面
- ✅ 生成 HTML 卡片代码
- ✅ 更新到对应板块
- ✅ 推送到 GitHub

---

## 🎨 自定义内容

### 修改个人信息

打开 `index.html`，找到以下位置修改：

```html
<!-- Hero 区域 -->
<h1 class="hero-title">Chunmiao | 多媒体设计师</h1>
<p class="hero-subtitle">专注品牌视频宣传创作者</p>

<!-- 联系方式 -->
<a href="mailto:chenchunmiao@foxmail.com" class="contact-email">chenchunmiao@foxmail.com</a>
```

### 替换示例视频

打开 `index.html`，找到对应的视频卡片，修改：

```html
<h3 class="video-title">您的视频标题</h3>
<p class="video-desc">您的视频简介</p>
<div class="video-tags">
  <span class="tag">标签 1</span>
  <span class="tag">标签 2</span>
</div>
```

---

## 📱 响应式支持

网站已适配：
- ✅ 桌面端（1024px+）：3 列网格
- ✅ 平板端（768px-1023px）：2 列网格
- ✅ 移动端（<768px）：1 列网格

---

## 🎯 下一步

1. **部署上线**：按上方步骤部署到 GitHub Pages
2. **填充内容**：将 12 个示例视频替换为您的真实作品
3. **分享链接**：发送给客户/朋友/招聘方

---

## 💡 高级功能（可选）

如需以下功能，联系小喵：
- [ ] 自定义域名绑定（如 chunmiao.com）
- [ ] B 站视频自动嵌入（点击卡片直接播放）
- [ ] 视频封面图自动生成
- [ ] 访问统计（Google Analytics）
- [ ] 暗黑模式切换
- [ ] 多语言支持

---

## 📞 技术支持

有任何问题，随时联系小喵～ 🐱

---

**Design System**: Apple-inspired Minimalism  
**Created**: 2026-04-12  
**Version**: 1.0
