// 折叠展开功能（Apple 风格 v4 - 完全展开后淡入）
function toggleDetails(button) {
  const content = button.nextElementSibling;
  const isExpanded = content.classList.contains('expanded');
  
  // 更新按钮文字
  const textSpan = button.querySelector('.btn-text');
  if (textSpan) {
    textSpan.textContent = '项目详情';
  }
  
  if (isExpanded) {
    // 收起：先淡出内容，再收缩高度
    button.classList.remove('active');
    
    // 淡出所有内容
    const titles = content.querySelectorAll('h4');
    const sections = content.querySelectorAll('.detail-section');
    
    titles.forEach(title => title.classList.remove('visible'));
    sections.forEach((section, index) => {
      setTimeout(() => {
        section.classList.remove('visible');
      }, index * 50);
    });
    
    // 等淡出完成后再收缩高度
    setTimeout(() => {
      content.classList.remove('expanded');
    }, 400);
  } else {
    // 展开：Apple 风格 - 完全展开后停顿，然后整体淡入
    button.classList.add('active');
    content.classList.add('expanded');
    
    // Apple 式动画：等高度完全展开后，停顿一下，然后所有内容优雅淡入
    animateDetailSectionsAppleStyleV4(content);
  }
}

// Apple 风格的逐行动画 v4（完全展开后淡入）
function animateDetailSectionsAppleStyleV4(container) {
  const projectDetails = container.querySelectorAll('.project-details');
  
  // 重置所有状态
  projectDetails.forEach(details => {
    const h4 = details.querySelector('h4');
    const sections = details.querySelectorAll('.detail-section');
    
    if (h4) h4.classList.remove('visible');
    sections.forEach(section => section.classList.remove('visible'));
  });
  
  // 强制浏览器重排
  void container.offsetWidth;
  
  // Apple 设计原则：
  // 1. 等待高度完全展开（800ms）
  // 2. 停顿 100ms（让眼睛适应）
  // 3. 所有内容同时开始淡入（标题 + 内容，间隔 50ms）
  // 4. 使用非常柔和的缓动曲线
  
  setTimeout(() => {
    // 开始淡入动画
    startFadeInAnimationV4(projectDetails);
  }, 900); // 800ms 展开 + 100ms 停顿
}

// 逐行淡入动画 v4（Apple 风格 - 同时淡入）
function startFadeInAnimationV4(projectDetailsList) {
  let globalIndex = 0;
  
  projectDetailsList.forEach((details) => {
    const h4 = details.querySelector('h4');
    const sections = details.querySelectorAll('.detail-section');
    
    // 标题先淡入
    if (h4) {
      void h4.offsetWidth; // 强制重排
      setTimeout(() => {
        h4.classList.add('visible');
      }, globalIndex * 80);
      globalIndex++;
    }
    
    // 内容紧随其后淡入（间隔很短）
    sections.forEach((section) => {
      void section.offsetWidth; // 强制重排
      setTimeout(() => {
        section.classList.add('visible');
      }, globalIndex * 80);
      globalIndex++;
    });
    
    // 每个项目之间留一点间隔
    globalIndex += 0.5;
  });
}

// 页面加载后初始化
document.addEventListener('DOMContentLoaded', function() {
  console.log('工作经历折叠功能已加载 - Apple 风格 v4');
});
