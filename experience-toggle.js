// 折叠展开功能（Apple 风格优化 v3 - 标题优雅淡入）
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
    
    // 移除标题 visible
    const titles = content.querySelectorAll('h4');
    titles.forEach(title => title.classList.remove('visible'));
    
    // 等内容隐藏后再收缩高度
    setTimeout(() => {
      content.classList.remove('expanded');
    }, 300);
  } else {
    // 展开：Apple 风格的渐进式动画
    button.classList.add('active');
    content.classList.add('expanded');
    
    // Apple 式动画：高度展开过程中，标题和内容依次优雅淡入
    animateDetailSectionsAppleStyleV3(content);
  }
}

// Apple 风格的逐行动画 v3（标题 + 内容依次优雅淡入）
function animateDetailSectionsAppleStyleV3(container) {
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
  
  // Apple 式动画流程：
  // 1. 高度开始展开
  // 2. 展开到 30% 时，标题淡入
  // 3. 标题出现后 200ms，第一行内容淡入
  // 4. 内容逐行淡入（每行 150ms）
  
  let titleShown = false;
  let contentStarted = false;
  let startTime = null;
  
  function animateExpand(timestamp) {
    if (!startTime) startTime = timestamp;
    const progress = (timestamp - startTime) / 800; // 800ms 总展开时间
    
    // 展开到 30% 时，标题淡入
    if (!titleShown && progress >= 0.3) {
      titleShown = true;
      projectDetails.forEach(details => {
        const h4 = details.querySelector('h4');
        if (h4) {
          // 强制重排后添加 visible
          void h4.offsetWidth;
          h4.classList.add('visible');
        }
      });
    }
    
    // 标题出现后 200ms，开始内容淡入
    if (titleShown && !contentStarted) {
      contentStarted = true;
      setTimeout(() => {
        startFadeInAnimationV3(projectDetails);
      }, 200);
    }
    
    // 继续动画直到完成
    if (progress < 1) {
      requestAnimationFrame(animateExpand);
    }
  }
  
  requestAnimationFrame(animateExpand);
}

// 逐行淡入动画 v3（标题先行，内容随后）
function startFadeInAnimationV3(projectDetailsList) {
  projectDetailsList.forEach((details, detailsIndex) => {
    const sections = details.querySelectorAll('.detail-section');
    
    sections.forEach((section, index) => {
      // 强制重排
      void section.offsetWidth;
      
      // 逐行淡入
      setTimeout(() => {
        section.classList.add('visible');
      }, index * 150); // 每行间隔 150ms
    });
  });
}

// 页面加载后初始化
document.addEventListener('DOMContentLoaded', function() {
  console.log('工作经历折叠功能已加载 - Apple 风格 v3');
});
