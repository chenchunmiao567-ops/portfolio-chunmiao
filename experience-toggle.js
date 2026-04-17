// 折叠展开功能（Apple 风格优化）
function toggleDetails(button) {
  const content = button.nextElementSibling;
  const isExpanded = content.classList.contains('expanded');
  
  // 更新按钮文字
  const textSpan = button.querySelector('.btn-text');
  if (textSpan) {
    textSpan.textContent = '项目详情';
  }
  
  if (isExpanded) {
    // 收起
    button.classList.remove('active');
    content.classList.remove('expanded');
    
    // 移除 visible 类，准备下次动画
    setTimeout(() => {
      const sections = content.querySelectorAll('.detail-section');
      sections.forEach(section => section.classList.remove('visible'));
    }, 300);
  } else {
    // 展开：Apple 风格
    button.classList.add('active');
    content.classList.add('expanded');
    
    // Apple 式动画：高度展开后，内容逐行淡入
    animateDetailSectionsAppleStyle(content);
  }
}

// Apple 风格的逐行动画
function animateDetailSectionsAppleStyle(container) {
  const sections = container.querySelectorAll('.detail-section');
  
  // 重置所有 section 的状态
  sections.forEach(section => {
    section.classList.remove('visible');
  });
  
  // 强制浏览器重排
  void container.offsetWidth;
  
  // 延迟一点点，等高度展开后再淡入内容
  setTimeout(() => {
    sections.forEach((section, index) => {
      setTimeout(() => {
        section.classList.add('visible');
      }, index * 100); // 每行间隔 100ms
    });
  }, 150); // 等 150ms 让高度开始展开
}

// 页面加载后初始化
document.addEventListener('DOMContentLoaded', function() {
  console.log('工作经历折叠功能已加载');
});
