// 折叠展开功能（Apple 风格优化 v2）
function toggleDetails(button) {
  const content = button.nextElementSibling;
  const isExpanded = content.classList.contains('expanded');
  
  // 更新按钮文字
  const textSpan = button.querySelector('.btn-text');
  if (textSpan) {
    textSpan.textContent = '项目详情';
  }
  
  if (isExpanded) {
    // 收起：先隐藏内容，再收缩高度
    button.classList.remove('active');
    
    // 先移除 visible 类（淡出效果）
    const sections = content.querySelectorAll('.detail-section');
    sections.forEach((section, index) => {
      setTimeout(() => {
        section.classList.remove('visible');
      }, index * 50); // 快速收起
    });
    
    // 等内容隐藏后再收缩高度
    setTimeout(() => {
      content.classList.remove('expanded');
    }, 300);
  } else {
    // 展开：Apple 风格的渐进式动画
    button.classList.add('active');
    content.classList.add('expanded');
    
    // Apple 式动画：高度展开过程中，内容逐行优雅淡入
    animateDetailSectionsAppleStyleV2(content);
  }
}

// Apple 风格的逐行动画 v2（更流畅优雅）
function animateDetailSectionsAppleStyleV2(container) {
  const sections = container.querySelectorAll('.detail-section');
  
  // 重置所有 section 的状态
  sections.forEach(section => {
    section.classList.remove('visible');
  });
  
  // 强制浏览器重排
  void container.offsetWidth;
  
  // Apple 设计原则：
  // 1. 高度展开到 40% 时开始第一行淡入
  // 2. 每行间隔 150ms（更从容的节奏）
  // 3. 使用更柔和的缓动曲线
  
  let animationStarted = false;
  let startTime = null;
  const startThreshold = 0.4; // 40% 高度时开始
  
  function animateExpand(timestamp) {
    if (!startTime) startTime = timestamp;
    const progress = (timestamp - startTime) / 800; // 800ms 总展开时间
    
    // 当展开到 40% 时开始淡入
    if (!animationStarted && progress >= startThreshold) {
      animationStarted = true;
      startFadeInAnimation(sections);
    }
    
    // 继续动画直到完成
    if (progress < 1) {
      requestAnimationFrame(animateExpand);
    }
  }
  
  requestAnimationFrame(animateExpand);
}

// 逐行淡入动画（更优雅的节奏）
function startFadeInAnimation(sections) {
  sections.forEach((section, index) => {
    setTimeout(() => {
      section.classList.add('visible');
    }, index * 150); // 每行间隔 150ms，更从容
  });
}

// 页面加载后初始化
document.addEventListener('DOMContentLoaded', function() {
  console.log('工作经历折叠功能已加载 - Apple 风格 v2');
});
