// 折叠展开功能（Apple 官方风格 - 完全展开后淡入）
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
    const projectDetails = content.querySelectorAll('.project-details');
    const titles = content.querySelectorAll('h4');
    const sections = content.querySelectorAll('.detail-section');
    
    // 先淡出文本框
    projectDetails.forEach((details, index) => {
      setTimeout(() => {
        details.classList.remove('visible');
      }, index * 50);
    });
    
    // 再淡出标题和内容
    titles.forEach(title => title.classList.remove('visible'));
    sections.forEach((section, index) => {
      setTimeout(() => {
        section.classList.remove('visible');
      }, index * 50);
    });
    
    // 等淡出完成后再收缩高度
    setTimeout(() => {
      content.classList.remove('expanded');
    }, 500);
  } else {
    // 展开：Apple 官方风格 - 完全展开后停顿，然后整体淡入
    button.classList.add('active');
    content.classList.add('expanded');
    
    // Apple 官方动画流程：
    // 1. 高度完全展开（800ms）
    // 2. 停顿 150ms（让眼睛适应）
    // 3. 所有内容同时淡入（标题 + 内容，间隔 80ms）
    animateDetailSectionsAppleOfficial(content);
  }
}

// Apple 官方风格的淡入动画
function animateDetailSectionsAppleOfficial(container) {
  const projectDetails = container.querySelectorAll('.project-details');
  
  // 重置所有状态
  projectDetails.forEach(details => {
    // 文本框先淡入
    details.classList.remove('visible');
    
    const h4 = details.querySelector('h4');
    const sections = details.querySelectorAll('.detail-section');
    
    if (h4) h4.classList.remove('visible');
    sections.forEach(section => section.classList.remove('visible'));
  });
  
  // 强制浏览器重排
  void container.offsetWidth;
  
  // Apple 优化设计：
  // 完全展开后等待 300ms（200ms 展开 + 100ms 停顿）
  // 然后文本框 → 标题 → 内容 依次优雅淡入
  // 更快响应，不等待完全展开
  setTimeout(() => {
    startFadeInAppleOfficial(projectDetails);
  }, 300);
}

// Apple 官方淡入动画（文本框先行，标题 + 内容紧随）
function startFadeInAppleOfficial(projectDetailsList) {
  let globalIndex = 0;
  
  projectDetailsList.forEach((details) => {
    // 1. 文本框先淡入
    void details.offsetWidth; // 强制重排
    setTimeout(() => {
      details.classList.add('visible');
    }, globalIndex * 80);
    globalIndex++;
    
    // 2. 标题淡入
    const h4 = details.querySelector('h4');
    if (h4) {
      void h4.offsetWidth; // 强制重排
      setTimeout(() => {
        h4.classList.add('visible');
      }, globalIndex * 80);
      globalIndex++;
    }
    
    // 3. 内容紧随其后淡入（间隔 80ms）
    const sections = details.querySelectorAll('.detail-section');
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
  console.log('工作经历折叠功能已加载 - Apple 官方风格');
});
