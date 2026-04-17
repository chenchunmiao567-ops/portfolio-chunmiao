// 折叠展开功能
function toggleDetails(button) {
  const content = button.nextElementSibling;
  const isExpanded = content.classList.contains('expanded');
  
  // 切换状态
  content.classList.toggle('expanded');
  button.classList.toggle('active');
  
  // 更新按钮文字（统一为"项目详情"）
  const textSpan = button.querySelector('.btn-text');
  if (textSpan) {
    if (isExpanded) {
      textSpan.textContent = '项目详情';
      button.classList.remove('active');
    } else {
      textSpan.textContent = '项目详情';
      button.classList.add('active');
    }
  }
  
  // 展开时：逐行显示内容
  if (!isExpanded) {
    animateDetailSections(content);
  }
}

// 逐行动画函数（与主页面一致的缓动上浮效果）
function animateDetailSections(container) {
  const sections = container.querySelectorAll('.detail-section');
  
  // 先重置所有section 的状态（确保动画可重复触发）
  sections.forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
  });
  
  // 逐行触发动画
  sections.forEach((section, index) => {
    setTimeout(() => {
      section.style.opacity = '1';
      section.style.transform = 'translateY(0)';
    }, index * 120); // 每行间隔 120ms
  });
}

// 页面加载后初始化
document.addEventListener('DOMContentLoaded', function() {
  console.log('工作经历折叠功能已加载');
});
