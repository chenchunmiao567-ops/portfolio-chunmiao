# Apple 官网动效设计分析报告

**版本**: v1.0  
**日期**: 2026-04-14  
**作者**: 前端 Agent  
**审阅**: 小喵

---

## 一、Apple 官网动效分析

### 1.1 滚动触发动画特点

访问 https://www.apple.com.cn/iphone/ 观察到的动效特征：

| 特性 | Apple 官网表现 | 技术实现 |
|------|---------------|---------|
| **触发时机** | 元素进入视口 100-200px 时触发 | IntersectionObserver + rootMargin |
| **动画方向** | 从下方 30-50px 上浮到原位 | transform: translateY() |
| **透明度** | 从 0 淡入到 1 | opacity: 0 → 1 |
| **缓动曲线** | 先快后慢，优雅减速 | cubic-bezier(0.16, 1, 0.3, 1) |
| **动画时长** | 600-1000ms | transition-duration |
| **延迟策略** | 多个元素错开 100-200ms | stagger animation |
| **一次性** | 只播放一次，不重复 | once: true |

### 1.2 Apple 风格缓动曲线

```css
/* Apple 官方缓动曲线 */
apple-ease: cubic-bezier(0.16, 1, 0.3, 1);

/* 特点 */
- 起始速度快 (0.16)
- 中间平滑过渡 (1)
- 结束缓慢停止 (0.3, 1)
- 类似物理世界的"减速带"效果
```

### 1.3 典型动效场景

**场景 1：标题进入**
```
初始状态：opacity: 0, translateY(40px)
触发后：opacity: 1, translateY(0)
时长：800ms
缓动：cubic-bezier(0.16, 1, 0.3, 1)
```

**场景 2：卡片上浮**
```
初始状态：opacity: 0, translateY(60px), scale(0.95)
触发后：opacity: 1, translateY(0), scale(1)
时长：1000ms
延迟：200ms
```

**场景 3：文字淡入**
```
初始状态：opacity: 0
触发后：opacity: 1
时长：600ms
延迟：400ms
```

---

## 二、当前网站问题分析

### 2.1 问题诊断

**问题 1：元素初始状态不可见**
```css
/* 当前代码 */
.section-title {
  opacity: 0;  /* ❌ 问题：如果 JS 未执行，永远不可见 */
  transform: translateY(30px);
}
```

**问题 2：Observer 监听逻辑错误**
```javascript
// 当前代码
observer.observe(title);  // ❌ 监听的是 title 元素本身
// 但 title 一开始 opacity:0，可能无法触发 intersect
```

**问题 3：缺少降级方案**
```css
/* 如果没有 JS，.visible 类永远不会添加 */
/* 元素将永远保持 opacity:0 */
```

### 2.2 根本原因

1. **循环依赖问题**：
   - 元素初始 `opacity: 0`（不可见）
   - Observer 需要元素可见才能触发
   - 但元素不可见，Observer 不触发
   - `.visible` 类不添加
   - 元素永远不可见

2. **监听目标错误**：
   - 应该监听 `.section` 板块，而不是 `.section-title`
   - 板块总是可见的，能正确触发

3. **缺少无 JS 降级**：
   - 如果 JS 加载失败/禁用，文字完全不可见

---

## 三、修复方案

### 3.1 核心修复思路

**原则：渐进增强（Progressive Enhancement）**

```
1. 默认状态：文字可见（无 JS 时也能看）
2. JS 加载后：添加"动画准备"类
3. 滚动触发：添加"动画完成"类
```

### 3.2 CSS 修复

