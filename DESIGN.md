# Design System: Chunmiao Portfolio

**Designer:** Chunmiao (Chen Chunmiao)  
**Style:** Apple-inspired Minimalism  
**Version:** 1.0  
**Created:** 2026-04-12

---

## 1. Visual Theme & Atmosphere

**整体氛围**：纯净、专业、电影感

- **风格定位**：Apple 经典白色极简主义
- **视觉密度**：疏朗通透，大量留白让内容呼吸
- **情绪基调**：专业可信、优雅克制、作品导向
- **设计哲学**：Less is More，让视频作品成为绝对主角

---

## 2. Color Palette & Roles

### 主色调

| 颜色 | 色值 | 用途 |
|------|------|------|
| **纯净白** | `#FFFFFF` | 主背景色 |
| **浅灰白** | `#F5F5F7` | 次要背景、卡片底色 |
| **中灰色** | `#86868B` | 辅助文字、边框 |
| **深空灰** | `#1D1D1F` | 主标题、正文 |
| **纯黑色** | `#000000` | 强调文字、链接 hover |

### 强调色

| 颜色 | 色值 | 用途 |
|------|------|------|
| **Apple 蓝** | `#0066CC` | 链接、CTA 按钮 |
| **播放按钮红** | `#FF0000` | 视频播放图标 |

---

## 3. Typography Rules

### 字体家族

```
主字体：-apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif
代码字体："SF Mono", "Monaco", "Consolas", "Courier New", monospace
```

### 字号阶梯

| 用途 | 字号 | 字重 | 行高 | 字间距 |
|------|------|------|------|--------|
| **大标题 (Hero)** | 48px | 600 (Semi-bold) | 1.1 | -0.02em |
| **章节标题** | 40px | 600 (Semi-bold) | 1.2 | -0.015em |
| **小标题** | 24px | 600 (Semi-bold) | 1.3 | -0.01em |
| **正文大** | 17px | 400 (Regular) | 1.5 | 0 |
| **正文** | 15px | 400 (Regular) | 1.5 | 0 |
| **辅助文字** | 13px | 400 (Regular) | 1.4 | 0 |
| **页脚** | 12px | 400 (Regular) | 1.4 | 0 |

### 字重使用规则

- **标题**：600 (Semi-bold) — 清晰醒目
- **正文**：400 (Regular) — 舒适阅读
- **强调**：600 (Semi-bold) — 局部加粗

---

## 4. Component Stylings

### 导航栏

- **背景**：`#FFFFFF`，95% 不透明度（滚动时模糊半透明）
- **高度**：48px
- **Logo**：17px，600 字重，`#1D1D1F`
- **链接**：13px，400 字重，`#1D1D1F`，hover 变`#0066CC`

### Hero 区域

- **布局**：垂直居中，内容水平居中
- **标题**：48px，600 字重，`#1D1D1F`
- **副标题**：24px，400 字重，`#86868B`
- **留白**：上下各 120px

### 视频卡片

- **圆角**：18px（大圆角，Apple 风格）
- **背景**：`#FFFFFF`
- **阴影**：`0 4px 24px rgba(0,0,0,0.08)`（柔和悬浮感）
- **悬停效果**：阴影加深至 `0 8px 32px rgba(0,0,0,0.12)`，轻微上移 2px
- **封面图比例**：16:9
- **卡片间距**：40px（桌面端）

### 视频信息区

- **标题**：17px，600 字重，`#1D1D1F`
- **简介**：15px，400 字重，`#86868B`，最多 3 行
- **你的贡献标签**：12px，400 字重，`#F5F5F7` 背景，`#1D1D1F` 文字，圆角 6px
- **播放按钮**：48px × 48px 圆形，红色 `#FF0000`，白色播放图标

### 板块标题

- **字体**：40px，600 字重，`#1D1D1F`
- **下边距**：60px
- **左侧对齐**：与视频卡片左边缘对齐

### 页脚

- **背景**：`#F5F5F7`
- **文字**：12px，400 字重，`#86868B`
- **居中**：水平居中
- **内边距**：48px 24px

---

## 5. Layout Principles

### 网格系统

- **最大宽度**：1200px（内容区域）
- **左右边距**：24px（移动端），48px（桌面端）
- **列数**：1 列（移动），2 列（平板），3 列（桌面）
- **水槽宽度**：40px

### 响应式断点

```css
/* 移动端 */
@media (max-width: 767px) {
  --grid-columns: 1;
  --card-gap: 24px;
}

/* 平板端 */
@media (min-width: 768px) and (max-width: 1023px) {
  --grid-columns: 2;
  --card-gap: 32px;
}

/* 桌面端 */
@media (min-width: 1024px) {
  --grid-columns: 3;
  --card-gap: 40px;
}
```

### 留白规则

- **区块间距**：120px（桌面），80px（移动）
- **卡片内边距**：24px
- **元素间距**：使用 4/8/12/16/24/32/48/64/80/120px（4 的倍数）

### 动效原则

- **持续时间**：200ms - 300ms
- **缓动函数**：`cubic-bezier(0.4, 0, 0.2, 1)`（Apple 风格）
- **触发**：hover、scroll、fade-in
- **原则**：微妙、流畅、不抢戏

---

## 6. Video Embed Guidelines

### B 站嵌入代码规范

```html
<iframe 
  src="//player.bilibili.com/player.html?bvid=BVxxxxx&page=1" 
  scrolling="no" 
  border="0" 
  frameborder="no" 
  framespacing="0" 
  allowfullscreen="true"
  style="width: 100%; aspect-ratio: 16/9; border-radius: 12px;">
</iframe>
```

### 视频卡片数据结构

```markdown
- 视频标题：《xxx》
- B 站链接：https://b23.tv/BVxxxxx 或 https://www.bilibili.com/video/BVxxxxx
- 封面图：可选（小喵自动截图）
- 简介：1-3 句话，说明视频内容
- 你的贡献：策划/拍摄/剪辑/动画/特效等
- 分类：品牌宣传片 / 三维产品动画 / MG 动画
```

---

## 7. Content Sections

### 网站结构

```
1. Hero Section（首页大标题）
   - 标题：Chunmiao | 多媒体设计师
   - 副标题：专注品牌视频宣传创作者

2. 品牌宣传片（6 条）
   - 板块标题
   - 3 列网格展示

3. 三维产品动画（3 条）
   - 板块标题
   - 3 列网格展示

4. MG 动画（3 条）
   - 板块标题
   - 3 列网格展示

5. Contact（联系方式）
   - 邮箱：chenchunmiao@foxmail.com
   - 可选：微信/B 站主页/GitHub

6. Footer（页脚）
   - © 2026 Chunmiao. All rights reserved.
```

---

## Usage Instructions

将此 DESIGN.md 放入项目根目录，AI 助手读取后生成的 UI 应符合以上所有规范。

**核心原则**：
1. 留白 > 填充
2. 内容 > 装饰
3. 一致 > 变化
4. 克制 > 张扬

**让作品说话，设计退后一步。**