```css
/* 步骤 1：默认状态 - 文字可见（降级方案） */
.section-title {
  font-size: 32px;
  font-weight: 700;
  color: #1d1d1f;
  /* 不设置 opacity 和 transform */
}

/* 步骤 2：JS 加载后 - 准备动画 */
.section-title.ready {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

/* 步骤 3：滚动触发 - 动画完成 */
.section-title.ready.visible {
  opacity: 1;
  transform: translateY(0);
}

/* 副标题同样逻辑 */
.section-subtitle.ready {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.2s,
              transform 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.2s;
}

.section-subtitle.ready.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### 3.3 JavaScript 修复

```javascript
// Apple 风格滚动动画 - 修复版
document.addEventListener('DOMContentLoaded', () => {
  // 步骤 1：给所有目标元素添加"ready"类
  const titles = document.querySelectorAll('.section-title, .section-subtitle');
  titles.forEach(title => {
    title.classList.add('ready');
  });

  // 步骤 2：创建 Observer（监听板块，不是标题）
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -150px 0px', // 元素进入视口 150px 时触发
    threshold: 0.01 // 1% 可见就触发
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // 找到板块内的所有标题
        const section = entry.target;
        const titles = section.querySelectorAll('.section-title, .section-subtitle');
        
        // 错开添加 visible 类
        titles.forEach((title, index) => {
          setTimeout(() => {
            title.classList.add('visible');
          }, index * 150); // 每个元素延迟 150ms
        });

        // 步骤 3：动画完成后停止监听（一次性）
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // 步骤 4：监听所有板块
  document.querySelectorAll('.section').forEach(section => {
    observer.observe(section);
  });

  console.log('✅ Apple 风格滚动动画初始化完成');
});
```

### 3.4 关键改进点

| 改进项 | 修复前 | 修复后 |
|--------|--------|--------|
| **初始状态** | opacity: 0（不可见） | 默认可见，JS 添加 ready 后隐藏 |
| **监听目标** | .section-title（可能不可见） | .section（总是可见） |
| **触发条件** | threshold: 0.1 | threshold: 0.01 + rootMargin: -150px |
| **一次性** | 无 | observer.unobserve() |
| **降级方案** | 无 JS 时文字消失 | 无 JS 时文字正常显示 |
| **延迟策略** | 固定 0.2s | 每个元素 150ms 递增 |

---

## 四、完整代码示例

### 4.1 CSS（styles.css）

```css
/* Apple 风格标题和文字动画 */

/* 默认状态 - 无 JS 时可见 */
.section-title {
  font-size: 32px;
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: #1d1d1f;
  margin-bottom: var(--spacing-4xl);
}

/* JS 加载后 - 准备动画 */
.section-title.ready {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

/* 滚动触发 - 动画完成 */
.section-title.ready.visible {
  opacity: 1;
  transform: translateY(0);
}

@media (min-width: 768px) {
  .section-title {
    font-size: 48px;
    margin-bottom: var(--spacing-5xl);
  }
}

/* 副标题同样逻辑 */
.section-subtitle {
  font-size: 17px;
  font-weight: 400;
  color: #86868b;
  margin-top: -20px;
  margin-bottom: var(--spacing-4xl);
}

.section-subtitle.ready {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.2s,
              transform 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.2s;
}

.section-subtitle.ready.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### 4.2 JavaScript（index.html）

```javascript
document.addEventListener('DOMContentLoaded', () => {
  // 1. 给所有目标元素添加"ready"类
  const titles = document.querySelectorAll('.section-title, .section-subtitle');
  titles.forEach(title => {
    title.classList.add('ready');
  });

  // 2. 创建 Observer
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -150px 0px',
    threshold: 0.01
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const section = entry.target;
        const titles = section.querySelectorAll('.section-title, .section-subtitle');
        
        titles.forEach((title, index) => {
          setTimeout(() => {
            title.classList.add('visible');
          }, index * 150);
        });

        // 3. 动画完成后停止监听
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // 4. 监听所有板块
  document.querySelectorAll('.section').forEach(section => {
    observer.observe(section);
  });

  console.log('✅ Apple 风格滚动动画初始化完成');
});
```

---

## 五、测试验证

### 5.1 测试场景

| 场景 | 预期行为 | 测试方法 |
|------|---------|---------|
| **正常滚动** | 文字缓动上浮 | 向下滚动页面 |
| **快速滚动** | 所有元素依次触发 | 快速滚到底部 |
| **无 JS** | 文字正常显示 | 禁用 JS 刷新 |
| **移动端** | 触摸滚动同样触发 | 手机测试 |
| **重复滚动** | 只触发一次 | 上下滚动多次 |

### 5.2 性能指标

| 指标 | 目标值 | 测量方法 |
|------|--------|---------|
| **首屏加载** | < 1s | Lighthouse |
| **动画帧率** | 60fps | Chrome DevTools |
| **Observer 数量** | = 板块数量 | console.log |
| **内存占用** | < 50MB | Chrome Task Manager |

---

## 六、总结

### 6.1 核心问题

- ❌ 元素初始 `opacity: 0` 导致 Observer 无法触发
- ❌ 监听目标错误（监听标题而不是板块）
- ❌ 缺少无 JS 降级方案

### 6.2 解决方案

- ✅ 渐进增强：默认可见 → JS 准备 → 滚动触发
- ✅ 正确监听：监听 `.section` 板块
- ✅ 一次性动画：`observer.unobserve()`
- ✅ 降级方案：无 JS 时文字正常显示

### 6.3 Apple 风格要点

1. **缓动曲线**：`cubic-bezier(0.16, 1, 0.3, 1)`
2. **动画时长**：600-1000ms
3. **触发时机**：进入视口 150px 时
4. **延迟策略**：元素错开 150ms
5. **运动方向**：从下方 40px 上浮

---

**报告完成时间**: 2026-04-14 03:45  
**审阅状态**: 待小喵审阅  
**执行状态**: 待执行
